from flask import Blueprint
from flask_restplus import Api

from apis.demo.views import ns_demo_one
from apis.demo.views import ns_demo_two
from apis.project.views import ns_project

authorizations = {
    'token': {
        'type': 'apiKey',
        'in': 'header',
        'name': '认证token值'
    }
}

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, title='Devops', version='1.0', description='Devops 1.0后台接口文档', authorizations=authorizations,
          security=['token'], ordered=True, doc="/docs")

# demo模块
api.add_namespace(ns_demo_one)
api.add_namespace(ns_demo_two)
# 项目模块
api.add_namespace(ns_project)
