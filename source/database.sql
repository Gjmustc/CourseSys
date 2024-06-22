-- MySQL 8.0.18
DROP DATABASE IF EXISTS CourseSys;
CREATE DATABASE CourseSys;
use CourseSys;

SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

/*==============================================================*/
/* Table: admin                                                 */
/*==============================================================*/
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `admin_account` char(7) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `admin_password` char(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'admin',
  `admin_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`admin_account`) USING BTREE,
  UNIQUE KEY UQ_adminaccount (`admin_account`) USING BTREE,
  UNIQUE KEY UQ_adminname (`admin_name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Dumping data for table `admin`
--
LOCK TABLES `admin` WRITE;
INSERT INTO `admin` VALUES ('admin01','123456','管理员01');
UNLOCK TABLES;

/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `stuid` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stuname` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stupassword` char(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stumajor` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stuyear` ENUM('2020','2021','2022','2023','2024') NOT NULL ,
  `stuemail` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`stuid`) USING BTREE,
  UNIQUE KEY UQ_stuid (`stuid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- LOCK TABLES `student` WRITE;
INSERT INTO `student` VALUES
('PB20210001', '张三', 'password001', '计算机科学与技术', '2021', 'zhangsan@example.com'),
('PB20210002', '李四', 'password002', '应用数学', '2021', 'lisi@example.com'),
('PB20210003', '王五', 'password003', '软件工程', '2021', 'wangwu@example.com'),
('PB20210004', '赵六', 'password004', '网络通信', '2021', 'zhaoliu@example.com');

-- UNLOCK TABLES;
/*==============================================================*/
/* Table: teacher                                               */
/*==============================================================*/
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `teacherid` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teachername` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teacherpassword` char(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teacheremail` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`teacherid`) USING BTREE,
  UNIQUE KEY UQ_teacherid (`teacherid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- LOCK TABLES `teacher` WRITE;
INSERT INTO `teacher` VALUES
('TA00000001', '张老师', 'password001', 'zhang@example.com'),
('TA00000002', '李老师', 'password002', 'li@example.com'),
('TA00000003', '王老师', 'password003', 'wang@example.com'),
('TA00000004', '赵老师', 'password004', 'zhao@example.com');
-- UNLOCK TABLES;

/*==============================================================*/
/* Table: course                                                */
/*==============================================================*/

DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `courseid` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `admin_account` char(7) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `coursename` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `credit` int NOT NULL CHECK (`credit` >= 1 AND `credit` <= 6),
  `courseintro` varchar(1024) CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (`courseid`) USING BTREE,
  UNIQUE KEY UQ_coursename (`coursename`) USING BTREE,
  CONSTRAINT FK_start_course FOREIGN KEY (`admin_account`) REFERENCES `admin` (`admin_account`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Dumping data for table `course`
--
-- LOCK TABLES `course` WRITE;
INSERT INTO `course` VALUES
('005109', 'admin01', '计算机基础', 3, '这门课程介绍计算机科学的基本概念，包括硬件、软件、编程和数据结构。'),
('005110', 'admin01', '高级编程', 4, '本课程重点讲授高级编程技巧和设计模式，适合有一定编程基础的学生。'),
('005111', 'admin01', '数据结构', 3, '学习各种数据结构及其在计算机科学中的应用。课程内容包括数组、链表、栈、队列、树和图。'),
('005112', 'admin01', '操作系统', 4, '课程涵盖操作系统的基本原理和概念，如进程管理、内存管理、文件系统和设备管理。'),
('005113', 'admin01', '数据库系统', 3, '介绍数据库系统的基本原理，包括数据模型、数据库设计、SQL语言和数据库管理系统。'),
('005114', 'admin01', '计算机网络', 3, '本课程介绍计算机网络的基础知识和协议，包括TCP/IP、网络编程和网络安全。'),
('005115', 'admin01', '软件工程', 3, '学习软件开发的基本原则和实践，包括需求分析、设计、测试和维护。'),
('005116', 'admin01', '人工智能', 4, '介绍人工智能的基本概念和技术，包括机器学习、神经网络和自然语言处理。'),
('005117', 'admin01', '编译原理', 4, '学习编译器的设计和实现，包括词法分析、语法分析和代码生成。'),
('005118', 'admin01', '计算机图形学', 3, '课程内容包括计算机图形学的基本概念和技术，如图形生成、变换、光照和动画。');
-- UNLOCK TABLES;

/*==============================================================*/
/* Table: class                                                 */
/*==============================================================*/
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `classid` char(9) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teacherid` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `courseid` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class_time` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `classroom` char(7) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class_hold` int NOT NULL DEFAULT 60,
  `current_sel` int DEFAULT 0,
  `class_material` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `avg_mark` FLOAT DEFAULT 0,
  PRIMARY KEY (`classid`) USING BTREE,
  CONSTRAINT FK_course_class FOREIGN KEY (`courseid`) REFERENCES `course` (`courseid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT FK_start_class FOREIGN KEY (`teacherid`) REFERENCES `teacher` (`teacherid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Dumping data for table `class`
--
-- LOCK TABLES `class` WRITE;
INSERT INTO `class` VALUES 
('005109.01','TA00000001','005109','2024春/周一/6-7节',  'GTA-101',60,2, '计算机基础',88.5),
('005109.02','TA00000002','005109','2024春/周二/3-4节',  'GTA-201',60,0, '计算机基础',0),
('005109.03','TA00000003','005109','2024春/周一/3-4节',  'GTA-103',60,2, '计算机基础',87.5),
('005110.01','TA00000001','005110','2024春/周三/6-7节',  'GTA-301',60,0, '高级编程',0),
('005110.02','TA00000003','005110','2024春/周四/3-4节',  'GTA-401',60,0, '高级编程',0),
('005111.01','TA00000002','005111','2024春/周三/8-10节', 'GTB-101',120,2,'数据结构',82.5),
('005111.02','TA00000003','005111','2024春/周四/6-7节', 'GTB-201',120,0,'数据结构',0),
('005111.03','TA00000004','005111','2024春/周五/8-10节','GTB-301',120,0,'数据结构',0),
('005114.01','TA00000002','005114','2024春/周四/8-10节', 'GTC-401',80,2,'计算机网络',87.5),
('005114.02','TA00000004','005114','2024春/周一/6-7节',  'GTC-403',80,2, '计算机网络',85),
('005113.01','TA00000001','005113','2024春/周五/10-11节','GTB-201',120,4,'数据库原理及实践',77.75);
-- UNLOCK TABLES;

/*==============================================================*/
/* Table: comment                                               */
/*==============================================================*/
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `commentid` int NOT NULL AUTO_INCREMENT,
  `classid` char(9) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stuid` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class_grade` int NOT NULL CHECK (`class_grade` >= 1 AND `class_grade` <= 5),
  `comment_time` DATETIME NOT NULL,
  `comment_content` varchar(1024) CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (`commentid`) USING BTREE,
  UNIQUE KEY UQ_commentid (`commentid`) USING BTREE,
  CONSTRAINT FK_commented FOREIGN KEY (`classid`) REFERENCES `class` (`classid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT FK_commentor FOREIGN KEY (`stuid`) REFERENCES `student` (`stuid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
--
-- Dumping data for table `comment`
--
-- LOCK TABLES `comment` WRITE;
INSERT INTO `comment` VALUES
(NULL, '005109.01', 'PB20210001', 4, '2024-05-01 10:15:00', '这门课非常有趣且内容丰富。'),
(NULL, '005109.01', 'PB20210004', 4, '2024-05-02 11:30:00', '很棒的课程，学到了很多东西。'),
(NULL, '005109.01', 'PB20210004', 5, '2024-05-04 13:00:00', '内容非常好，课程结构很好。'),
(NULL, '005109.03', 'PB20210003', 3, '2024-05-09 18:15:00', '讲解得很好，容易理解。'),
(NULL, '005109.03', 'PB20210002', 5, '2024-05-10 19:30:00', '这是我参加过的最好的课程之一。'),
(NULL, '005114.02', 'PB20210004', 3, '2024-05-05 14:15:00', '课程不错，但可以加入更多实践例子。'),
(NULL, '005114.02', 'PB20210004', 3, '2024-05-06 15:30:00', '非常详细且内容丰富。'),
(NULL, '005114.02', 'PB20210003', 5, '2024-05-07 16:45:00', '非常喜欢这种讲课的方式。'),
(NULL, '005113.01', 'PB20210003', 3, '2024-05-08 17:00:00', '课程很好，但节奏有点快。'),
(NULL, '005113.01', 'PB20210001', 4, '2024-05-09 18:15:00', '内容很实用，很喜欢。'),
(NULL, '005113.01', 'PB20210002', 5, '2024-05-10 19:30:00', '非常好的课程，推荐给大家。'),
(NULL, '005113.01', 'PB20210004', 4, '2024-05-11 20:45:00', '课程内容很实用，很喜欢。');


-- UNLOCK TABLES;

/*==============================================================*/
/* Table: course_materials                                      */
/*==============================================================*/
DROP TABLE IF EXISTS `course_materials`;
CREATE TABLE `course_materials` (
  `materialid` int  NOT NULL AUTO_INCREMENT,
  `teacherid` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `material_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `courseid` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `material` LONGBLOB DEFAULT NULL,
  PRIMARY KEY (`materialid`) USING BTREE,
  UNIQUE KEY UQ_materialname (`material_name`) USING BTREE,
  CONSTRAINT FK_course_use_materials FOREIGN KEY (`courseid`) REFERENCES `course` (`courseid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT FK_teacher_support_materials FOREIGN KEY (`teacherid`) REFERENCES `teacher` (`teacherid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
--
-- Dumping data for table `course`
--
-- LOCK TABLES `course_materials` WRITE;
-- INSERT INTO `course_materials` VALUES
-- (NULL, 'TA00000001', '计算机基础讲义', '005109', NULL),
-- (NULL, 'TA00000002', '高级编程教材', '005110', NULL),
-- (NULL, 'TA00000003', '数据结构讲义', '005111', NULL),
-- (NULL, 'TA00000004', '操作系统笔记', '005112', NULL),
-- (NULL, 'TA00000005', '数据库系统教程', '005113', NULL),
-- (NULL, 'TA00000006', '计算机网络资料', '005114', NULL),
-- (NULL, 'TA00000007', '软件工程讲义', '005115', NULL),
-- (NULL, 'TA00000008', '人工智能教材', '005116', NULL),
-- (NULL, 'TA00000009', '编译原理资料', '005117', NULL),
-- (NULL, 'TA00000010', '计算机图形学讲义', '005118', NULL);
-- UNLOCK TABLES;


/*==============================================================*/
/* Table: main_post                                             */
/*==============================================================*/
DROP TABLE IF EXISTS `main_post`;
CREATE TABLE `main_post`(
    `mainpostid` int NOT NULL AUTO_INCREMENT,
    `stuid` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
    `admin_account` char(7) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
    `teacherid` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
    `main_title` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `main_content` varchar(1024) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
    `main_postime` DATETIME NOT NULL,
    `iftea_post_main` BOOL NOT NULL,
  PRIMARY KEY (`mainpostid`) USING BTREE,
  CONSTRAINT FK_admin_post_main FOREIGN KEY (`admin_account`) REFERENCES `admin` (`admin_account`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT FK_stu_post_main FOREIGN KEY (`stuid`) REFERENCES `student` (`stuid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT FK_tea_post_main FOREIGN KEY (`teacherid`) REFERENCES `teacher` (`teacherid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
-- LOCK TABLES `main_post` WRITE;
INSERT INTO `main_post` VALUES
(NULL, NULL, NULL, 'TA00000001', '课程介绍', '这门课主要介绍计算机基础知识。', '2024-05-01 09:00:00', TRUE),
(NULL, 'PB20210002', NULL, NULL, '问题讨论', '关于数据库设计的一些问题讨论。', '2024-05-02 10:00:00', FALSE),
(NULL, NULL, 'admin01', NULL, '系统维护通知', '本周末系统将进行维护，请大家提前做好准备。', '2024-05-03 11:00:00', FALSE),
(NULL, 'PB20210004', NULL, NULL, '编程技巧', '分享一些高级编程技巧。', '2024-05-04 12:00:00', FALSE),
(NULL, NULL, NULL, 'TA00000002', '考试安排', '期末考试安排已公布，请查阅。', '2024-05-05 13:00:00', TRUE);
-- UNLOCK TABLES;

/*==============================================================*/
/* Table: follow_post                                           */
/*==============================================================*/
DROP TABLE IF EXISTS `follow_post`;
CREATE TABLE `follow_post` (
    `followpostid` int NOT NULL AUTO_INCREMENT,
    `stuid` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
    `mainpostid` int NOT NULL,
    `admin_account` char(7) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
    `teacherid` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
    `follow_content` varchar(1024) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
    `follow_postime` DATETIME NOT NULL,
    `iftea_post_follow` BOOL NOT NULL,
  PRIMARY KEY (`followpostid`) USING BTREE,
  CONSTRAINT FK_admin_post_follow FOREIGN KEY (`admin_account`) REFERENCES `admin` (`admin_account`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT FK_stu_post_follow FOREIGN KEY (`stuid`) REFERENCES `student` (`stuid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT FK_tea_post_follow FOREIGN KEY (`teacherid`) REFERENCES `teacher` (`teacherid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT FK_main2follow FOREIGN KEY (`mainpostid`) REFERENCES `main_post` (`mainpostid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- LOCK TABLES `follow_post` WRITE;
INSERT INTO `follow_post` VALUES
(NULL, 'PB20210001', 1, NULL, NULL, '谢谢老师的介绍，非常有帮助。', '2024-05-01 10:00:00', FALSE),
(NULL, 'PB20210004', 1, NULL, NULL, '非常感谢老师的辛勤付出。', '2024-05-02 11:00:00', FALSE),
(NULL, NULL, 2, 'admin01', NULL, '请大家积极参与讨论。', '2024-05-02 11:00:00', FALSE),
(NULL, 'PB20210003', 2, NULL, NULL, '我有一些问题想请教大神们。', '2024-05-02 11:30:00', FALSE),
(NULL, 'PB20210001', 2, NULL, NULL, '关于数据库设计的问题，我有一些建议。', '2024-05-02 12:00:00', FALSE),
(NULL, 'PB20210004', 3, NULL, NULL, '好的，我们会提前做好准备。', '2024-05-03 12:30:00', FALSE),
(NULL, 'PB20210001', 4, NULL, NULL, '非常实用的编程技巧，谢谢分享！', '2024-05-04 13:30:00', FALSE),
(NULL, 'PB20210002', 4, NULL, NULL, '有什么额外的课程或者资料推荐吗！', '2024-05-04 14:00:00', FALSE),
(NULL, NULL, 4,  NULL,'TA00000003', '这个同学可以参考一下这些资料。', '2024-05-04 14:30:00', TRUE),
(NULL, NULL, 5, NULL, 'TA00000002', '请同学们注意考试安排。', '2024-05-05 14:00:00', TRUE),
(NULL, 'PB20210004', 5, NULL, NULL, '好的，谢谢老师提醒。', '2024-05-05 14:30:00', FALSE);
-- UNLOCK TABLES;

/*==============================================================*/
/* Table: select_course                                         */
/*==============================================================*/
DROP TABLE IF EXISTS `select_course`;
CREATE TABLE `select_course`(
    `stuid` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `classid` char(9) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `grade` FLOAT DEFAULT NULL,
    PRIMARY KEY (`stuid`, `classid`) USING BTREE,
    CONSTRAINT FK_selected FOREIGN KEY (`classid`) REFERENCES `class` (`classid`) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK_selector FOREIGN KEY (`stuid`) REFERENCES `student` (`stuid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Dumping data for table `course`
--
-- LOCK TABLES `select_course` WRITE;
INSERT INTO `select_course` VALUES
('PB20210001', '005109.01', 85.00),
('PB20210001', '005114.01', 90.00),
('PB20210001', '005113.01', 68.00),
('PB20210004', '005109.01', 92.00),
('PB20210004', '005114.02', 80.00),
('PB20210004', '005113.01', 85.00),
('PB20210002', '005109.03', 90.00),
('PB20210002', '005114.01', 85.00),
('PB20210002', '005113.01', 88.00),
('PB20210002', '005111.01', 70.00),
('PB20210003', '005111.01', 95.00),
('PB20210003', '005109.03', 85.00),
('PB20210003', '005114.02', 90.00),
('PB20210003', '005113.01', 70.00);
-- UNLOCK TABLES;


SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
