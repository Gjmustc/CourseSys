use CourseSys;

DROP TRIGGER IF EXISTS UpdateClass_Avggrade;
DELIMITER //
CREATE TRIGGER UpdateClass_Avggrade AFTER UPDATE ON `select_course` FOR EACH ROW
BEGIN
    DECLARE stu_count INT DEFAULT 0;
    DECLARE old_avg FLOAT DEFAULT 0;
    SELECT COUNT(*) FROM `select_course` WHERE `select_course`.`classid` = new.classid AND `select_course`.`grade` IS NOT NULL INTO stu_count;
    IF stu_count != 0 THEN
        SELECT `avg_mark` FROM `class` WHERE `class`.`classid` = new.classid INTO old_avg;
        SET FOREIGN_KEY_CHECKS = false;
        SET SQL_SAFE_UPDATES = OFF;
        IF old_avg IS NOT NULL THEN
            UPDATE `class` SET `avg_mark` = (old_avg * (stu_count - 1) + new.grade) / stu_count WHERE `class`.`classid` = new.classid;
        ELSE
            UPDATE `class` SET `avg_mark` = new.grade WHERE `class`.`classid` = new.classid;
        END IF;
        SET SQL_SAFE_UPDATES = ON;
        SET FOREIGN_KEY_CHECKS = true;
    END IF;
END //
DELIMITER ;

DROP TRIGGER IF EXISTS DELETEClass_Avggrade;
DELIMITER //
CREATE TRIGGER DELETEClass_Avggrade AFTER DELETE ON `select_course` FOR EACH ROW
BEGIN
    DECLARE stu_count INT DEFAULT 0;
    DECLARE old_avg FLOAT DEFAULT 0;
    SELECT COUNT(*) FROM `select_course` WHERE `select_course`.`classid` = old.classid AND `select_course`.`grade` IS NOT NULL INTO stu_count;
    SET FOREIGN_KEY_CHECKS = false;
    SET SQL_SAFE_UPDATES = OFF;
    IF stu_count != 0 THEN
        SELECT `avg_mark` FROM `class` WHERE `class`.`classid` = old.classid INTO old_avg;
        UPDATE `class` SET `avg_mark` = (old_avg * (stu_count + 1) - old.grade) / stu_count WHERE `class`.`classid` = old.classid;
    ELSE
        UPDATE `class` SET `avg_mark` = NULL WHERE `class`.`classid` = old.classid;
    END IF;
    SET SQL_SAFE_UPDATES = ON;
    SET FOREIGN_KEY_CHECKS = true;
END //
DELIMITER ;


DROP TRIGGER IF EXISTS MINUSClassSelectNum;
DELIMITER //
CREATE TRIGGER MINUSClassSelectNum AFTER DELETE ON `select_course` FOR EACH ROW
BEGIN
    SET FOREIGN_KEY_CHECKS = false;
    SET SQL_SAFE_UPDATES = OFF;
    UPDATE `class` SET `class`.`current_sel` = `class`.`current_sel` - 1 WHERE `class`.`classid` = old.classid;
    SET SQL_SAFE_UPDATES = ON;
    SET FOREIGN_KEY_CHECKS = true;
END //
DELIMITER ;

DROP FUNCTION IF EXISTS GetStu_gpa;
DELIMITER //
CREATE FUNCTION GetStu_gpa(stu_id CHAR(10))
RETURNS FLOAT
READS SQL DATA
BEGIN
    DECLARE s , credit, total_credit INT DEFAULT 0;
    DECLARE grade, gpa, t FLOAT DEFAULT 0; 
    DECLARE ct CURSOR FOR SELECT `select_course`.`grade`, `course`.`credit` FROM `select_course`,`course`,`class` WHERE `select_course`.`stuid`= stu_id AND `select_course`.`grade` IS NOT NULL AND `select_course`.`classid` = `class`.`classid` AND `class`.`courseid` = `course`.`courseid`;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET s = 1; -- 游标结束
    OPEN ct;
    REPEAT
        FETCH ct INTO grade, credit;
        IF s = 0 THEN
            CASE
                WHEN grade >= 95 THEN SET grade = 4.3;
                WHEN grade >= 90 AND grade <95 THEN SET t = 4.0;
                WHEN grade >= 85 AND grade <90 THEN SET t = 3.7;
                WHEN grade >= 82 AND grade <85 THEN SET t = 3.3;
                ELSE SET t = 3.0;
            END CASE;
            SET gpa = gpa + t * credit;
            SET total_credit =  total_credit + credit;
        END IF;
        UNTIL s = 1 
    END REPEAT;
    SET gpa = gpa / total_credit;
    ClOSE ct;
    RETURN gpa;
