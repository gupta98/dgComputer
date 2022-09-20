from flaskSite import db


class User(db.model):
    __tablename__ = "users"
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    mongoid = db.Column(db.String, unique=True, nullable=False)


class Prodcut(db.model):
    __tablename__ = "products"
    productid = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String, unique=True, nullable=False)
    productcategory = db.Column(db.String, unique=False, nullable=False)
    productimageurl = db.Column(db.String, unique=True, nullable=True)
    productcost = db.Column(db.Float, unique=False, nullable=False)
    productquantity = db.Column(db.Integer, unique=False, nullable=False)