from sqlalchemy import Column, Integer, String, Text
from apis.base.base_model import BaseModel
from exts import db


class DemoOne(db.Model, BaseModel):
    __tablename__ = 'demo_one'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(15), nullable=False, unique=True, index=True)
    name = Column(String(100))
    description = Column(Text)

    def __repr__(self):
        return '<DemoOne %r>' % self.id


class DemoTwo(db.Model):
    __tablename__ = "demo_two"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    code = Column(Integer)

    def __repr__(self):
        return '<DemoTwo %r>' % self.id
