---
title: LearnGit02
summary:
    Learn Git From Liao 
tags:
  - Git
...

# Learn Git 02 #

## git标签 ##

### 创建标签 ###
需要切换到分支，`git checkout master`  

    git tag <name>

### 为历史添加标签 ###

先查询commit ID  
`git log --pretty=oneline --addrev-commit`  
	
	git tag <name> CommitID
	git tag -a v0.1 -m "version 0.1 released" 3628164	#-a 指定名称 -m说明文字
	git show <tagname>			#可查看说明文字
	git tag -s <tagname>			#添加私钥

### 操作标签 ###

	git tag -d <tagname>		#删除标签
	git push origin <tagname>	#想远程库添加标签
删除远程库标签

	git tag -d	<tagname>				 	#先删除本地库的标签
	git push origin :refs/tags/<tagname>	#向远程库推送删除消息

## 使用GitHub ##
先登录github账户,Fork他人项目,再从个人账户上拷下项目  
`git clone git@github.com:<UserName>/<OriginName>.git`

## 自定义Git ##

### 颜色修改 ###
对git status的输出修改颜色

	git config --global color.ui true

### git的过滤 ###
`.gitignore`文件,为git的提交提供过滤
  
强制添加可以使用`git add -f FILE`

### 配置别名alias ###

    git config	--global alias.<ShortName>	<Command>  

修改`git log`的输出  
`git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"`

后文还有建设git服务器的文章。  
[资料来源](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137583770360579bc4b458f044ce7afed3df579123eca000)