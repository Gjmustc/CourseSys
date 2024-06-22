import pymysql
import datetime
class MySQL:

    def connectDataBase(self):
        connection = pymysql.connect(host="localhost",
                                     db="CourseSys",
                                     user="root",
                                     passwd="091305",
                                     charset='utf8')
        cursor = connection.cursor()
        return connection, cursor
    
    def closeDataBase(self, connection, cursor):
        cursor.close()
        connection.close()
        return

    def registerStudent(self, stuid, stuname, stupassword, stumajor, stuyear, stuemail):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "INSERT INTO student (stuid, stuname, stupassword, stumajor, stuyear, stuemail) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(instruction, [stuid, stuname, stupassword, stumajor, stuyear, stuemail])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL registerStudent错误")
        self.closeDataBase(connection, cursor)
        return
    
    def registerTeacher(self, teacherid, teachername, teacherpassword, teacheremail):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "INSERT INTO teacher (teacherid, teachername, teacherpassword, teacheremail) VALUES (%s, %s, %s, %s)"
            cursor.execute(instruction, [teacherid, teachername, teacherpassword, teacheremail])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL registerTeacher错误")
        self.closeDataBase(connection, cursor)
        return

    def findAdmin(self, admin_account):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT * FROM admin WHERE admin_account = %s"
        cursor.execute(instruction, [admin_account])
        result = cursor.fetchone()
        self.closeDataBase(connection, cursor)
        return result
    
    def findStudent(self, stuid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT * FROM student WHERE stuid = %s"
        cursor.execute(instruction, [stuid])
        result = cursor.fetchone()       
        self.closeDataBase(connection, cursor)
        return result
    
    def findTeacher(self, teacherid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT * FROM teacher WHERE teacherid = %s"
        cursor.execute(instruction, [teacherid])
        result = cursor.fetchone()   
        self.closeDataBase(connection, cursor)
        return result
    
    def adminPasswordChange(self, admin_account, admin_password):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "UPDATE admin SET admin_password = %s WHERE admin_account = %s"
            cursor.execute(instruction, [admin_password, admin_account])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL adminPasswordChange错误")
        self.closeDataBase(connection, cursor)
        return
    
    def studentPasswordChange(self, stuid, stupassword):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "UPDATE student SET stupassword = %s WHERE stuid = %s"
            cursor.execute(instruction, [stupassword, stuid])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL studentPasswordChange错误")
        self.closeDataBase(connection, cursor)
        return
    
    def teacherPasswordChange(self, teacherid, teacherpassword):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "UPDATE teacher SET teacherpassword = %s WHERE teacherid = %s"
            cursor.execute(instruction, [teacherpassword, teacherid])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL teacherPasswordChange错误")
        self.closeDataBase(connection, cursor)
        return
    
    def getCourseInfo(self, courseid):
        connection,cursor = self.connectDataBase()
        instruction = "SELECT c.id, c.name, c.credit, c.courseintro, c.materialname FROM (SELECT course.courseid, course.coursename,course.credit,course.courseintro,course_materials.material_name FROM course LEFT OUTER JOIN course_materials ON course.courseid = course_materials.courseid) AS c(id,name,credit,courseintro,materialname) WHERE c.id = %s"
        cursor.execute(instruction, [courseid])
        result = cursor.fetchone()
        self.closeDataBase(connection, cursor)
        return result

    def getClassInfo(self,classid):  #这时可以返回class avg mark
        connection,cursor = self.connectDataBase()
        instruction = "SELECT coursename,classid,teachername,class_time,classroom,class_hold,current_sel,class_material,avg_mark FROM class ,course, teacher WHERE class.classid = %s AND class.courseid = course.courseid AND class.teacherid = teacher.teacherid"
        cursor.execute(instruction, [classid])
        result = cursor.fetchone()
        self.closeDataBase(connection, cursor)
        return result
    
    def getCourseList(self):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT courseid, coursename, credit, courseintro FROM course ORDER BY courseid"
        cursor.execute(instruction)
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
    
    def getClassList(self):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT classid, coursename, teachername, class_time, classroom, class_hold, current_sel, class_material FROM class, course, teacher WHERE class.courseid = course.courseid AND class.teacherid = teacher.teacherid ORDER BY classid"
        cursor.execute(instruction)
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result

    def getClassByCourse(self, coursename):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT classid, coursename, teachername, class_time, classroom, class_hold, current_sel, class_material FROM class, course, teacher WHERE course.coursename = %s AND class.courseid = course.courseid AND class.teacherid = teacher.teacherid ORDER BY classid"
        cursor.execute(instruction, [coursename])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
    
    def getStudentClassList(self, stuid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT select_course.classid, coursename, teachername, class_time, classroom, class_material, grade FROM class, course, teacher, select_course WHERE select_course.stuid = %s AND select_course.classid = class.classid AND class.courseid = course.courseid AND class.teacherid = teacher.teacherid ORDER BY classid"
        cursor.execute(instruction, [stuid])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result

    def getTeacherClassList(self, teacherid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT classid, coursename, class_time, classroom, class_hold, current_sel, class_material, avg_mark FROM class, course WHERE class.teacherid = %s AND class.courseid = course.courseid ORDER BY classid"
        cursor.execute(instruction, [teacherid])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result


    def selectClass(self, stuid, classid):
        connection, cursor = self.connectDataBase()
        state = 0
        try:
            cursor.callproc('CheckSelCourseConflict',args=[stuid,classid,state])
            cursor.execute("SELECT @_CheckSelCourseConflict_2")
            state = cursor.fetchone()[0]
            if state == 0:
                connection.commit()
            else:
                print("执行存储过程CheckSelCourseConflict错误")
        except Exception as e:
            connection.rollback()
            print("执行MySQL selectClass错误")
        self.closeDataBase(connection, cursor)
        return state

    def createClass(self,classid,teacherid,courseid,class_time,classroom,classmaterial):
        connection, cursor = self.connectDataBase()
        state = 0
        try:
            cursor.callproc('CheckClassroomConflict',args=[class_time,classroom,classid,teacherid,courseid,classmaterial,state])
            cursor.execute("SELECT @_CheckClassroomConflict_6")
            state = cursor.fetchone()[0]
            if state == 0:
                connection.commit()
            else:
                print("执行存储过程CheckClassroomConflict错误")
        except Exception as e:
            connection.rollback()
            print("执行MySQL createClass错误")
        self.closeDataBase(connection, cursor)
        return state
    
    def createCourse(self,courseid,adminaccount,coursename,credit,courseintro):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "INSERT INTO course (courseid, admin_account, coursename, credit, courseintro) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(instruction, [courseid, adminaccount, coursename, credit, courseintro])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL createCourse错误")
        self.closeDataBase(connection, cursor)
        return
    
    def dropClass(self, stuid, classid):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "DELETE FROM select_course WHERE stuid = %s AND classid = %s"
            cursor.execute(instruction, [stuid, classid])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL dropClass错误")
        self.closeDataBase(connection, cursor)
        return
    
    def cancelClass(self, teacherid, coursename):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "DELETE FROM class WHERE class.teacherid = %s AND class.courseid IN (SELECT course.courseid FROM course WHERE course.coursename = %s)"
            cursor.execute(instruction, [teacherid, coursename])
            connection.commit()
        except Exception as e:  
            connection.rollback()
            print("执行MySQL cancelClass错误")
        self.closeDataBase(connection, cursor)
        return
    
    # 会级联删除课堂，评论，学习资料
    def deleteCourse(self, adminaccount, coursename):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "DELETE FROM course WHERE course.admin_account = %s AND course.coursename = %s"
            cursor.execute(instruction, [adminaccount, coursename])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL deleteCourse错误")
        self.closeDataBase(connection, cursor)
        return

    def modifyClass(self, class_id, class_time, class_room, class_material):
        connection, cursor = self.connectDataBase()
        state = 0
        try:
            cursor.callproc('CheckUpdateClassroomConflict',args=[class_time,class_room, class_id, class_material,state])
            cursor.execute("SELECT @_CheckUpdateClassroomConflict_4")
            state = cursor.fetchone()[0]
            if state == 0:
                connection.commit()
            else:
                print("执行存储过程CheckUpdateClassroomConflict错误")
        except Exception as e:
            connection.rollback()
            print("执行MySQL modifyClass错误")
        self.closeDataBase(connection, cursor)
        return

    def modifyCourse(self, course_id, course_name, course_credit, course_intro):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "UPDATE course SET coursename = %s, credit = %s, courseintro = %s WHERE courseid = %s"
            cursor.execute(instruction, [course_name, course_credit, course_intro, course_id])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL modifyCourse错误")
        self.closeDataBase(connection, cursor)
        return

    def convertToBinaryData(self, filename):
    # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def write_file(self, data, filename):
    # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def uploadMaterial(self, teacherid, material_name, coursename, material_path): #material_path为文件绝对路径
        connection, cursor = self.connectDataBase()
        courseid = ""
        state = 0
        try:
            print("Inserting LONGBLOB into course_material table")
            instruction = "SELECT courseid FROM course WHERE coursename = %s"
            cursor.execute(instruction, [coursename])
            courseid = cursor.fetchone()[0]
            material = self.convertToBinaryData(material_path)
            cursor.callproc('CheckMaterialDuplication',args=[teacherid,material_name,courseid,material,state])
            cursor.execute("SELECT @_CheckMaterialDuplication_4")
            state = cursor.fetchone()[0]
            if state == 0:
                connection.commit()
                print("Material inserted successfully as a LONGBLOB into course_materials table")
            else:
                print("Material already exists in course_materials table")
        except Exception as e:
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
            record = cursor.fetchone()[0]
            print("Storing material on disk \n")
            self.write_file(record, material_path)
        except Exception as e:
            connection.rollback()
            print("Failed reading LONGBLOB data from MySQL table {}".format(e))
        self.closeDataBase(connection, cursor)
        return

    def getTeacherMaterialList(self, teacherid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT materialid, material_name FROM course_materials WHERE teacherid = %s"
        cursor.execute(instruction, [teacherid])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result


    def deleteMaterial(self, material_id):  # 教师删除课程资料
        connection, cursor = self.connectDataBase()
        try:
            instruction = "DELETE FROM course_materials WHERE materialid = %s"
            cursor.execute(instruction, [material_id])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL deleteMaterial错误")
        self.closeDataBase(connection, cursor)
        return
    
    def getMaterialList(self):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT materialid, material_name FROM course_materials ORDER BY materialid"
        cursor.execute(instruction)
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
    
    def commentClass(self, classid, stuid, class_grade,comment):
        connection, cursor = self.connectDataBase() 
        try:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            instruction = "INSERT INTO comment VALUES(NULL,%s,%s,%s,%s,%s)"
            cursor.execute(instruction, [classid, stuid, class_grade, time, comment])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL commentClass错误")
        self.closeDataBase(connection, cursor)
        return
    
    def getCommentList(self, classid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT commentid, stuid, class_grade, comment_time, comment_content FROM comment WHERE classid = %s"
        cursor.execute(instruction, [classid])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
                                                    
    def getStudentCommentList(self, stuid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT commentid, classid, class_grade, comment_time, comment_content FROM comment WHERE stuid = %s"
        cursor.execute(instruction, [stuid])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
        
    def modifyComment(self, commentid, class_grade, comment):
        connection,cursor = self.connectDataBase()
        try:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            instruction = "UPDATE comment SET class_grade = %s, comment_time = %s, comment_content = %s WHERE commentid = %s"
            cursor.execute(instruction,[class_grade, time, comment, commentid])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL modifyComment错误")
        self.closeDataBase(connection, cursor)
        return
    
    def deleteComment(self, commentid):
        connection,cursor = self.connectDataBase()
        try:
            instruction = "DELETE FROM comment WHERE commentid = %s"
            cursor.execute(instruction,[commentid])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL deleteComment错误")
        self.closeDataBase(connection, cursor)
        return
    
    # 不使用视图
    # def studentPostMain(self, id, title, content):
    #     connection, cursor = self.connectDataBase()
    #     try:
    #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #         instruction = "INSERT INTO main_post VALUES (NULL, %s, NULL,NULL,%s, %s,%s,FALSE)"
    #         cursor.execute(instruction,[id,title,content,time])
    #         connection.commit()
    #     except Exception as e:
    #         connection.rollback()
    #         print("执行MySQL studentPostMain错误")
    #     self.closeDataBase(connection, cursor)
    #     return
    
    # 使用视图
    def studentPostMain(self, id, title, content):
        connection, cursor = self.connectDataBase()
        try:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            instruction = "INSERT INTO studentPostMain VALUES (NULL, %s,%s,%s,%s,FALSE)"
            cursor.execute(instruction,[id,title,content,time])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL studentPostMain错误")
        self.closeDataBase(connection, cursor)
        return
    
    def teacherPostMain(self, id, title, content):
        connection, cursor = self.connectDataBase()
        try:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            instruction = "INSERT INTO teacherPostMain VALUES (NULL, %s, %s, %s,%s,TRUE)"
            cursor.execute(instruction,[id,title,content,time])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL teacherPostMain错误")
        self.closeDataBase(connection, cursor)
        return
    
    def adminPostMain(self, id, title, content):
        connection, cursor = self.connectDataBase()
        try:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            instruction = "INSERT INTO adminPostMain VALUES (NULL, %s, %s, %s,%s,FALSE)"
            cursor.execute(instruction,[id,title,content,time])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL adminPostMain错误")
        self.closeDataBase(connection, cursor)
        return
    
    def getStudentMainPost(self, stuid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT postid, id, title, content, postime FROM studentPostMain WHERE id = %s"
        cursor.execute(instruction, [stuid])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
    
    def getTeacherMainPost(self, teacherid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT postid, id, title, content, postime FROM teacherPostMain WHERE id = %s"
        cursor.execute(instruction, [teacherid])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
    
    def getAdminMainPost(self, admin_account):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT postid, id, title, content, postime FROM adminPostMain WHERE id = %s"
        cursor.execute(instruction, [admin_account])
        result = cursor.fetchall()  
        self.closeDataBase(connection, cursor)
        return result
    
    def getMainPostList(self):
        connection, cursor = self.connectDataBase()
        result = ""
        try:
            instruction = "SELECT mainpostid, stuid, teacherid, admin_account, main_title, main_content, main_postime FROM main_post ORDER BY main_postime DESC"
            cursor.execute(instruction)
            result = cursor.fetchall()
        except Exception as e:
            connection.rollback()
            print("执行MySQL getMainPostList错误")
        self.closeDataBase(connection, cursor)
        return result
    
    def deleteMainPost(self, mainpostid):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "DELETE FROM main_post WHERE mainpostid = %s"
            cursor.execute(instruction, [mainpostid])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL deleteMainPost错误")
        self.closeDataBase(connection, cursor)
        return
    
    def studentPostFollow(self, stuid, mainpostid, follow_content):
        connection, cursor = self.connectDataBase()
        try:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            instruction = "INSERT INTO studentPostFollow VALUES (NULL, %s, %s ,%s, %s, FALSE)"
            cursor.execute(instruction,[stuid, mainpostid, follow_content, time])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL studentPostFollow错误")
        self.closeDataBase(connection, cursor)
        return
    
    def teacherPostFollow(self, teacherid, mainpostid, follow_content):
        connection, cursor = self.connectDataBase()
        try:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            instruction = "INSERT INTO teacherPostFollow VALUES (NULL, %s, %s, %s, %s, TRUE)"
            cursor.execute(instruction,[teacherid, mainpostid, follow_content, time])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL teacherPostFollow错误")
        self.closeDataBase(connection, cursor)
        return
    
    def adminPostFollow(self, admin_account, mainpostid, follow_content):
        connection, cursor = self.connectDataBase()
        try:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            instruction = "INSERT INTO adminPostFollow VALUES (NULL, %s, %s, %s, %s, FALSE)"
            cursor.execute(instruction,[admin_account, mainpostid, follow_content, time])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL adminPostFollow错误")
        self.closeDataBase(connection, cursor)
        return
    
    def getFollowByMain(self, mainpostid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT followpostid, stuid, teacherid, admin_account, follow_content, follow_postime FROM follow_post WHERE mainpostid = %s"
        cursor.execute(instruction, [mainpostid])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
    
    def getStudentFollowPosts(self, stuid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT postid, id, mainid, content, postime FROM studentPostFollow WHERE id = %s"
        cursor.execute(instruction, [stuid])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
    
    
    def getTeacherFollowPosts(self, teacherid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT postid, id, mainid, content, postime FROM teacherPostFollow WHERE id = %s"
        cursor.execute(instruction, [teacherid])
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result

    def deleteFollowPost(self, followpostid):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "DELETE FROM follow_post WHERE followpostid = %s"
            cursor.execute(instruction, [followpostid])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL deleteFollowPost错误")
        self.closeDataBase(connection, cursor)
        return
    
    def getStudentList(self):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT * FROM student"
        cursor.execute(instruction)
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
    
    def getTeacherList(self):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT * FROM teacher"
        cursor.execute(instruction)
        result = cursor.fetchall()
        self.closeDataBase(connection, cursor)
        return result
    
    def getClassRank(self, classid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT GetClass_Avgrank(%s)"
        cursor.execute(instruction, [classid])
        result = cursor.fetchone()[0]
        self.closeDataBase(connection, cursor)
        return result
    
    def getStudentGPA(self, stuid):
        connection, cursor = self.connectDataBase()
        instruction = "SELECT GetStu_gpa(%s)"
        cursor.execute(instruction, [stuid])
        result = cursor.fetchone()[0]
        self.closeDataBase(connection, cursor)
        return result
        
    def pushStudentGrade(self, stuid, classid, grade):
        connection, cursor = self.connectDataBase()
        try:
            instruction = "UPDATE select_course SET grade = %s WHERE select_course.stuid = %s AND select_course.classid = %s"
            cursor.execute(instruction, [grade, stuid, classid])
            connection.commit()
        except Exception as e:
            connection.rollback()
            print("执行MySQL pushStudentGrade错误")
        self.closeDataBase(connection, cursor)
        return
    
    