import datetime

from exts import db


class BaseModel(object):
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)
    update_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.datetime.now)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()

    # 添加多条数据
    def save_all(self, *args):
        try:
            db.session.add_all(args)
            db.session.commit()
        except:
            db.session.rollback()

    # 删除一条数据
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