END //
DELIMITER ;

DROP FUNCTION IF EXISTS GetClass_Avgrank;
DELIMITER //
CREATE FUNCTION GetClass_Avgrank(class_id CHAR(9))
RETURNS FLOAT
READS SQL DATA
BEGIN
    DECLARE s, total_comment, onerank, total_rank INT DEFAULT 0;
    DECLARE avg_rank FLOAT DEFAULT 0;
    DECLARE ct CURSOR FOR (SELECT `class_grade` FROM `comment` WHERE `classid` = class_id);
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET s = 1; -- 游标结束
    OPEN ct;
    REPEAT
        FETCH ct INTO onerank;
        IF s = 0 THEN
            SET total_comment = total_comment + 1;
            SET total_rank = total_rank + onerank;
        END IF;
        UNTIL s = 1 
    END REPEAT;
    ClOSE ct;
    If total_comment = 0 THEN
        SET avg_rank = NULL;
    ELSE
        SET avg_rank = total_rank / total_comment;
    END IF;
    RETURN avg_rank;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS CheckClassroomConflict;
DELIMITER //
CREATE PROCEDURE CheckClassroomConflict(IN class_time varchar(20),  class_room char(7),  class_id char(9),  teacher_id char(10), course_id char(6),  class_material varchar(20), OUT state INT)
BEGIN
    DECLARE s, class_hold INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET s = 1; 
    START TRANSACTION;
    IF EXISTS(SELECT * FROM `class` WHERE `class`.`classroom` = class_room AND `class`.`class_time` = class_time) THEN -- 课程安排冲突
        SET s = 2;
    ELSE 
        SET FOREIGN_KEY_CHECKS = false;
        CASE
            WHEN class_room LIKE 'GTA%' THEN SET class_hold = 60;
            WHEN class_room LIKE 'GTB%' THEN SET class_hold = 120;
            WHEN class_room LIKE 'GTC%' THEN SET class_hold = 80;
            ELSE SET class_hold = 60;
        END CASE;
        INSERT INTO `class` VALUES (class_id, teacher_id, course_id, class_time, class_room, class_hold, 0, class_material, NULL);
        SET FOREIGN_KEY_CHECKS = true;
    END IF;
    SET state = s;
    IF s = 0 THEN
        SELECT "Insert Class Success!";
        COMMIT;
    ELSE
        CASE s
            WHEN 1 THEN SELECT "Insert Class Failed!";
            WHEN 2 THEN SELECT "Class Conflict!";
        END CASE;
        ROLLBACK;
    END IF;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS CheckUpdateClassroomConflict;
DELIMITER //
CREATE PROCEDURE CheckUpdateClassroomConflict(IN class_time varchar(20),  class_room char(7),  class_id char(9),  class_material varchar(20), OUT state INT)
BEGIN
    DECLARE s, class_hold INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET s = 1; 
    START TRANSACTION;
    IF EXISTS(SELECT * FROM `class` WHERE `class`.`classroom` = class_room AND `class`.`class_time` = class_time AND `class`.`classid` != class_id) THEN -- 课程安排冲突
        SET s = 2;
    ELSE 
        SET FOREIGN_KEY_CHECKS = false;
        CASE
            WHEN class_room LIKE 'GTA%' THEN SET class_hold = 60;
            WHEN class_room LIKE 'GTB%' THEN SET class_hold = 120;
            WHEN class_room LIKE 'GTC%' THEN SET class_hold = 80;
            ELSE SET class_hold = 60;
        END CASE;
        SET SQL_SAFE_UPDATES = OFF;
        UPDATE `class` SET `class_time` = class_time, `classroom` = class_room, `class_hold` = class_hold, `class_material` = class_material WHERE `classid` = class_id;
        SET SQL_SAFE_UPDATES = ON;
        SET FOREIGN_KEY_CHECKS = true;
    END IF;
    SET state = s;
    IF s = 0 THEN
        SELECT "Update Class Success!";
        COMMIT;
    ELSE
        CASE s
            WHEN 1 THEN SELECT "Update Class Failed!";
            WHEN 2 THEN SELECT "Class Conflict!";
        END CASE;
        ROLLBACK;
    END IF;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS CheckSelCourseConflict;
