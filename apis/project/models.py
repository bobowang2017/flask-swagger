import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, UniqueConstraint
from apis.base.base_model import BaseModel
from exts import db


class Project(db.Model, BaseModel):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    code = Column(String(15), nullable=False, unique=True, index=True)
    name = Column(String(100))
    description = Column(Text)
    resource_id = Column(Integer)
    avatar = Column(String(255))
    status = Column(Integer)
    domain = Column(String(100), nullable=False, default='cm-dt.com')
    created_by = Column('created_by', Integer)
    harbor_id = Column(Integer)
    start_date = Column('start_date', DateTime, default=datetime.datetime.now())
    end_date = Column('end_date', DateTime, default=datetime.datetime.now())


class ProjectUser(db.Model, BaseModel):
    __tablename__ = 'project_user'
    __table_args__ = (UniqueConstraint('project_id', 'user_id', 'role_code'),)

    id = Column(Integer, primary_key=True)
    project_id = Column('project_id', Integer)
    user_id = Column('user_id', Integer)
    role_code = Column('role_code', index=True, nullable=False)