from app.db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    typeofbalance = db.Column(db.String(15))
    balance = db.Column(db.String(80))

    def __init__(self, username, typeofbalance , balance):
        self.username = username
        self.typeofbalance = typeofbalance
        self.balance = balance
