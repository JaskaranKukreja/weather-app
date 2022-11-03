from flask import g, request, redirect, url_for,abort,make_response,jsonify
from jsonschema import validate,ValidationError

class NotFoundError(Exception):
    def __init__(self,message):
        self.message=message
        
def exception_handler(f):
    def wrapper(*args,**kwargs):
        try:
            return f(*args, **kwargs)
        except ValidationError as error:
            abort(make_response(jsonify({
                'status': 400,
                'message': error.message,
                'type': 'ValidationError'
            }), 400))
        except NotFoundError as error:
            abort(make_response(jsonify({
                'status': 404,
                'message': error.message,
                'type': 'NotFoundError'
            }), 404))
        except Exception as error:
            print(error)
            abort(make_response(jsonify({
                'status': 500,
                'message': "Internal server error",
            }), 500))
    # Renaming the function name:
    wrapper.__name__ = f.__name__
    return wrapper