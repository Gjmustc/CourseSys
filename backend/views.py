# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .base_mysql import MySQL
import json
import re
# Create your views here.

class StudentRegister(APIView):
    def get(self, request):
        userid = str(request.GET.get('useraccount', None))
        username = str(request.GET.get('username', None))
        password = str(request.GET.get('password', None))
        password_confirm = str(request.GET.get('password_confirm', None))
        major = str(request.GET.get('major', None))
        enrollyear = str(request.GET.get('enrollyear', None))
        useremail = str(request.GET.get('useremail', None))
        if password != password_confirm:
            return Response({"status": "fail", "message": "password not match"})
        sql = MySQL()
        result = sql.findStudent(userid)
        flag = not not result
        if flag:
            return Response({"status": "fail", "message": "user already exists"})
        sql.registerStudent(userid, username, password, major, enrollyear, useremail)
        return Response({"status": "success", "message": "register success"})

class StudentLogin(APIView):
    def get(self,request):
        userid = str(request.GET.get('useraccount', None))
        password = str(request.GET.get('password', None))
        sql = MySQL()
        result = sql.findStudent(userid)
        flag = not not result
        if not flag:
            return Response({"status": "fail", "message": "user not exists"})
        if result[2] != password:
            return Response({"status": "fail", "message": "password error"})
        return Response({"status": "success", "message": "login success"})

class TeacherRegister(APIView):
    def get(self, request):
        userid = str(request.GET.get('useraccount', None))
        username = str(request.GET.get('username', None))
        password = str(request.GET.get('password', None))
        password_confirm = str(request.GET.get('password_confirm', None))
        useremail = str(request.GET.get('useremail', None))
        if password != password_confirm:
            return Response({"status": "fail", "message": "password not match"})
        sql = MySQL()
        result = sql.findTeacher(userid)
        flag = not not result
        if flag:
            return Response({"status": "fail", "message": "user already exists"})
        sql.registerTeacher(userid, username, password, useremail)
        return Response({"status": "success", "message": "register success"})

class TeacherLogin(APIView):
    def get(self,request):
        userid = str(request.GET.get('useraccount', None))
        password = str(request.GET.get('password', None))
        sql = MySQL()
        result = sql.findTeacher(userid)
        flag = not not result
        if not flag:
            return Response({"status": "fail", "message": "user not exists"})
        if result[2] != password:
            return Response({"status": "fail", "message": "password error"})
        return Response({"status": "success", "message": "login success"})

class AdminLogin(APIView):
    def get(self,request):
        adminaccount = str(request.GET.get('adminaccount', None))
        password = str(request.GET.get('password', None))
        sql = MySQL()
        result = sql.findAdmin(adminaccount)
        flag = not not result
        if not flag:
            return Response({"status": "fail", "message": "admin not exists"})
        if result[1] != password:
            return Response({"status": "fail", "message": "password error"})
        return Response({"status": "success", "message": "login success"})

class StudentChange(APIView):
    def get(self, request):
        userid = str(request.GET.get('useraccount', None))
        oldpassword = str(request.GET.get('oldpassword', None))
        newpassword = str(request.GET.get('newpassword', None))
        newpassword_confirm = str(request.GET.get('newpassword_confirm', None))
        sql = MySQL()
        result = sql.findStudent(userid)
        flag = not not result
        if not flag:
            return Response({"status": "fail", "message": "user not exists"})
        if result[2] != oldpassword:
            return Response({"status": "fail", "message": "password error"})
        if newpassword != newpassword_confirm:
            return Response({"status": "fail", "message": "password not match"})
        sql.studentPasswordChange(userid, newpassword)
        return Response({"status": "success", "message": "change success"})

class TeacherChange(APIView):
    def get(self, request):
        userid = str(request.GET.get('useraccount', None))
        oldpassword = str(request.GET.get('oldpassword', None))
        newpassword = str(request.GET.get('newpassword', None))
        newpassword_confirm = str(request.GET.get('newpassword_confirm', None))
        sql = MySQL()
        result = sql.findTeacher(userid)
        flag = not not result
        if not flag:
            return Response({"status": "fail", "message": "user not exists"})
        if result[2] != oldpassword:
            return Response({"status": "fail", "message": "password error"})
        if newpassword != newpassword_confirm:
            return Response({"status": "fail", "message": "password not match"})
        sql.teacherPasswordChange(userid, newpassword)
        return Response({"status": "success", "message": "change success"})

