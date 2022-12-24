from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    firm = db.Column(db.String(100), nullable=False)
    info = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    currency = db.Column(db.Text)
    # theDate = db.Column(db.String(100))


    def __repr__(self):
        return self.title