from sqlalchemy import UniqueConstraint, Column, Integer, String, Boolean, Text
from apis.base.base_model import BaseModel
from exts import db


class Environment(db.Model, BaseModel):
    __tablename__ = 'environment'
    __table_args__ = (UniqueConstraint('project_id', 'name'),)

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, nullable=False, index=True)
    name = Column(String(45), index=True)
    port = Column(Integer, nullable=False, unique=False, index=True)
    cpu = Column(Integer)
    mem = Column(Integer)
    https = Column(Boolean, default=False)
    indep_ingress = Column('indep_ingress', Boolean, default=False)
    vcode = Column(Boolean, default=False)
    network_isolated = Column(Boolean, default=False)
    use_internal_dns = Column('user_internal_dns', Boolean, nullable=False, default=False)
    public_dns_domain = Column('public_dns_domain', String(50), nullable=False, default="")
    create_user_id = Column('create_user_id', Integer, index=True, default=0)
    private = Column(Integer, default=0)
    prod = Column(Integer, default=0)
    label = Column(String(50))
    ingress_yaml = Column('ingress_yaml', Text)
    description = Column(Text)
    last_error_message = Column('last_error_message', Text)
    vdc = Column(String(20), nullable=False)
    run_type = Column('run_type', String(50), nullable=False, default="KUBERNETES")
    ssl_domain = Column(String(50))
    namespace = Column(String(50), nullable=False)