class AdminChange(APIView):
    def get(self,request):
        adminaccount = str(request.GET.get('adminaccount', None))
        oldpassword = str(request.GET.get('oldpassword', None))
        newpassword = str(request.GET.get('newpassword', None))
        newpassword_confirm = str(request.GET.get('newpassword_confirm', None))
        sql = MySQL()
        result = sql.findAdmin(adminaccount)
        flag = not not result
        if not flag:
            return Response({"status": "fail", "message": "admin not exists"})
        if result[1] != oldpassword:
            return Response({"status": "fail", "message": "password error"})
        if newpassword != newpassword_confirm:
            return Response({"status": "fail", "message": "password not match"})
        sql.adminPasswordChange(adminaccount, newpassword)
        return Response({"status": "success", "message": "change success"})

class GetCourseList(APIView):
    def get(self,request):
        sql = MySQL()
        result = sql.getCourseList()
        courselist = [] #字典列表
        for item in result:
            course = {
                "courseid": item[0],
                "coursename": item[1],
                "coursecredit": item[2],
                "coursedescription": item[3] if item[3] is not None else "",
            }
            courselist.append(course)
        return Response(courselist)

class GetClassList(APIView):
    def get(self,request):
        sql = MySQL()
        result = sql.getClassList()
        classlist = []
        for item in result:
            rank = sql.getClassRank(item[0])
            classroom = {
                "classid": item[0],
                "coursename": item[1],
                "teachername": item[2],
                "classtime": item[3],
                "classroom": item[4],
                "classhold": item[5],
                "currentselect":item[6],
                "recommendmaterial": item[7] if item[7] is not None else "",
                "classrank": rank if rank is not None else 0,
            }
            classlist.append(classroom)
        return Response(classlist)

class GetClassByCourse(APIView):
    def get(self,request):
        coursename = str(request.GET.get('coursename', None))
        sql = MySQL()
        result = sql.getClassByCourse(coursename)
        classlist = []  
        for item in result:
            classroom = {
                "classid": item[0],
                "coursename": item[1],
                "teachername": item[2],
                "classtime": item[3],
                "classroom": item[4],
                "classhold": item[5],
                "currentselect":item[6],
                "recommendmaterial": item[7] if item[7] is not None else "",
            }
            classlist.append(classroom)
        return Response(classlist)
    
class GetStudentClassList(APIView):
    def get(self,request):
        stuid = str(request.GET.get('studentid', None))
        sql = MySQL()
        result = sql.getStudentClassList(stuid)
        classlist = []
        for item in result:
            classroom = {
                "classid": item[0],
                "coursename": item[1],
                "teachername": item[2],
                "classtime": item[3],
                "classroom": item[4],
                "recommendmaterial": item[5] if item[5] is not None else "",
                "grade":item[6] if item[6] is not None else 0,
            }
            classlist.append(classroom)
        return Response(classlist)

class GetTeacherClassList(APIView):
    def get(self,request):
        teacherid = str(request.GET.get('teacherid', None))
        sql = MySQL()
        result = sql.getTeacherClassList(teacherid)
        classlist = []
        for item in result:
            classroom = {
                "classid": item[0],
                "coursename": item[1],
                "classtime": item[2],
                "classroom": item[3],
                "classhold": item[4],
                "currentselect":item[5],
                "recommendmaterial": item[6] if item[6] is not None else "",
                "avg_mark" : item[7],
            }
            classlist.append(classroom)
        return Response(classlist)

class SelectClass(APIView):
    def get(self,request):
        stuid = str(request.GET.get('studentid', None))
        classid = str(request.GET.get('classid', None))
        sql = MySQL()
        result = sql.selectClass(stuid, classid)
        if result == 0 :
            return Response({"status":"success","message":"select class success"})
        elif result == 2:
            return Response({"status":"fail","message":"class already selected"})
        elif result == 3:
            return Response({"status":"fail","message":"class is full"})
        elif result == 4:
            return Response({"status":"fail","message":"time conflict"})

class DropClass(APIView):
    def get(self,request):
        stuid = str(request.GET.get('studentid', None))
        classid = str(request.GET.get('classid', None))
        sql = MySQL()
        sql.dropClass(stuid, classid)
        return Response({"status":"success","message":"drop class success"})      

class CreateClass(APIView):
    def get(self,request):
        classid = str(request.GET.get('classid', None))
        teacherid = str(request.GET.get('teacherid', None))
        courseid = str(request.GET.get('courseid', None))
        classtime = str(request.GET.get('classtime', None))
        classroom = str(request.GET.get('classroom', None))
        recommendmaterial = str(request.GET.get('recommendmaterial', None))
        sql = MySQL()
        result = sql.createClass(classid, teacherid, courseid, classtime, classroom, recommendmaterial)
        if result == 0:
            return Response({"status":"success","message":"create class success"})
        elif result == 2:
            return Response({"status":"fail","message":"classroom conflict"})

