# awesome-python-webapp

An awesome python webapp learnt from Micheal Liao.

### Day 01

Build the environment.

### Day 02

Database module.

### Day 03

ORM(Object Relational Mapping) module.

### Day 04

Model module.

### Day 05

Web framework module.

### Day 06

Add config files.

### Day 07

MVC module.

### Day 08

Front-end module.

### Day 09

API module.

### Day 10

User register and log in.
```
localhost:9000/register
localhost:9000/login
```

### Day 11

Blog creating page.
```
localhost:9000/mange/blogs/create
```

### Day 12

Blog list page.
```
localhost:9000/manage/blogs
```

### Day 13

Add pymonitor.py(DEBUG model).

### Day 14

Accomplished!

## 运行方式

进入/www目录下，运行 wsgiapp.py 文件，在浏览器中进入127.0.0.1:9000，即可看到博客页面。

此前需要在config文件中设置本地数据库的连接方式，username和password。需要在本地的mysql数据库中创建一个名为awesome的database，在其中建立名为users,blogs和comments的表，这些在schema.sql中已经写好，在命令行中运行schema.sql即可。
```
mysql -u root -p < schema.sql
```
即可完成数据库表的初始化。

## Reference

* [python教程 实战](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013976177048818eb4187c05a84f9280169d58e22afa09000)
