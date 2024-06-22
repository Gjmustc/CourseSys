from django.urls import path
from . import views

# 项目页面分页布局
urlpatterns = [
    path('StudentRegister/', views.StudentRegister.as_view()),
    path('StudentLogin/', views.StudentLogin.as_view()),
    path('TeacherRegister/', views.TeacherRegister.as_view()),
    path('TeacherLogin/', views.TeacherLogin.as_view()),
    path('AdminLogin/', views.AdminLogin.as_view()),
    path('StudentChange/', views.StudentChange.as_view()),
    path('TeacherChange/', views.TeacherChange.as_view()),
    path('AdminChange/', views.AdminChange.as_view()),
    path('GetCourseList/', views.GetCourseList.as_view()),#获取全部课程列表(管理员可管理)
    path('GetClassList/', views.GetClassList.as_view()),#获取全部课堂列表
    path('GetClassByCourse/', views.GetClassByCourse.as_view()),#获取某课程的课堂列表
    path('GetStudentClassList/', views.GetStudentClassList.as_view()),#获取学生已选课堂列表
    path('GetTeacherClassList/', views.GetTeacherClassList.as_view()),#获取教师开设课堂列表
    path('SelectClass/', views.SelectClass.as_view()),#学生选课
    path('DropClass/', views.DropClass.as_view()),#学生退课 
    path('CreateClass/', views.CreateClass.as_view()),#教师开课
    path('CancelClass/', views.CancelClass.as_view()),#教师停课
    path('ModifyClass/', views.ModifyClass.as_view()),#教师修改课堂信息
    path('CreateCourse/', views.CreateCourse.as_view()),#管理员创建课程
    path('DeleteCourse/', views.DeleteCourse.as_view()),#管理员删除课程
    path('ModifyCourse/', views.ModifyCourse.as_view()),#管理员修改课程信息
    path('GetCourseInfo/', views.GetCourseInfo.as_view()),#获取课程信息
    path('GetClassInfo/', views.GetClassInfo.as_view()),#获取课堂信息
    path('UploadMaterial/', views.UploadMaterial.as_view()),#教师上传课程资料
    path('DeleteMaterial/', views.DeleteMaterial.as_view()),#教师删除课程资料
    path('DownloadMaterial/', views.DownloadMaterial.as_view()),#学生下载课程资料
    path('GetMaterialList/', views.GetMaterialList.as_view()),#获取课程资料列表
    path('GetTeacherMaterialList/', views.GetTeacherMaterialList.as_view()),#获取教师上传的课程资料列表
    path('CommentClass/', views.CommentClass.as_view()),#学生评价课堂
    path('GetCommentList/', views.GetCommentList.as_view()),#获取课堂评价列表
    path('DeleteComment/', views.DeleteComment.as_view()),#删除课堂评价
    path('ModifyComment/', views.ModifyComment.as_view()),#修改课堂评价
    path('PostMain/', views.PostMain.as_view()),#发布主贴
    path('DeleteMain/', views.DeleteMain.as_view()),#删除主贴
    path('GetMainList/', views.GetMainList.as_view()),#获取主贴列表
    path('PostFollow/', views.PostFollow.as_view()),#发布跟帖
    path('DeleteFollow/', views.DeleteFollow.as_view()),#删除跟帖
    path('GetFollowListByMain/', views.GetFollowListByMain.as_view()),#获取主贴下的跟帖列表
    path('GetStudentList/', views.GetStudentList.as_view()),#获取学生列表(管理员可管理)
    path('GetTeacherList/', views.GetTeacherList.as_view()),#获取教师列表(管理员可管理)
    # path('GetClassRank/', views.GetClassRank.as_view()),#获取课堂评分
    path('PushStudentGrade/', views.PushStudentGrade.as_view()),#推送学生成绩(教师可管理)
    path('GetStudentGPA/', views.GetStudentGPA.as_view()),#获取学生GPA
    path('GetStudentComments/', views.GetStudentComments.as_view()),#获取特定学生所有评价
    path('GetStudentMainPosts/', views.GetStudentMainPosts.as_view()),#获取特定学生所有主贴
    path('GetTeacherMainPosts/', views.GetTeacherMainPosts.as_view()),#获取特定教师所有主贴
    path('GetAdminMainPosts/', views.GetAdminMainPosts.as_view()),#获取特定管理员所有主贴
    path('GetStudentFollowPosts/', views.GetStudentFollowPosts.as_view()),#获取特定学生所有跟帖
    path('GetTeacherFollowPosts/', views.GetTeacherFollowPosts.as_view()),#获取特定教师所有跟帖
]
