---
title: 安装lxml的血与泪
summary:
   lxml真的好难安装啊！快崩溃了，花了一晚上呢！
tags:
  - python
...
# 安装lxml的辛酸泪 #

##开始的错误##

起初不能成功安装lxml，使publish.py不能正常from lxml import html, 导致不能成功发布博客。

返回值```ImportError: No module named lxml```

所以我尝试```pip install lxml```，但仍然返回错误

```/bin/python -c "import setuptools, tokenize;__file__='/tmp/pip-build-7HN4t8/lxml/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /tmp/pip-LUVnYB-record/install-record.txt --single-version-externally-managed --compile --install-headers /root/pycode/blogenv/include/site/python2.7/lxml" failed with error code 1 in /tmp/pip-build-7HN4t8/lxml```


通过找各种资料尝试，无果。我决定卸载python的虚拟环境重新安装虚拟环境，并安装包。

##这次的思路为##

- 更新软件包
- 更新pip
- 检查requirements.txt的包是否齐全
- 通过pip安装requirement.txt

首先```apt-get update```更新软件包，然后```python -m pip install -U pip```

更新pip，最后查看requirements.txt文件

```
Babel==2.3.4
blinker==1.4
click==6.6
coverage==4.2
decorator==4.0.10
Flask==0.11.1
Flask-Babel==0.11.1
Flask-Login==0.3.2
Flask-Mail==0.9.1
flask-mongoengine==0.8
Flask-OpenID==1.2.5
Flask-Script==2.0.5
Flask-SQLAlchemy==2.1
Flask-WhooshAlchemy==0.56
Flask-WTF==0.12
flipflop==1.0
guess-language==0.2
itsdangerous==0.24
Jinja2==2.8
Markdown==2.6.6
markdown2==2.3.1
MarkupSafe==0.23
pbr==1.10.0
pyjwt==1.4.2
python-openid==2.2.5
pytz==2016.6.1
PyYAML==3.12
requests==2.11.1
six==1.10.0
SQLAlchemy==1.0.15
sqlalchemy-migrate==0.10.0
sqlparse==0.2.1
Tempita==0.5.2
Werkzeug==0.11.11
Whoosh==2.7.4
WTForms==2.1
lxml==3.5.0
```

这是拿windows上python的requirement文件，有许多包不用安装，修改太麻烦就没有动。

最后我们使用pip安装```pip install -r requirements.txt```


终于迎来了喜讯


```Successfully installed Babel-2.3.4 Flask-0.11.1 Flask-Babel-0.11.1 Flask-Login-0.3.2 Flask-Mail-0.9.1 Flask-OpenID-1.2.5 Flask-SQLAlchemy-2.1 Flask-Script-2.0.5 Flask-WTF-0.12 Flask-WhooshAlchemy-0.56 Jinja2-2.8 Markdown-2.6.6 MarkupSafe-0.23 PyYAML-3.12 SQLAlchemy-1.0.15 Tempita-0.5.2 WTForms-2.1 Werkzeug-0.11.11 Whoosh-2.7.4 blinker-1.4 click-6.6 coverage-4.2 decorator-4.0.10 flask-mongoengine-0.8 flipflop-1.0 guess-language-0.2 itsdangerous-0.24 lxml-3.5.0 markdown2-2.3.1 mongoengine-0.10.6 pbr-1.10.0 pyjwt-1.4.2 pymongo-3.3.0 python-openid-2.2.5 pytz-2016.6.1 requests-2.11.1 six-1.10.0 sqlalchemy-migrate-0.10.0 sqlparse-0.2.1```


成功安装，然后使用publish.py提交.md文件即可生成博文，可见flask的强大！