class CancelClass(APIView):
    def get(self,request):
        teacherid = str(request.GET.get('teacherid', None))
        coursename = str(request.GET.get('coursename', None))
        sql = MySQL()
        sql.cancelClass(teacherid, coursename)
        return Response({"status":"success","message":"cancel class success"})

class ModifyClass(APIView):
    def get(self,request):
        classid = str(request.GET.get('classid', None))
        classtime = str(request.GET.get('classtime', None))
        classroom = str(request.GET.get('classroom', None))
        recommendmaterial = str(request.GET.get('recommendmaterial', None))
        sql = MySQL()
        result = sql.modifyClass(classid, classtime, classroom, recommendmaterial)
        if result == 0:
            return Response({"status":"success","message":"modify class success"})
        elif result == 2:
            return Response({"status":"fail","message":"classroom conflict"})
        

class CreateCourse(APIView):
    def get(self,request):
        courseid = str(request.GET.get('courseid', None))
        adminaccount = str(request.GET.get('adminaccount', None))
        coursename = str(request.GET.get('coursename', None))
        coursecredit = str(request.GET.get('coursecredit', None))
        coursedescription = str(request.GET.get('coursedescription', None))
        coursedescription = re.sub(r'<[^<>]+>', '',coursedescription)
        coursedescription = re.sub(r'&nbsp;', '', coursedescription, flags=re.IGNORECASE)
        print(courseid, adminaccount, coursename, coursecredit, coursedescription)
        sql = MySQL()
        sql.createCourse(courseid, adminaccount, coursename, coursecredit, coursedescription)
        return Response({"status":"success","message":"create course success"})
    
class DeleteCourse(APIView):
    def get(self,request):
        adminaccount = str(request.GET.get('adminaccount', None))
        coursename = str(request.GET.get('coursename', None))
        sql = MySQL()
        sql.deleteCourse(adminaccount, coursename)
        return Response({"status":"success","message":"delete course success"})
    
class ModifyCourse(APIView):
    def get(self,request):
        courseid = str(request.GET.get('courseid', None))
        coursename = str(request.GET.get('coursename', None))
        coursecredit = str(request.GET.get('coursecredit', None))
        coursedescription = str(request.GET.get('coursedescription', None))
        sql = MySQL()
        sql.modifyCourse(courseid, coursename, coursecredit, coursedescription)
        return Response({"status":"success","message":"modify course success"})

class GetCourseInfo(APIView):
    def get(self,request):
        courseid = str(request.GET.get('courseid', None))
        sql = MySQL()
        result = sql.getCourseInfo(courseid)
        materiallist = []
        for i in result:
            materiallist.append(i[4] if i[4] is not None else "")
        course = {
            "courseid": result[0][0],
            "coursename": result[0][1],
            "coursecredit": result[0][2],
            "coursedescription": result[0][3] if result[0][3] is not None else "",
            "materiallist": materiallist,
        }
        return Response(course)

class GetClassInfo(APIView):
    def get(self, request):
        classid = str(request.GET.get('classid', None))
        sql = MySQL()
        result = sql.getClassInfo(classid)
        classroom = {
            "coursename": result[0],
            "classid": result[1],
            "teachername": result[2],
            "classtime": result[3],
            "classroom": result[4],
            "classhold": result[5],
            "currentselect": result[6],
            "recommendmaterial": result[7] if result[7] is not None else "",
            "avg_mark" : result[8],
        }
        return Response(classroom)

class UploadMaterial(APIView):
    def get(self,request):
        teacherid = str(request.GET.get('teacherid', None))
        materialname = str(request.GET.get('materialname', None))
        coursename = str(request.GET.get('coursename', None))
        materialpath = str(request.GET.get('materialpath', None)) #绝对路径
        sql = MySQL()
        result = sql.uploadMaterial(teacherid, materialname, coursename, materialpath)
        if result == 0:
            return Response({"status":"success","message":"upload material success"})
        elif result == 2:
            return Response({"status":"fail","message":"material already exists"})

class DeleteMaterial(APIView):
    def get(self,request):
        materialid = str(request.GET.get('materialid', None))
        sql = MySQL()
        sql.deleteMaterial(materialid)
        return Response({"status":"success","message":"delete material success"})

