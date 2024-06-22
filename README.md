[TOC]

## 需求分析

本项目是面向师生**日常开课教学及交流讨论**需求的集**评课、选课、贴吧**为一体的**前后端分离**的小型综合性课程平台。平台分设**管理员、教师、学生**三类用户，为不同用户提供了不同界面设计及应用支持。教师和学生账号可由用户自主注册创建，管理员账号只允许后台开设。

其中面向管理员开放的功能主要有：

- 课程管理：对每学期的课程进行开设、规定、介绍或删除
- 课堂管理：综合对不同课堂的教室和时间安排进行统筹，避免发生冲突（系统程序保证）
- 用户管理：对平台中教师和学生用户的人员信息进行统一管理
- 教材管理：平台可对部分小容量的教材资料进行统一收管，供教师学生下载使用
- 言论管理：对学生评价和自由讨论社区的帖子进行管理

其中面向教师开放的功能主要有：

- 介绍课程：向教师介绍本学期可以开设的课程详情，便于教师根据课程内容开设对应的课堂
- 管理课堂：对不同课程可自主选择是否开设对应课堂或停止自己已经开设的课堂
- 上传成绩: 查看已开设课堂的学生平均成绩，根据成绩单上传自己课堂学生的对应成绩
- 上传教材：根据上课需求上传资料到教材库中供学生下载使用
- 查看评价：在留言板的评价区查看学生给自己课堂的评价及打分
- 自由言论：在讨论区发帖跟帖自由交流讨论

其中面向学生开放的功能主要有：

- 介绍课程：向学生介绍本学期开设的课程详情，如学分、教学内容等
- 选择课堂：对不同课程开设的多个课堂选择其中之一修学或退选
- 查看成绩: 查看已选课堂的已获成绩及学期平均绩点
- 下载教材：根据上课需求下载教材库中的资料
- 评价课堂：在讨论区评价课堂教学质量并进行五等级制打分
- 自由言论：在讨论区发帖跟帖自由讨论

## 总体设计

### 系统模块结构

#### 前端设计

> 本项目前端设计文件夹为/frontend
> For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

##### 目录解析

```
.
├── build/                      # webpack配置文件，运行自动生成
│   └── ...
├── config/
│   ├── index.js                # 项目主要配置概览
│   └── ...
├── dist/
│   ├── static/                 # 前端静态资源和组件引用存放处
│   └── ...
├── src/                        # 主要代码工作编写目录
│   ├── main.js                 # app entry file, 前端主JSON文件，负责创建APP并挂载
│   ├── App.vue                 # main app component，前端Vue文件渲染入口，由router路由组织后续页面展示
│   ├── components/             # Vue文件主要编写目录，将前端子页面各自组织成组件形式方便路由管理
│   │   └── Admin/               # 管理员账号界面设计区
|   |     └── ...
│   │   └── Teacher/             # 教师账号界面设计区
|   |     └── ...
│   │   └── Student/             # 学生账号界面设计区
|   |     └── ...
│   |   └── HelloWorld.vue      # CourseSys平台首页
│   ├── router/                 # URL路由跳转配置
│   |   └── index.js
│   ├── util/                 # Cookie设置配置
│   |   └── cookie.js
│   └── assets/                 # module assets (processed by webpack)
│       └── ...
├── static/                     # pure static assets (directly copied)
├── test/                       # Vue提供的部分测试文件
│   └── ...
├── .babelrc                    # babel config
├── .editorconfig               # indentation, spaces/tabs and similar settings for your editor
├── .eslintrc.js                # eslint config
├── .eslintignore               # eslint ignore rules，eslint对代码编写风格有强制性要求，若影响编译或调试可在此处ignore部分文件的代码规范约束
├── .gitignore                  # sensible defaults for gitignore
├── index.html                  # 前端网页组织的主入口HTML文件
├── package.json                # 项目所需的前端脚本和环境依赖配置详情
├── vue.config.js               # vue config
└── README.md                   # Default README file
```

##### 运行逻辑

前端主要负责用户与系统界面的人机交互：

