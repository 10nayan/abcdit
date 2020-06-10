from flask import Flask,render_template,request,url_for,redirect,session,flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
from flask_session import Session
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime,date
from passlib.hash import pbkdf2_sha256
from models import *
import requests
import numpy as np
import numpy.linalg
from flask_socketio import SocketIO,send,emit
app = Flask(__name__)
app.secret_key="qwerty"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:Nayan@123.@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
Session(app)
socketio = SocketIO(app)
notes=[]
data={'results1':"",'results2':"",'results3':'','results4':'','results5':''}
users={}
db=SQLAlchemy(app)
login=LoginManager(app)
login.init_app(app)
@login.user_loader
def user_loader(id):
    return User.query.get(int(id))
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.email=='nayan.h4.aec@gmail.com'
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('signin', next=request.url))
admin = Admin(app)
admin.add_view(MyModelView(User, db.session))
def validate_email(email):
    if email[-4::]=='.com' or email[-3::]=='.in':
        return True
    else:
        return False
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
        password2=request.form.get("password2")
        hashed=pbkdf2_sha256.hash(password)
        if User.query.filter_by(email=email).first():
            flash(u"Email already exists","danger")
            return redirect(url_for('signup'))
        if password!=password2:
            flash(u"Both password should be same","warning")
            return redirect(url_for('signup'))
        if not validate_email(email):
            flash(u"Email not valid","error")
            return redirect(url_for('signup'))
        user=User(first_name=first_name,last_name=last_name,email=email,gender=gender,birthday=birthday,hash=hashed)
        db.session.add(user)
        db.session.commit()
        flash(u"You have registered successfully","success")
        return redirect(url_for('signin'))
    return render_template("signup.html")
@app.route("/signin",methods=["POST","GET"])
def signin():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        user=User.query.filter_by(email=email).first()
        if current_user.is_active:
            flash(u"You are already logged in","warning")
            return redirect(url_for('signin'))
        if not user:
            flash(u'User not found','error')
            return redirect(url_for('signin'))
        if not pbkdf2_sha256.verify(password,user.hash):
            flash(u"Incorrect password","danger")
            return redirect(url_for('signin'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template("signin.html")
@app.route("/calender",methods=["POST","GET"])
def calender():
	return render_template("calender.html")
@app.route("/convert")
def convert():
    return render_template("convert.html")
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
@app.route("/search",methods=["GET","POST"])
def search():
    search_input=request.form.get('search_name').lower()
    print(search_input)
    if search_input[0]=="w":
        return redirect(url_for('weather'))
    if search_input[0]=="m":
        return redirect(url_for('chat'))
    if search_input[0]=="a":
        return redirect(url_for('about'))
    if search_input[0]=="h":
        return redirect(url_for('home'))
    if search_input[0]=="s":
        if not current_user.is_authenticated:
            flash(u"You haven't logged yet","error")
            return redirect(url_for('signin'))
        return redirect(url_for('signout'))
    if search_input[0:3]=="cal":
        return redirect(url_for('calculate'))
    if search_input[0:2]=="co":
        return redirect(url_for('convert'))
    if search_input[0:2]=="ch":
        return redirect(url_for('chat'))
    if search_input[0]=="c":
        return redirect(url_for('calender'))
    return render_template("base.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route('/signout')
def signout():
    logout_user()
    flash(u"You have logged out","success")
    return redirect(url_for('signin'))
@app.route("/calculate",methods=["GET"])
def calculate():
    return render_template("calculate.html",data=data)
@app.route("/calculate/quadratic",methods=["POST"])
def quadratic():
    try:
        a=request.form.get('a')
        b=request.form.get('b')
        c=request.form.get('c')
        data['results1']=np.roots([a,b,c])
    except:
        data['results1']="Error, either a=0 or some input field left empty"
    return render_template("calculate.html",data=data)
@app.route("/calculate/linear",methods=["POST"])
def Linear():
    try:
        a1=request.form.get('a1')
        b1=request.form.get('b1')
        c1=request.form.get('c1')
        a2=request.form.get('a2')
        b2=request.form.get('b2')
        c2=request.form.get('c2')
        A=np.array([[a1,b1],[a2,b2]],dtype='float')
        b=np.array([c1,c2],dtype='float')
        data['results2']=numpy.linalg.solve(A,b)
    except:
        data['results2']="Error in calulation or some input field left empty"
    return render_template("calculate.html",data=data)
@app.route("/calculate/integrate",methods=["POST"])
def integrate():
    try:
        a2=request.form.get('a2')
        b2=request.form.get('b2')
        c2=request.form.get('c2')
        d2=request.form.get('d2')
        e2=request.form.get('e2')
        f2=request.form.get('f2')
        array=np.array([a2,b2,c2,d2,e2,f2],dtype='float')
        data['results3']=np.polyint(array)
    except:
        data['results3']="Error in calulation or some input field left empty"
    return render_template("calculate.html",data=data)
@app.route("/calculate/differenciate",methods=["POST"])
def differenciate():
    try:
        a3=request.form.get('a3')
        b3=request.form.get('b3')
        c3=request.form.get('c3')
        d3=request.form.get('d3')
        e3=request.form.get('e3')
        f3=request.form.get('f3')
        array=np.array([a3,b3,c3,d3,e3,f3],dtype='float')
        data['results4']=np.polyder(array)
    except:
        data['results4']="Error in calulation or some input field left empty"
    return render_template("calculate.html",data=data)
@app.route("/calculate/evaluate",methods=["POST"])
def evaluate():
    try:
        a4=request.form.get('a4')
        b4=request.form.get('b4')
        c4=request.form.get('c4')
        d4=request.form.get('d4')
        e4=request.form.get('e4')
        x=request.form.get('x')
        array=np.array([a4,b4,c4,d4,e4],dtype='float')
        data['results5']=np.polyval(array,int(x))
    except:
        data['results5']="Error in calulation or some input field left empty"
    return render_template("calculate.html",data=data)
@app.route("/chat",methods=["GET","POST"])
def chat():
    if not current_user.is_authenticated:
        flash(u"You have to login first","error")
        return redirect(url_for('signin'))
    name=current_user.first_name
    email=current_user.email
    return render_template("chat.html",name=name,email=email)
@socketio.on('message')
def handle_message(email):
    users[email]=request.sid
    send(email)
    emit('my_event','This task is also completed')
@socketio.on('new_event')
def handle_newevent(message):
    try:
        receiver_session_id=users[message['receiver']]
        message['time']=datetime.now().strftime("%I:%M %p")
        emit('new_response',message,room=receiver_session_id)
        print(users)
    except:
        message['name']="Server"
        message['msg']=message['receiver']+"  has left or not available"
        message['time']=datetime.now().strftime("%I:%M %p")
        emit('new_response',message)
        print(users)
@login_required
@app.route("/chat/leave")
def leave():
    users.pop(current_user.email,None)
    return  redirect(url_for('index'))
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
if __name__ == '__main__':
	socketio.run(app,debug=True)