class DownloadMaterial(APIView):
    def get(self,request):
        materialid = str(request.GET.get('materialid', None))
        materialpath = str(request.GET.get('materialpath', None))
        sql = MySQL()
        print(materialid, materialpath)
        sql.downloadMaterial(materialid, materialpath)
        return Response({"status":"success","message":"download material success"})

class GetMaterialList(APIView):
    def get(self,request):
        sql = MySQL()
        result = sql.getMaterialList()
        materiallist = []
        for item in result:
            material = {
                "materialid": item[0],
                "materialname": item[1],
            }
            materiallist.append(material)
        return Response(materiallist)
    
class GetTeacherMaterialList(APIView):
    def get(self,request):
        teacherid = str(request.GET.get('teacherid', None))
        sql = MySQL()
        result = sql.getTeacherMaterialList(teacherid)
        materiallist = []
        for item in result:
            material = {
                "materialid": item[0],
                "materialname": item[1],
            }
            materiallist.append(material)
        return Response(materiallist)
    
class CommentClass(APIView):
    def get(self,request):
        stuid = str(request.GET.get('studentid', None))
        classid = str(request.GET.get('classid', None))
        class_rank = str(request.GET.get('class_rank', None))
        comment = str(request.GET.get('comment', None))
        sql = MySQL()
        sql.commentClass(classid, stuid, class_rank, comment)
        return Response({"status":"success","message":"comment success"})


class GetCommentList(APIView):
    def get(self,request):
        classid = str(request.GET.get('classid', None))
        sql = MySQL()
        result = sql.getCommentList(classid)
        commentlist = []
        for item in result:
            comment = {
                "commentid": item[0],
                "studentid": item[1],
                "classrank": item[2],
                "commenttime": item[3],
                "comment": item[4],
            }
            commentlist.append(comment)
        return Response(commentlist)

class DeleteComment(APIView):
    def get(self,request):
        commentid = str(request.GET.get('commentid', None))
        sql = MySQL()
        sql.deleteComment(commentid)
        return Response({"status":"success","message":"delete comment success"})


class ModifyComment(APIView):
    def get(self,request):
        commentid = str(request.GET.get('commentid', None))
        classrank = str(request.GET.get('classrank', None))
        comment = str(request.GET.get('comment', None))
        sql = MySQL()
        sql.modifyComment(commentid, classrank, comment)
        return Response({"status":"success","message":"modify comment success"})

class PostMain(APIView):
    def get(self,request):
        userid = str(request.GET.get('userid', None))
        title = str(request.GET.get('title', None))
        content = str(request.GET.get('content', None))
        sql = MySQL()
        flag = 0
        find = not not sql.findAdmin(userid)
        if find:
            flag = 1
        find = not not sql.findTeacher(userid)
        if find:
            flag = 2
        find = not not sql.findStudent(userid)
        if find:
            flag = 3
        match flag:
            case 1:
                sql.adminPostMain(userid, title, content)
            case 2:
                sql.teacherPostMain(userid, title, content)
            case 3:
                sql.studentPostMain(userid, title, content)
        return Response({"status":"success","message":"post main success"})

class DeleteMain(APIView):
    def get(self,request):
        mainid = str(request.GET.get('mainid', None))
        sql = MySQL()
        sql.deleteMainPost(mainid)
        return Response({"status":"success","message":"delete main success"})

class GetMainList(APIView):
    def get(self,request):
        sql = MySQL()
        result = sql.getMainPostList()
        mainlist = []
        for item in result:
            main = {
                "mainid": item[0],
                "userid": item[1] if item[1] is not None else item[2] if item[2] is not None else item[3],
                "title": item[4],
                "content": item[5],
                "posttime": item[6],
            }
            mainlist.append(main)
        return Response(mainlist)

class PostFollow(APIView):
    def get(self,request):
        userid = str(request.GET.get('userid', None))
        mainid = str(request.GET.get('mainid', None))
        content = str(request.GET.get('content', None))
        sql = MySQL()
        flag = 0
        find = not not sql.findAdmin(userid)
        if find:
            flag = 1
        find = not not sql.findTeacher(userid)
        if find:
            flag = 2
        find = not not sql.findStudent(userid)
        if find:
            flag = 3
        match flag:
            case 1:
                sql.adminPostFollow(userid, mainid, content)
            case 2:
                sql.teacherPostFollow(userid, mainid, content)
            case 3:
                sql.studentPostFollow(userid, mainid, content)
        return Response({"status":"success","message":"post follow success"})

class DeleteFollow(APIView):
    def get(self,request):
        followid = str(request.GET.get('followid', None))
        sql = MySQL()
        sql.deleteFollowPost(followid)
        return Response({"status":"success","message":"delete follow success"})

