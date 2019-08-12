import functools
import json
import traceback
from datetime import datetime as c_datetime
from datetime import date, time
from sqlalchemy import DateTime, Numeric, Date, Time
from flask import Response
from flask_sqlalchemy import Model
from werkzeug.exceptions import BadRequest
from tools.exceptions import *


def standard_resp(func):
    """
    Creates a standardized response. This function should be used as a decorator.
    :function: The function decorated should return a dict with one of the keys  bellow:
        success -> GET, 200
        error -> Bad Request, 400
        created -> POST, 200
        updated -> PUT, 200
        deleted -> DELETE, 200
        no-data -> No Content, 204
        not-exist -> Not Exist 404
        no-access -> NoAccessError 403
        internal-error -> InternalError 500
        ……
    :returns: json.dumps(response), status code
    """

    @functools.wraps(func)
    def make_response(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except (ReturnDataError, InputError) as e:
            return resp_error(400, str(e), data=e.data)
        except AuthFailureError as e:
            return resp_error(401, str(e), data=e.data)
        except NoAccessError as e:
            return resp_error(403, str(e), data=e.data)
        except (NotExistError, NotFoundError) as e:
            return resp_error(404, str(e), data=e.data)
        except (ConnectionError, TypeError, BadRequest) as e:
            return resp_error(500, str(e))
        except (InternalError, NeedRecordError, K8sError, GitError, DevopsBusyError) as e:
            return resp_error(500, str(e), data=e.data)
        except Exception as e:
            return resp_error(500, str(e))
        if result is None:
            return resp_error(400, 'No Result')
        return Response(json.dumps({"code": 200, "result": result}, ensure_ascii=False),
                        content_type='application/json')

    return make_response


def resp_error(status, msg, data=None):
    traceback.print_exc()
    return {'status': status, 'msg': msg, 'data': data}, status


class Serializer(object):
    """
    公共序列化类，将ORM查询的Model转换成dict数据类型
    """
    @staticmethod
    def as_dict(models):
        # 将多Model联合查询对象转化为字典
        def result_to_dict(results):
            return [dict(zip(r.keys(), (convert_datetime(_r) if isinstance(_r, c_datetime) else _r for _r in r)))
                    for r in results]

        # 将实体类Model转化为字典
        def model_to_dict(model):
            for col in model.__table__.columns:
                if isinstance(col.type, DateTime):
                    value = convert_datetime(getattr(model, col.name))
                elif isinstance(col.type, Numeric):
                    value = float(getattr(model, col.name))
                else:
                    value = getattr(model, col.name)
                yield (col.name, value)

        # 对时间类型数据进行转换
        def convert_datetime(value):
            if isinstance(value, (c_datetime, DateTime)):
                return value.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(value, (date, Date)):
                return value.strftime("%Y-%m-%d")
            elif isinstance(value, (Time, time)):
                return value.strftime("%H:%M:%S")

        # 如果查询的是实体类集合
        if isinstance(models, list):
            # 如果是单个实体的查询
            if isinstance(models[0], Model):
                res = []
                for model in models:
                    _model = model_to_dict(model)
                    _res = dict((g[0], g[1]) for g in _model)
                    res.append(_res)
                return res
            # 如果是多model联合查询
            else:
                return result_to_dict(models)
        else:
            if isinstance(models, Model):
                return dict((g[0], g[1]) for g in model_to_dict(models))
            else:
                return dict(
                    zip(models.keys(), (convert_datetime(_r) if isinstance(_r, c_datetime) else _r for _r in models)))
