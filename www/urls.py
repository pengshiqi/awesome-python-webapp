# -*- coding: utf-8 -*-

__author__ = 'patrick_psq'

import logging

from transwarp.web import get, view

from models import User, Blog, Comment

# @view('test_users.html')
# @get('/')
# def test_users():
#     users = User.find_all()
#     return dict(users=users)

@view('blogs.html')
@get('/')
def index():
    blogs = Blog.find_all()
    # 查找登录用户
    user = User.find_first('where email=?', 'patrick_psq@outlook.com')
    return dict(blogs=blogs, user=user)