每一个`.vue`文件都主要由`<template>`、`<script>`、`<style>`三部分组成，template 负责页面展示布局设计，script 负责数据传输、方法挂载、页面跳转等动态控制，style 负责页面元素显示的样式静态控制。为每一个前端子页面设计一个对应的组件（vue 文件），通过`router/index.js`import 不同组件并由 url 路径设计路由跳转方式，当 vue 中的 template 只有`<router-view></router-view>`元素时，该页面不单独显示而只是作为路由中转。

在 vue 中主要通过：`this.$router.push({path: "xxx", query: { xx:xx, ...},});`来直接实现页面跳转，`this.$http.request({ url: that.$url + "xxx", method: "get", params: {xx:xx, ...},})`来实现从后端获取相应数据；script 中的`components`、`data`、`methods`分别对应组件、后端数据和前端交互方法的声明注册；若需要在页面初显示时即有后端数据显示，那么需要在 script 的`mounted`里为 methods 函数提前声明并挂载，类似提前声明变量，进入页面且内容全部渲染完成后自动调用函数。

若想增加一个新页面，步骤是：在`src/components/`里编写对应 Vue 文件，根据页面数据需求在后端文件的`urls.py`和`views.py`添加对应方法类和 get 调用接口，在前端文件的 router/index.js 里设置路由跳转路径，即可。

##### 启动方式

```bash
# install dependencies
npm install
# build for production with minification
npm run build
# serve with hot reload at localhost:8080
npm run dev
```

其他启动配置可以在`package.json`的`"scripts"`字段修改。

#### 后端设计

> 本项目后端设计文件夹为/backend
> For a detailed explanation on how things work, check out the [guide](https://vscode.github.net.cn/docs/python/tutorial-django).

##### 目录解析

```
.                                   # 以下大部分文件在django项目创建完毕后自动生成，无需过多编辑
├── __init__.py
├── __pycache__                     # python运行缓存目录
│   └── ...
├── migrations                      # 与App迁移打包有关的目录
│   ├── __init__.py
│   └── ...
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── base_mysql.py                   # pymysql提供的mysql高级编程接口，负责运行mysql语句返回数据
├── urls.py                         # 前端可利用http请求从此处的url中获取数据库数据返回给前端
└── views.py                        # 前端与pymysql的编程接口，负责数据传输的字段对接和初步处理
```

##### 运行逻辑

后端主要负责前端与数据库的数据交互：
`urls.py`和`views.py`搭配提供了前端 vue 文件和 pymysql 的调用接口，利用 django.urls、views 和 rest_framework 包为不同的 http get 请求设计对应的方法类，负责后端数据清洗处理以及与前端请求字段的对齐。
`base_mysql.py`提供了 pymysql 和 mysql 数据库的高级编程接口，主要是定义了一个主类`MySQL`，通过类方法控制数据库的连接和关闭、不同 Mysql 语句的执行及数据返回。
若要增加一个与数据库的数据交互，步骤是定义类内方法：

```python
connection,cursor = self.connectDataBase()    #连接数据库并创建游标
instruction = "Mysql合法语句，参数由%s占位"     #待执行mysql语句
cursor.execute(instruction, 参数列表)          #执行mysql增删查改DML命令
# cursor.callproc('过程名',args=参数列表)      #执行mysql的存储过程或函数
result = cursor.fetchone()/cursor.fetchall()  #游标返回一行或全部数据元组
# 可根据需要选择异步执行mysql便于进行异常控制，如
# try:
#     instruction = "xxx"
#     cursor.execute(instruction, ...)
#     connection.commit()
# except Exception as e:
#     connection.rollback()
#     print("执行MySQL xxx错误")
self.closeDataBase(connection, cursor)        #关闭数据库链接
return result                                 #返回数据结果
```

##### 启动方式

使用如下命令启动创建好的 Django 项目：

```bash
python manage.py runserver
```

使用上述命令正确启动项目后，终端显示如下(显示地址可命令行或配置文件中更改)：

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
June 22, 2024 - 14:14:12
Django version 5.0.6, using settings 'admin.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```