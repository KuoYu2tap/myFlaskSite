---
title: LearnGit01
summary:
    Learn Git From Liao 
tags:
  - Git
...

# Learn Git #

#### 基本操作 ####
`sudo apt-get git`   
`mkdir learngit` and `cd learngit`

`git init`  
生成了.git文件

>千万不要使用Windows自带的记事本编辑任何文本文件。原因是Microsoft开发记事本的团队使用了一个非常弱智的行为来保存UTF-8编码的文件，他们自作聪明地在每个文件开头添加了0xefbbbf（十六进制）的字符.

>TXT开头添加的**BOM头**是为了识别该文件为UTF8编码文件，其他的编译软件不识别

#### 添加文件 ####
`git add File`把文件添加到仓库   
`git commit -m "提示内容"`把文件提交到仓库,-m 添加操作说明  
`git status `查看仓库状态  
`git diff FILE` 查看文件  
`git log` 查看历史记录 _包含了修改时间_ --pretty=oneline 仅显示一行

#### 版本问题 ####
`HEAD`代表当前版本，`HEAD^`代表上一版本，`HEAD~100`上一百版本。

#### 版本回退 ####
`git reset -hard HEAD`  
`git reset -hard CommitId前几位` 找回以前的版本。  
不知道CommitId时，可以使用`git relog` 查看原来的操作指令。

#### 工作区和暂存区 ####
上文`mkdir learngit`创建的learngit文件夹为一个**工作区**  
工作区中有.git隐藏目录，为git的**版本库**  
`git add`把**工作区**的文件放入**暂存区**  
`git commit`把**暂存区**所有的修改提交到分支  

`git checkout --FILE`把FILE文件在工作区中的修改全部撤销  
事实上是让FILE文件回到执行`git add`或者`git commit`前的状态 
 
`git reset HEAD FILE`把FILE在暂存区的修改撤销，重新放回工作区  

## 删除文件 ##
#### 前提 ####
在文件管理器下删除了文件`rm FILE`,即工作区删除了文件  

#### 确认删除该文件 ####
`git rm FILE` and `git commit -m "删除FILE"`版本库上也删除了FILE

#### 误删除 ####
`git checkout --FILE`把版本库中的文件提出来。  
`git checkout`把版本库的文件提取出来，让本地文件一键还原。


## GitHub远程库 ##

#### 添加远程库 ####
在github中添加远程库 
 
	git remote add origin git@github.com:MyName/learngit.git 

本地库推送至远程库

	git push -u origin master	#初次使用，-u 关联分支
	git push origin master		#日后使用

#### 从远程库中克隆 ####
克隆远程库

    git clone git@github.com:Myname/NewGit.git

## 分支管理 ##
当只有一位开发者时只有`master`分支，我们采用的`HEAD`->`master`，
当我们创建一个`dev`新分支时，`HEAD`->`dev`  
分支的工作流程为:

	创建dev分支 -> 在dev分支下工作 -> 合并dev分支到master分支 -> 删除dev分支，主分支又进一步

#### 创建dev分支 ####
    git checkout -b dev		#-b 创建并切换
	git branch				#查看当前分支
	git checkout master		#切换到master分支

#### 合并分支并删除 ####
	git merge dev			#合并dev分支
	git cbranch -d dev		#删除分支

#### 冲突 ####
	git log --graph		#查看分支冲突示意图

#### 分支管理策略 ####

	git checkout -b dev
	git add file.txt	#在dev分支上添加文件
	git checkout master	#切换回master分支
	
	git merge --no-ff -m "merge --no-ff" dev		#禁用Fast forward即合并后不删除分支信息

#### bug分支 ####
>为了修改Bug,先存储当前工作,解决Bug后再提取出来。

	git stash					#储藏当前分支的工作
	git stash list				#查看储藏的分支
	
	git stash apply	stash@{No.}	#恢复储藏,但储藏的内容不消失,需要git stash drop
	git stash pop				#pop方式弹出储藏内容

#### Future分支 ####
> 为了添加一个新功能而创建的Future分支  
> 这是一个未合并的分支,删除时显示冲突

	git branch -d Future		#显示删除冲突,原因该分支未合并
	git branch -D Future		#成功删除

#### 多人协作 ####

查看远程库
 
	git remote		#返回远程库名列表，-v显示详细信息
	git pull		#从远程库抓取


因此，多人协作的工作模式通常是这样：  
1.首先，可以试图用git push origin branch-name推送自己的修改；  
2.如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；  
3.如果合并有冲突，则解决冲突，并在本地提交；  
4.没有冲突或者解决掉冲突后，再用git push origin branch-name推送就能成功！  
5.如果git pull提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream branch-name origin/branch-name。
6.这就是多人协作的工作模式，一旦熟悉了，就非常简单。