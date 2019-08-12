from flask import Flask, request
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from apiv1 import blueprint
from settings import CONFIG
from exts import db

# 需要传递一个参数__name__
# 1、方便flask框架去寻找资源
# 2、方便flask插件比如Flask-SQLAlchemy出现错误的时候好去寻找问题所在的位置
app = Flask(__name__)

# 注册蓝图
app.register_blueprint(blueprint)

# 读取并加载数据库配置
app.config.from_object(CONFIG['local'])
db.init_app(app)

# migrate
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.before_request
def process_request(*args, **kwargs):
    request.user_info = {"name": "devops"}
    # 验证表示，任何地址请求都会先执行before_request，所以登录验证就可以在before_request里做用户认证功能了
    print("其他请求之前就执行了process_request")


@app.after_request
def process_response(response):
    print("其他请求结束后就执行了process_response")
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    manager.run()