class GetFollowListByMain(APIView):
    def get(self,request):
        mainid = str(request.GET.get('mainid', None))
        sql = MySQL()
        result = sql.getFollowByMain(mainid)
        followlist = []
        for item in result:
            follow = {
                "followid": item[0],
                "userid": item[1] if item[1] is not None else item[2] if item[2] is not None else item[3],
                "content": item[4],
                "posttime": item[5],
            }
            followlist.append(follow)
        return Response(followlist)

class GetStudentList(APIView):
    def get(self,request):
        sql = MySQL()
        result = sql.getStudentList()
        studentlist = []
        for item in result:
            student = {
                "studentid": item[0],
                "studentname": item[1],
                "studentpassword": item[2],
                "major": item[3],
                "enrollyear": item[4],
                "useremail": item[5],
            }
            studentlist.append(student)
        return Response(studentlist)

class GetTeacherList(APIView):
    def get(self,request):
        sql = MySQL()
        result = sql.getTeacherList()
        teacherlist = []
        for item in result:
            teacher = {
                "teacherid": item[0],
                "teachername": item[1],
                "teacherpassword": item[2],
                "useremail": item[3],
            }
            teacherlist.append(teacher)
        return Response(teacherlist)

class PushStudentGrade(APIView):
    def get(self,request):
        studentid = str(request.GET.get('studentid', None))
        classid = str(request.GET.get('classid', None))
        grade = str(request.GET.get('grade', None))
        sql = MySQL()
        sql.pushStudentGrade(studentid, classid, grade)
        return Response({"status":"success","message":"push grade success"})

class GetStudentComments(APIView):
    def get(self,request):
        studentid = str(request.GET.get('studentid', None))
        sql = MySQL()
        result = sql.getStudentCommentList(studentid)
        commentlist = []
        for item in result:
            comment = {
                "commentid": item[0],
                "classid": item[1],
                "classrank": item[2],
                "commenttime": item[3],
                "comment": item[4],
            }
            commentlist.append(comment)
        return Response(commentlist)


class GetStudentMainPosts(APIView):
    def get(self,request):
        studentid = str(request.GET.get('studentid', None))
        sql = MySQL()
        result = sql.getStudentMainPost(studentid)
        mainlist = []
        for item in result:
            main = {
                "mainid": item[0],
                "userid": item[1],
                "title": item[2],
                "content": item[3],
                "posttime": item[4],
            }
            mainlist.append(main)
        return Response(mainlist)

class GetTeacherMainPosts(APIView):
    def get(self,request):
        teacherid = str(request.GET.get('teacherid', None))
        sql = MySQL()
        result = sql.getTeacherMainPost(teacherid)
        mainlist = []
        for item in result:
            main = {
                "mainid": item[0],
                "userid": item[1],
                "title": item[2],
                "content": item[3],
                "posttime": item[4],
            }
            mainlist.append(main)
        return Response(mainlist)

class GetAdminMainPosts(APIView):
    def get(self,request):
        adminaccount = str(request.GET.get('adminaccount', None))
        sql = MySQL()
        result = sql.getAdminMainPost(adminaccount)
        mainlist = []
        for item in result:
            main = {
                "mainid": item[0],
                "userid": item[1],
                "title": item[2],
                "content": item[3],
                "posttime": item[4],
            }
            mainlist.append(main)
        return Response(mainlist)

class GetStudentFollowPosts(APIView):
    def get(self,request):
        studentid = str(request.GET.get('studentid', None))
        sql = MySQL()
        result = sql.getStudentFollowPosts(studentid)
        followlist = []
        for item in result:
            follow = {
                "followid": item[0],
                "userid": item[1],
                "mainid": item[2],
                "content": item[3],
                "posttime": item[4],
            }
            followlist.append(follow)
        return Response(followlist)

class GetTeacherFollowPosts(APIView):
    def get(self,request):
        teacherid = str(request.GET.get('teacherid', None))
        sql = MySQL()
        result = sql.getTeacherFollowPosts(teacherid)
        followlist = []
        for item in result:
            follow = {
                "followid": item[0],
                "userid": item[1],
                "mainid": item[2],
                "content": item[3],
                "posttime": item[4],
            }
            followlist.append(follow)
        return Response(followlist)

class GetStudentGPA(APIView):
    def get(self,request):
        studentid = str(request.GET.get('studentid', None))
        sql = MySQL()
        result = sql.getStudentGPA(studentid)
        return Response(result)