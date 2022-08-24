from start import db


class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    brand=db.Column(db.String(100))
    model=db.Column(db.String(100))
    description=db.Column(db.String(200))
    

class Customer(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(80))
    email=db.Column(db.String(80))