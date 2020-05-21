from flask import Flask,render_template,request,url_for,redirect,session,flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
from flask_session import Session
from datetime import datetime,date
from passlib.hash import pbkdf2_sha256
from models import *
import requests
import numpy as np
import numpy.linalg
app = Flask(__name__)
app.secret_key="qwerty"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:Nayan@123.@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
Session(app)
notes=[]
data={'results1':"",'results2':"",'results3':'','results4':'','results5':''}
db=SQLAlchemy(app)
login=LoginManager(app)
login.init_app(app)
@login.user_loader
def user_loader(id):
    return User.query.get(int(id))
@app.route("/home")
def home():
    if current_user.is_active:
        name=current_user.first_name
    else:
        name=""
    today=date.today()
    d=today.strftime("%B %d %Y")
    now=datetime.now().strftime("%I:%M %p")
    return render_template("home.html",name=name,today=d,now=now)
@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method=="POST":
        first_name=request.form.get("first_name")
        last_name=request.form.get("last_name")
        email=request.form.get("email")
        gender=request.form.get("gender")
        birthday=request.form.get("birthday")
        password=request.form.get("password")
        hashed=pbkdf2_sha256.hash(password)
        user=User(first_name=first_name,last_name=last_name,email=email,gender=gender,birthday=birthday,hash=hashed)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("signup.html")
@app.route("/signin",methods=["POST","GET"])
def signin():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        user=User.query.filter_by(email=email).first()
        if current_user.is_active:
            flash("You are already logged in, logged out first")
            return redirect(url_for('signin'))
        if not user:
            flash('User not found')
            return redirect(url_for('signin'))
        if not pbkdf2_sha256.verify(password,user.hash):
            flash("Incorrect password")
            return redirect(url_for('signin'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template("signin.html")
@app.route("/more",methods=["POST","GET"])
def more():
	if session.get ("notes") is None:
		session["notes"]=[]
	if request.method=="POST":
		note=request.form.get("note")
		session["notes"].append(note)
	return render_template("more.html",notes=session["notes"],user=current_user)
@app.route("/converts",methods=["POST","GET"])
def converts():
    if request.method=="POST":
        other=request.form.get('other')
        res=requests.get("http://data.fixer.io/api/latest?access_key=5c0328116134b8ff2be7cb3103709f89&format=1",params={'symbols':other})
        if res.status_code!=200:
            raise Exception("Error :API request unsuccessful")
        data=res.json()
        rate=data['rates'][other]
        return f'1 EURO is equal to {rate} {other}'
    return '''<form method="POST">
        Enter The Currency Symbol to where you want to convert: <input type="text" name="other">
        <input type="submit">
        </form>'''
@app.route("/currency")
def currency():
    return render_template("currency.html")
@app.route("/convert",methods=["POST"])
def convert():
    currency = request.form.get("currency")

    res=requests.get("http://data.fixer.io/api/latest?access_key=5c0328116134b8ff2be7cb3103709f89&format=1",params={'symbols':currency})
    if res.status_code != 200:
        return jsonify({"success": False})
    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success": False})
    return jsonify({"success": True, "rate": data["rates"][currency]})
@app.route("/weather")
def weather():
    return render_template("weather.html")
@app.route("/")
def index():
    if current_user.is_active:
        name=current_user.first_name.capitalize()
    else:
        name="Guest"
    return render_template("base.html",name=name)
@app.route("/search")
def search():
    return render_template("search.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route('/signout')
@login_required
def signout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for('signin'))
@app.route("/calculate",methods=["GET"])
def calculate():
    return render_template("calculate.html",data=data)
@app.route("/calculate/quadratic",methods=["POST"])
def quadratic():
    a=request.form.get('a')
    b=request.form.get('b')
    c=request.form.get('c')
    data['results1']=np.roots([a,b,c])
    return render_template("calculate.html",data=data)
@app.route("/calculate/linear",methods=["POST"])
def Linear():
    a1=request.form.get('a1')
    b1=request.form.get('b1')
    c1=request.form.get('c1')
    a2=request.form.get('a2')
    b2=request.form.get('b2')
    c2=request.form.get('c2')
    A=np.array([[a1,b1],[a2,b2]],dtype='float')
    b=np.array([c1,c2],dtype='float')
    data['results2']=numpy.linalg.solve(A,b)
    return render_template("calculate.html",data=data)
@app.route("/calculate/integrate",methods=["POST"])
def integrate():
    a2=request.form.get('a2')
    b2=request.form.get('b2')
    c2=request.form.get('c2')
    d2=request.form.get('d2')
    e2=request.form.get('e2')
    array=np.array([a2,b2,c2,d2,e2],dtype='float')
    data['results3']=np.polyint(array)
    return render_template("calculate.html",data=data)
@app.route("/calculate/differenciate",methods=["POST"])
def differenciate():
    a3=request.form.get('a3')
    b3=request.form.get('b3')
    c3=request.form.get('c3')
    d3=request.form.get('d3')
    e3=request.form.get('e3')
    array=np.array([a3,b3,c3,d3,e3],dtype='float')
    data['results4']=np.polyder(array)
    return render_template("calculate.html",data=data)
@app.route("/calculate/evaluate",methods=["POST"])
def evaluate():
    a4=request.form.get('a4')
    b4=request.form.get('b4')
    c4=request.form.get('c4')
    d4=request.form.get('d4')
    e4=request.form.get('e4')
    x=request.form.get('x')
    array=np.array([a4,b4,c4,d4,e4],dtype='float')
    data['results5']=np.polyval(array,int(x))
    return render_template("calculate.html",data=data)
if __name__ == '__main__':
	app.run(debug=True)
