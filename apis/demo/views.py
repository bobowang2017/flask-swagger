from flask import request

from apis.demo import ns_demo_one, ns_demo_two
from apis.demo.models import DemoOne, DemoTwo
from apis.demo.swagger import demo_one_get_parser, DemoOneSwagger, header, demo_one_post_parser
from exts import logger
from flask_restplus import Resource
from tools.helper import standard_resp, Serializer


@ns_demo_one.route("/list")
class DemoOneListResource(Resource):
    @standard_resp
    def post(self):
        data = [DemoOne(code="123", description="desc", name="test") for _i in range(3)]
        DemoOne.save_all(*tuple(data))
        return data.json


@ns_demo_one.route("/<application_id>")
@ns_demo_one.expect(header)
class DemoOneResource(Resource):
    @ns_demo_one.expect(demo_one_get_parser)
    @standard_resp
    def get(self, application_id):
        params = request.args
        data = DemoOne.query.all()
        return Serializer.as_dict(data)

    @ns_demo_one.expect(DemoOneSwagger)
    @standard_resp
    def post(self):
        params = request.args
        obj = DemoOne(code=params.data['code'], description=params.data['description'], name=params.data['name'])
        obj.save()
        logger.info("Add DemoOne Success")
        return "created"

    @standard_resp
    @ns_demo_one.expect(demo_one_post_parser)
    def put(self):
        print(request.get_json())
        return "updated"


@ns_demo_two.route("")
class DemoTwoResource(Resource):
    @standard_resp
    def get(self):
        data = DemoOne.query.join(DemoTwo, DemoOne.id == DemoTwo.id).with_entities(DemoOne.id, DemoOne.name,
                                                                                    DemoTwo.code, DemoOne.create_at).first()
        return Serializer.as_dict(data)


