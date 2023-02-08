from marshmallow import Schema, fields

from setup_db import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(300), nulltable=False)
    name = db.Column(db.String(100))
    surname = db.Colum(db.String(100))
    favorite_genre = db.Column(db.String(100))


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()