# -*- coding: utf-8 -*-

__author__ = 'patrick_psq'

import logging, os, re, time, base64, hashlib

from transwarp.web import get, view, post, ctx, interceptor, seeother, notfound

from models import User, Blog, Comment

from apis import api, APIError, APIValueError, APIPermissionError, APIResourceNotFoundError

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

@api
@get('/api/users')
def api_get_users():
    users = User.find_by('order by created_at desc')
    for u in users:
        u.password = '******'
    return dict(users=users)
