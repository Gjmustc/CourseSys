<div style="text-align:center;font-size:2em;font-weight:bold">中国科学技术大学计算机学院</div>

<div style="text-align:center;font-size:2em;font-weight:bold">《数据库系统实验报告》</div>

<img src="./pics/logo.png" style="zoom: 50%;" />

<div style="display: flex;flex-direction: column;align-items: center;font-size:2em">
<div>
<p>实验题目：CourseSys评课选课系统</p>
<p>学生姓名：龚劲铭</p>
<p>学生学号：PB21111682</p>
<p>完成时间：2024年6月16日</p>
</div>
</div>

<div style="page-break-after:always"></div>

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

### 数据库设计

#### ER 图

![](/pics/ER.png)

#### 模式分解

**本数据库模式设计符合 3NF（无局部依赖、无传递依赖）**
分解举例：

1. 选课={学号（PK1）、课堂号（PK2）、选课学生、课程名、选课成绩}，由于存在*局部依赖*：（学号->选课学生），（课堂号->课程名），故分解成三个表（选课、学生、课堂）
2. 课堂={课堂号(PK)、职工号、课程号、上课教师、上课课程、上课时间……}，由于存在*传递依赖*：（课堂号->课程号，课程号->上课课程），（课堂号->职工号，职工号->上课教师），故分解成三个表（课堂、课程、教师）
3. 评价={评价 ID（PK）、学号、课堂号、课堂打分、评价内容、评价人……}，由于存在*传递依赖*：评价 ID->学号，学号->评价人，故单独分解出两个表（评价、学生），但若评价人允许学生匿名（每次自定义评价人名称），则不存在依赖学号->评价人，则原模式不存在传递依赖，可不分解。

模式列表：

> /source/database.sql

- admin(<u>admin_account</u>,admin_password,admin_name)
- student(<u>stuid</u>,stuname,stupassword,stumajor,stuyear,stuemail)
- teacher(<u>teacherid</u>,teachername,teacherpassword,teacheremail)
- course(<u>courseid</u>,admin_account,coursename,credit,courseintro)
- class(<u>classid</u>,teacherid,courseid,class_time,classroom,class_hold,current_sel,class_material,avg_mark)
- comment(<u>commentid</u>,classid,stuid,class_grade,comment_time,comment_content)
- course_materials(<u>materialid</u>, teacherid,material_name,courseid,material)
- main_post(<u>mainpostid</u>,stuid,admin_account,teacherid,main_title,main_content,main_postime,iftea_post_main)
- follow_post(<u>followpostid</u>,stuid,mainpostid,admin_account,teacherid,follow_content,follow_postime,iftea_post_follow)
- select_course(<u>stuid</u>,<u>classid</u>,grade)

#### Pysql 设计（存储过程、触发器、函数）

> /source/execute.sql

| 类型      | 名字                     | 参数/触发条件/返回值                            | 主要功能                                                                                                 |
| --------- | ------------------------ | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| TRIGGER   | UpdateClass_Avggrade     | AFTER UPDATE ON select_course                   | 教师上传一名学生成绩时，更新对应课堂的学生平均成绩                                                       |
| TRIGGER   | DELETEClass_Avggrade     | AFTER DELETE ON select_course                   | 学生退课时，更新对应课堂的学生平均成绩，不包括已退课学生成绩                                             |
| TRIGGER   | MINUSClassSelectNum      | AFTER DELETE ON select_course                   | 学生退课后选课人数自动-1                                                                                 |
| FUNCTION  | GetStu_gpa               | in:stu_id out:gpa                               | 根据学生学号获取已获全部课堂成绩，根据分数等级转换和对应课程学分计算学期当前绩点                         |
| FUNCTION  | GetClass_Avgrank         | in:class_id out:avg_rank                        | 根据课堂号从 comments 中计算平均学生打分（五等级制）                                                     |
| PROCEDURE | CheckClassroomConflict   | in:classtime/classroom 等 out:state             | 在教师开设课堂时检测同时同地是否有课堂安排冲突，根据所选教室类型确定课堂容量                             |
| PROCEDURE | CheckSelCourseConflict   | in:classid/stuid out:state                      | 在学生选课时检测是否重复选课、是否超过课堂容量、是否课堂时间安排冲突，若可以选课则对应课堂选课人数自动+1 |
| PROCEDURE | CheckMaterialDuplication | in:material_name/material(longblob)等 out:state | 在教师上传资料时检查是否重名                                                                             |

