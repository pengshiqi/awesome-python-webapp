# -*- coding:utf-8 -*-

import re, json, logging, functools

from transwarp.web import ctx

__author__ = 'patrick_psq'

'''
JSON API definition
'''

def dumps(obj):
    return json.dumps(obj)


class APIError(StandardError):
    '''
    The base APIError which contains error(required), data(optional), and message(optional)
    '''
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('value:forbidden', 'permission', message)


def api(func):
    '''
    A decorator that makes a function ro json api, makes the return value as json

    @app.route('/api/test')
    @api
    def api_test():
        return dict(result='123', items=[])
    '''
    @functools.wraps(func)
    def _wrapper(*args, **kw):
        try:
            r = dumps(func(*args, **kw))
        except APIError, e:
            r = json.dumps(dict(error=e.error, data=e.data, message=e.message))
        except Exception, e:
            logging.exception(e)
            r = json.dumps(dict(error='internalerror', data=e.__class__.__name__, message=e.message))
        ctx.response.content_type = 'application/json'
        return r
    return _wrapper


if __name__ == '__main__':
    import doctest
    doctest.testmod()
