from db import db
from models.category import CategoryModel


class StoreModel(db.Model):
    __tablename__  = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    categories = db.relationship("CategoryModel", back_populates = "store", lazy="dynamic")