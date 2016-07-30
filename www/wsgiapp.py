# -*- coding: utf-8 -*-

__author__ = 'patrick_psq'

import logging; logging.basicConfig(level=logging.INFO)
import os

from transwarp import db
from transwarp.web import WSGIApplication, Jinja2TemplateEngine

from config import configs

# init the Database
db.create_engine(**configs.db)

# create a WSGIApplication
wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))

# init jinja2 template engine
template_engine = Jinja2TemplateEngine(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
wsgi.template_engine = template_engine

# 加载带有@get/@post的URL处理函数
import urls
wsgi.add_module(urls)

if __name__ == '__main__':
    wsgi.run(9000)