DELIMITER //
CREATE PROCEDURE CheckSelCourseConflict(IN stu_id char(10),  class_id char(9), OUT state INT)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET s = 1;
    START TRANSACTION;
    IF EXISTS(SELECT * FROM `select_course` WHERE `select_course`.`stuid` = stu_id AND `select_course`.`classid` = class_id) THEN
        SET s = 2;
    ELSEIF EXISTS(SELECT * FROM `class` WHERE `class`.`classid` = class_id AND `class`.`current_sel` + 1 > `class`.`class_hold`) THEN
        SET s = 3;
    ELSEIF (SELECT `class_time` FROM `class` WHERE `class`.`classid` = class_id) IN (SELECT `class_time` FROM `class`,`select_course` WHERE `select_course`.`stuid` = stu_id AND `select_course`.`classid` = `class`.`classid`) THEN
        SET s = 4;
    ELSE
        SET FOREIGN_KEY_CHECKS = false;
        INSERT INTO `select_course` VALUES (stu_id, class_id, NULL);
        SET SQL_SAFE_UPDATES = OFF;
        UPDATE `class` SET `current_sel` = `current_sel` + 1 WHERE `classid` = class_id;
        SET SQL_SAFE_UPDATES = ON;
        SET FOREIGN_KEY_CHECKS = true;
    END IF;
    SET state = s;
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

DROP PROCEDURE IF EXISTS CheckMaterialDuplication;
DELIMITER //
CREATE PROCEDURE CheckMaterialDuplication(IN teacher_id char(10),  material_name varchar(30),  course_id char(6),  material LONGBLOB, OUT state INT)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET s = 1;
    START TRANSACTION;
    IF EXISTS(SELECT * FROM `course_materials` WHERE `course_materials`.`material_name` = material_name) THEN
        SET s = 2;
    ELSE
        SET FOREIGN_KEY_CHECKS = false;
        INSERT INTO `course_materials` VALUES (NULL, teacher_id, material_name, course_id, material);
        SET FOREIGN_KEY_CHECKS = true;
    END IF;
    SET state = s;
    IF s = 0 THEN
        SELECT "Insert Material Success!";
        COMMIT;
    ELSE
        CASE s
            WHEN 1 THEN SELECT "Insert Material Failed!";
            WHEN 2 THEN SELECT "Material Already Exists!";
        END CASE;
        ROLLBACK;
    END IF;
END //
DELIMITER ;





DROP VIEW IF EXISTS studentPostMain;
CREATE VIEW studentPostMain (postid, id, title, content, postime, iftea)
AS SELECT mainpostid, stuid, main_title, main_content, main_postime, iftea_post_main FROM main_post WHERE stuid IS NOT NULL;

DROP VIEW IF EXISTS teacherPostMain;
CREATE VIEW teacherPostMain (postid, id, title, content, postime,iftea)
AS SELECT mainpostid, teacherid, main_title, main_content, main_postime,iftea_post_main FROM main_post WHERE teacherid IS NOT NULL;

DROP VIEW IF EXISTS adminPostMain;
CREATE VIEW adminPostMain (postid, id, title, content, postime,iftea)
AS SELECT mainpostid, admin_account, main_title, main_content, main_postime,iftea_post_main FROM main_post WHERE admin_account IS NOT NULL;

DROP VIEW IF EXISTS studentPostFollow;
CREATE VIEW studentPostFollow (postid, id, mainid, content, postime,iftea)
AS SELECT followpostid, stuid, mainpostid, follow_content, follow_postime,iftea_post_follow FROM follow_post WHERE stuid IS NOT NULL;

DROP VIEW IF EXISTS teacherPostFollow;
CREATE VIEW teacherPostFollow (postid, id, mainid, content, postime,iftea)
AS SELECT followpostid, teacherid, mainpostid, follow_content, follow_postime,iftea_post_follow FROM follow_post WHERE teacherid IS NOT NULL;

DROP VIEW IF EXISTS adminPostFollow;
CREATE VIEW adminPostFollow (postid, id, mainid, content, postime,iftea)
AS SELECT followpostid, admin_account, mainpostid, follow_content, follow_postime,iftea_post_follow FROM follow_post WHERE admin_account IS NOT NULL;