## 核心代码解析

> 仓库地址 [github](https://github.com/Gjmustc/CourseSys.git)

### 数据库实现部分讲解

> source/execute.sql

```mysql
DROP TRIGGER IF EXISTS UpdateClass_Avggrade;
DELIMITER //
CREATE TRIGGER UpdateClass_Avggrade AFTER UPDATE ON `select_course` FOR EACH ROW
BEGIN
    DECLARE stu_count INT DEFAULT 0;
    DECLARE old_avg FLOAT DEFAULT 0;
    SELECT COUNT(*) FROM `select_course` WHERE `select_course`.`classid` = new.classid AND `select_course`.`grade` IS NOT NULL INTO stu_count;
    ---- 根据教师上传成绩对应的课堂号，获取已选课且拥有成绩的学生人数
    IF stu_count != 0 THEN
        SELECT `avg_mark` FROM `class` WHERE `class`.`classid` = new.classid INTO old_avg;
        ---- 对有外键约束的表进行更新时，要暂时解除外键约束和安全检查
        SET FOREIGN_KEY_CHECKS = false;
        SET SQL_SAFE_UPDATES = OFF;
        IF old_avg IS NOT NULL THEN
            ---- 结合旧平均分和学生人数快速计算新的平均分
            UPDATE `class` SET `avg_mark` = (old_avg * (stu_count - 1) + new.grade) / stu_count WHERE `class`.`classid` = new.classid;
        ELSE
            UPDATE `class` SET `avg_mark` = new.grade WHERE `class`.`classid` = new.classid;
        END IF;
        ---- 更新结束，恢复外键约束和安全检查
        SET SQL_SAFE_UPDATES = ON;
        SET FOREIGN_KEY_CHECKS = true;
    END IF;
END //
DELIMITER ;
------------------------------------------------------------------
DROP FUNCTION IF EXISTS GetStu_gpa;
DELIMITER //
CREATE FUNCTION GetStu_gpa(stu_id CHAR(10))
RETURNS FLOAT
READS SQL DATA
BEGIN
    DECLARE s , credit, total_credit INT DEFAULT 0;
    DECLARE grade, gpa, t FLOAT DEFAULT 0;
    ---- 为学生的成绩表建立游标
    DECLARE ct CURSOR FOR SELECT `select_course`.`grade`, `course`.`credit` FROM `select_course`,`course`,`class` WHERE `select_course`.`stuid`= stu_id AND `select_course`.`grade` IS NOT NULL AND `select_course`.`classid` = `class`.`classid` AND `class`.`courseid` = `course`.`courseid`;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET s = 1; -- 游标结束
    OPEN ct;
    REPEAT
    ---- 循环通过游标移动获取每项成绩和对应课程学分
        FETCH ct INTO grade, credit;
        IF s = 0 THEN
            CASE
                WHEN grade >= 95 THEN SET grade = 4.3;
                WHEN grade >= 90 AND grade <95 THEN SET t = 4.0;
                WHEN grade >= 85 AND grade <90 THEN SET t = 3.7;
                WHEN grade >= 82 AND grade <85 THEN SET t = 3.3;
                ELSE SET t = 3.0;
            END CASE;
            ---- 计算总学分和学分加权绩点和
            SET gpa = gpa + t * credit;
            SET total_credit =  total_credit + credit;
        END IF;
        UNTIL s = 1
    END REPEAT;
    ---- 计算平均绩点GPA并返回
    SET gpa = gpa / total_credit;
    ClOSE ct;
    RETURN gpa;
END //
DELIMITER ;
---------------------------------------------------------------
DROP PROCEDURE IF EXISTS CheckSelCourseConflict;
DELIMITER //
CREATE PROCEDURE CheckSelCourseConflict(IN stu_id char(10),  class_id char(9), OUT state INT)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET s = 1;
    START TRANSACTION;
    ---- 检查是否重复选课
    IF EXISTS(SELECT * FROM `select_course` WHERE `select_course`.`stuid` = stu_id AND `select_course`.`classid` = class_id) THEN
        SET s = 2;
    ---- 检查是否超过课堂容量
    ELSEIF EXISTS(SELECT * FROM `class` WHERE `class`.`classid` = class_id AND `class`.`current_sel` + 1 > `class`.`class_hold`) THEN
        SET s = 3;
    ---- 检查是否有时间冲突
    ELSEIF (SELECT `class_time` FROM `class` WHERE `class`.`classid` = class_id) IN (SELECT `class_time` FROM `class`,`select_course` WHERE `select_course`.`stuid` = stu_id AND `select_course`.`classid` = `class`.`classid`) THEN
        SET s = 4;
    ELSE
    ---- 没有冲突和异常，则更新对应课堂数据和选课数据
        SET FOREIGN_KEY_CHECKS = false;
        INSERT INTO `select_course` VALUES (stu_id, class_id, NULL);
        SET SQL_SAFE_UPDATES = OFF;
        UPDATE `class` SET `current_sel` = `current_sel` + 1 WHERE `classid` = class_id;
        SET SQL_SAFE_UPDATES = ON;
        SET FOREIGN_KEY_CHECKS = true;
    END IF;
    SET state = s;
    ---- 集中异常处理
    IF s = 0 THEN
        SELECT "Insert Select Course Success!";
        COMMIT;
    ELSE
        CASE s
            WHEN 1 THEN SELECT "Insert Select Course Failed!";
            WHEN 2 THEN SELECT "Course Already Selected!";
            WHEN 3 THEN SELECT "Classroom Capacity Exceeded!";
            WHEN 4 THEN SELECT "Classroom Time Conflict!";
        END CASE;
        ROLLBACK;
    END IF;
END //
DELIMITER ;
```

### 后端实现部分讲解

> backend/base_mysql.py 上传下载文件

```python
def convertToBinaryData(self, filename):
    # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def write_file(self, data, filename):
    # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def uploadMaterial(self, teacherid, material_name, coursename, material_path): #material_path为本机文件绝对路径
        connection, cursor = self.connectDataBase()
        courseid = ""
        state = 0
        # 异步执行文件上传
        try:
            print("Inserting LONGBLOB into course_material table")
            # 先获取课程名对应的课程号
            instruction = "SELECT courseid FROM course WHERE coursename = %s"
            cursor.execute(instruction, [coursename])
            courseid = cursor.fetchone()[0]   # 注意，这种写法才能只返回一个数据，而非一行或多行元组
            # 将上传文件转为二进制数据，便于存进mysql的LONGBLOB变量中
            material = self.convertToBinaryData(material_path)
            # 调用存储过程检查是否有重名冲突，没有则存储文件
            cursor.callproc('CheckMaterialDuplication',args=[teacherid,material_name,courseid,material,state])
            # 从存储过程中获得对应会话变量，这里是对应存储过程的返回参数state
            cursor.execute("SELECT @_CheckMaterialDuplication_4")
            state = cursor.fetchone()[0]
            # 根据state判断执行状态
            if state == 0:
              # 无异常则提交结果，并在后端打印提示
                connection.commit()
                print("Material inserted successfully as a LONGBLOB into course_materials table")
            else:
                print("Material already exists in course_materials table")
        except Exception as e:
          # 若出现异常则回滚并在终端打印报错信息
            connection.rollback()
            print("Failed inserting LONGBLOB data into MySQL table {}".format(e))
        self.closeDataBase(connection, cursor)
        return state

    def downloadMaterial(self, material_id, material_path):
        connection, cursor = self.connectDataBase()
        try:
            print("Reading LONGBLOB data from course_materials table")
            instruction = "SELECT material FROM course_materials WHERE materialid = %s"
            cursor.execute(instruction, [material_id])
            # 此时record获取到的是纯二进制数据
            record = cursor.fetchone()[0]
            print("Storing material on disk \n")
            # 将数据按照二进制格式写回到本地磁盘中
            self.write_file(record, material_path)
        except Exception as e:
            connection.rollback()
            print("Failed reading LONGBLOB data from MySQL table {}".format(e))
        self.closeDataBase(connection, cursor)
        return
```

> backend/views.py 用户登陆

```python
class StudentLogin(APIView):  #继承rest_framework.views父类APIView
  # 为前端的url+http request定义对应的get方法类
    def get(self,request):
      # GET和Response都是父类接口
      # 将前端url字段参数一律转为字符类型使用
        userid = str(request.GET.get('useraccount', None))
        password = str(request.GET.get('password', None))
        # 创建mysql接口
        sql = MySQL()
        # 调用接口查询
        result = sql.findStudent(userid)
        flag = not not result
        # 根据sql语句执行结果返回响应到前端，以字典格式（json格式）
        if not flag:
            return Response({"status": "fail", "message": "user not exists"})
        if result[2] != password:
            return Response({"status": "fail", "message": "password error"})
        return Response({"status": "success", "message": "login success"})
```

> backend/views.py 获取课程介绍信息

```python
class GetCourseInfo(APIView):
    def get(self,request):
        courseid = str(request.GET.get('courseid', None))
        sql = MySQL()
        result = sql.getCourseInfo(courseid)
        # 若数据库返回数据格式不符合前端显示需求，则需要中间处理
        # 数据库返回的不同属性值都可以用数组下标索引
        materiallist = []
        for i in result:
            materiallist.append(i[4] if i[4] is not None else "")
        # 将资料库中所有与该课程相关的资料名整合成清单显示
        course = {
            "courseid": result[0][0],
            "coursename": result[0][1],
            "coursecredit": result[0][2],
            "coursedescription": result[0][3] if result[0][3] is not None else "",
            "materiallist": materiallist,
        }
        return Response(course)
```

### 前端实现部分讲解

> frontend/src/components/Student/ClassTable/SelectClass.Vue

```Vue
<template>
...
<!-- 按钮组件el-button通过点击v-on:click绑定相关方法selectClass -->
<el-button-group style="margin-top: 2%">
   <el-button v-on:click="selectClass(index)" type="primary">选课</el-button>
</el-button-group>
...
</template>
<script>
export default{
  methods:{
    //前端使用的方法都在此定义
    selectClass(index) {
      // 网页端控制台信息输出，便于调试
      console.log(index);
      let that = this;
      // 利用http request向后端请求数据
      this.$http
        .request({
          url: that.$url + "SelectClass/",
          method: "get",
          params: {
            studentid: this.userAccount,
            classid: this.showClassList[index].classid,
          },
        })
        // 对后端传回数据进行分析，判断执行是否成功，若执行失败则message相关报错信息
        .then(function (response) {
          console.log(response.data);
          that.message = response.data.message;
          if (that.message === "select class success") {
            that.$message.success("选课成功");
          } else if (that.message === "class already selected") {
            that.$message.info("已选择该课程");
          } else if (that.message === "class is full") {
            that.$message.info("课堂容量已达上限");
          } else if (that.message === "time conflict") {
            that.$message.info("选课时间冲突");
          } else {
            that.$message.error("!");
          }
        });
    },
  }
}
</script>

```

> frontend/src/components/Student/Talk/StudentComment.Vue

```Vue
<template>
  ...
 <el-row>
    <div style="font-size: medium">给课程评分</div>
    <!-- 五等级制星级评分组件el-rate，数据v-model绑定到rank变量中 -->
      <el-rate style="font-size: medium" v-model="rank" show-text> </el-rate>
  </el-row>
  <el-row> &nbsp; </el-row>
  <el-row>
    <el-col>
    <!-- el-input获取表单输入，绑定到评价内容变量上 -->
      <el-input
                class="input"
                v-model="contentInput"
                type="textarea"
                :rows="3"
                placeholder="对于课程内容、讲课质量、考核方式等的评价"
              >
      </el-input>
    </el-col>
    <!-- el-button按钮组件点击事件绑定到CommentClass方法上（无需传参） -->
      <el-button
                v-on:click="CommentClass"
                type="primary"
                size="small"
                style="float: right"
                >添加评价
      </el-button>
  </el-row>
  ...
</template>

```

> frontend/src/components/Student/Talk/StudentDiscussTable.Vue

```Vue
<template>
<el-row>
<!-- 按钮点击事件绑定到对话框是否可见 -->
  <el-button
    @click="PostMainVisible = true"
    style="width: 100%"
    type="primary"
    >新建主贴
  </el-button>
  <!-- el-dialog 对话框组件弹出，供用户输入相关信息并提交，是否可见跟变量postmainvisible绑定 :visible.sync -->
  <el-dialog title="新建主帖" :visible.sync="PostMainVisible" width="70%">
     <el-row style="margin-bottom: 10px">
       <el-col>
         <el-input
           v-model="input.title"
           placeholder="请输入标题"
         ></el-input>
       </el-col>
     </el-row>
     <el-row style="margin-bottom: 10px">
       <el-col>
       <!-- quill-editor是可调用的富文本编辑组件，需要在script中先注册组件再使用 -->
         <quill-editor
           ref="text"
           v-model="input.content"
           style="height: 300px"
         ></quill-editor>
       </el-col>
     </el-row>
     <div slot="footer" class="dialog-footer" style="margin-top: 10%">
       <el-button @click="PostMainVisible = false">取消</el-button>
       <el-button type="primary" @click="PostMain">确定</el-button>
     </div>
  </el-dialog>
</el-row>
</template>

```

## 实验与测试

### 依赖

1. python 工具包: 详见根目录下的`requirements.txt`，执行`pip install -r requirements.txt`则可自动下载
2. 后端依赖：详见`/admin/settings.py`中的配置，主要需要自主修改的几步为：导入 pymysql 并`pymysql.install_as_MySQLdb()`，提供数据库编程接口，`STATICFILES_DIRS`添加自定义的静态资源位置，`DATABASES`配置应用连接的数据库，`INSTALLED_APPS`显式注明需要注册实现的 app 内容如`backend`项目，支持跨域配置`corsheaders`+`CORS_ALLOW_CREDENTIALS = True`等。
3. 前端依赖：详见`/frontend/package.json`中配置，主要字段为 vue 启动设置`scripts`，vue 项目相关依赖`dependencies`(包括`element-ui`/`vue-quill-editor`/`vue-router`)，vue 开发相关依赖`devDependencies`(包括`babel`/`css-loader`/`eslint`/`vue-loader`/`webpack`)等。

### 部署

启动项目只需要启动后端即可，进入项目根目录后运行`python manage.py runserver`。若要修改前端内容，则需要先进入 frontend 前端，运行`npm run install`（若没添加其他依赖无需运行此步）和`npm run build`，然后启动后端才会显示前端修改。

### 实验结果

#### 基本页面展示

![](/pics/主页.png)
![](/pics/学生首页.png)
![](/pics/学生登陆.png)

#### 增删改查基本功能

1. 学生选课(数据结构李老师)
   ![](/pics/选课成功.jpg)
   ![](/pics/新增选课.png)
2. 删除跟帖
   ![](/pics/删除前.png)
   ![](/pics/删除后.png)
3. 上传成绩(数据结构李老师)
   ![](/pics/新增选课.png)
   ![](/pics/上传成绩.jpg)
   ![](/pics/上传成绩后.png)

4. 查找课堂
   ![](/pics/查找课堂.png)

#### 存储过程

检查课堂安排冲突(想开设的操作系统课堂与已有的计算机基础课堂安排冲突)
![](/pics/新开课堂.jpg)
![](/pics/课堂冲突.jpg)

#### 函数调用

获得学生平均绩点（退课后会实时更新）
![](/pics/学生绩点.png)
![](/pics/退课.jpg)
![](/pics/更新绩点.png)

#### 触发器

实时更新课堂评价平均评分
![](/pics/评价删除前.png)
![](/pics/评价删除后.png)

#### 文件管理（资料上传下载）

![](/pics/文件上传前.jpg)
![](/pics/文件上传.jpg)
![](/pics/文件下载.png)
![](/pics/下载成功.png)

## 参考

- 前端模板：https://element.eleme.cn/#/zh-CN
- Vue 教程：http://vuejs-templates.github.io/webpack/、http://vuejs.github.io/vue-loader、https://cn.vuejs.org/guide/quick-start.html
- Django 教程：https://vscode.github.net.cn/docs/python/tutorial-django
