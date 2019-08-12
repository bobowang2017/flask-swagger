from flask import request
from flask_restplus import Resource

from apis.project import ns_project
from tools.helper import standard_resp


@ns_project.route("")
class ProjectResource(Resource):
    @ns_project.doc(params={'id': 'An ID'})
    @standard_resp
    def get(self):
        params = request.args
        return "success"
