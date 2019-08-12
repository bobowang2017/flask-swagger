from flask_restplus import fields

from apis.demo import ns_demo_one

# 定义请求头
header = ns_demo_one.parser()
header.add_argument('project_id', type=str, location="headers", help="项目ID", required=True)

# 定义实体对象
DemoOneSwagger = ns_demo_one.model('DemoOne', {
    'code': fields.String(description='The name', required=True),
    'project_id': fields.Integer(min=1),
    'description': fields.String,
    'name': fields.String
})

demo_one_get_parser = ns_demo_one.parser()
demo_one_get_parser.add_argument('code', type=int, help='项目Code')
demo_one_get_parser.add_argument('description', type=str, help="描述信息")
demo_one_get_parser.add_argument('name', type=str, help="名称")

demo_one_post_parser = ns_demo_one.parser()
demo_one_post_parser.add_argument('project_id', type=str, location="headers", help="项目ID")
demo_one_post_parser.add_argument('code', type=int, help='Code')
demo_one_post_parser.add_argument('description', type=str, help="描述信息")
demo_one_post_parser.add_argument('name', type=str, help="名称")

# https://flask-restplus.readthedocs.io/en/stable/swagger.html
