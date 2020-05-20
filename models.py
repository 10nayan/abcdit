from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class User(db.Model,UserMixin):
  __tablename__="users"
  id = db.Column(db.Integer,primary_key=True)
  date=db.Column(db.DateTime,default=datetime.now())
  first_name = db.Column(db.String,nullable=False)
  last_name = db.Column(db.String,nullable=False)
  email= db.Column(db.String,unique=True,nullable=False)
  gender = db.Column(db.String,nullable=False)
  birthday = db.Column(db.String,nullable=False)
  hash=db.Column(db.Text,nullable=False)
  def __init__(self,first_name,last_name,email,gender,birthday,hash):
    self.email=email
    self.first_name=first_name
    self.last_name=last_name
    self.gender=gender
    self.birthday=birthday
    self.hash=hash
