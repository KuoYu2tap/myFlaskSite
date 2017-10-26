---
title: 使用Nginx+gunicorn部署Flask
summary:
  如果想使Flask顺利运行,单单使用Flask自带的server是不够的。因此我们需要Nginx+gunicorn协同工作。
tags:
  - mysite
...

# 使用Nginx+gunicorn部署Flask #
> &nbsp;&nbsp;如果想使Flask顺利运行,单单使用Flask自带的server是不够的。因此我们需要Nginx+gunicorn协同工作。


&nbsp;&nbsp;其实单gunicorn也可以使Flask成功发布，但是遭遇本地多个web服务都需要监听80端口时，就没有办法转发，因此需要gunicorn负责转发服务，配合Nginx工作。当然uWSGI也可以胜任转发工作。


&nbsp;&nbsp;如果本机确定只跑这一个服务，由于gunicorn的性能问题以及对各种Http请求缓冲头的处理没有Nginx完善，我们还是需要Nignx提供正式的服务
[资料来源](http://zhidao.baidu.com/link?url=Leky7je6XUPF4iuLa5EaHU3KYQ37Frt_mtK4_mwwrr6lnsMWIJ_s5KSIf4-D3D2bemjC1oFZhGMFGsh2SgUUHSuiM-w2Om-yjKcw6n9MDF7)

## Gunicorn的安装与配置 ##

打开python的虚拟环境virtualenv。

```$ source /flask/bin/activate ```

运行pip安装

```(flask)$ pip install gunicorn```

运行gunicorn

```(flask)$ gunicorn -w 8 -b 127.0.0.1:8080 run:app```

这里的-w 8参数是打开八个进程（worker）同时处理HTTP请求。-b 127.0.0.1:端口号是设置监听端口，我们设置为8080以供设置Nginx。后面的run:app，是指本地上的run.py中的app实例。

## Nginx的安装和配置 ##

这里我们不使用python的虚拟环境，所以执行```deactivate```退出虚拟环境。直接apt-get安装nginx。

```$ apt-get install nginx```

然后我们转向Nginx的默认配置文件

```$ cd /etc/nginx/site-avalidable/default```

在目录下备份默认文件```sudo cp default default.bak```

修改default文件，因为Nginx的版本不同，需要把没有出现的语句都注释掉。

```$ sudo vim default```

	server {
    	listen 80;
    	server_name example.org; # 这是HOST机器的外部域名，用地址也行```

		location / {
        	proxy_pass http://127.0.0.1:8080; # 这里是指向 gunicorn host 的服务地址
        	proxy_set_header Host $host;
        	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    	}
	}

然后重新启动nginx

```$ sudo service nginx restart```

后文有让flask程序在linux启动时运行的操作，不赘述。

[资料来源](http://www.cnblogs.com/Ray-liang/p/4837850.html)


