import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import AdminLogin from '../components/Admin/AdminLogin'
import AdminHead from '../components/Admin/AdminHead'
import AdminChange from '../components/Admin/AdminChange'
import AdminClassTable from '../components/Admin/ClassTable/AdminClassTable'
import AdminCourseTable from '../components/Admin/CourseTable/AdminCourseTable'
import AdminMaterialTable from '../components/Admin/MaterialTable/AdminMaterialTable'
import StudentTable from '../components/Admin/StudentTable/StudentTable'
import TeacherTable from '../components/Admin/TeacherTable/TeacherTable'
import AdminCommentAndDiscussNav from '../components/Admin/Talk/AdminCommentAndDiscussNav'
import AdminComment from '../components/Admin/Talk/AdminComment'
import AdminCommentTable from '../components/Admin/Talk/AdminCommentTable'
import AdminDiscuss from '../components/Admin/Talk/AdminDiscuss'
import AdminDiscussTable from '../components/Admin/Talk/AdminDiscussTable'

import StudentLogin from '../components/Student/StudentLogin'
import StudentRegister from '../components/Student/StudentRegister'
import StudentHead from '../components/Student/StudentHead'
import StudentChange from '../components/Student/StudentChange'
import SelectClass from '../components/Student/ClassTable/SelectClass'
import SelectedClass from '../components/Student/ClassTable/SelectedClass'
import StudentClass from '../components/Student/ClassTable/StudentClass'
import StudentCourseTable from '../components/Student/CourseTable/StudentCourseTable'
import StudentMaterialTable from '../components/Student/MaterialTable/StudentMaterialTable'
import StudentAllComment from '../components/Student/Talk/StudentAllComment'
import StudentAllFollowPost from '../components/Student/Talk/StudentAllFollowPost'
import StudentAllMainPost from '../components/Student/Talk/StudentAllMainPost'
import StudentComment from '../components/Student/Talk/StudentComment'
import StudentDiscuss from '../components/Student/Talk/StudentDiscuss'
import StudentCommentAndDiscussNav from '../components/Student/Talk/StudentCommentAndDiscussNav'
import StudentCommentTable from '../components/Student/Talk/StudentCommentTable'
import StudentDiscussTable from '../components/Student/Talk/StudentDiscussTable'

import TeacherLogin from '../components/Teacher/TeacherLogin'
import TeacherHead from '../components/Teacher/TeacherHead'
import TeacherRegister from '../components/Teacher/TeacherRegister'
import TeacherChange from '../components/Teacher/TeacherChange'
import TeacherClass from '../components/Teacher/ClassTable/TeacherClass'
import CreatedClass from '../components/Teacher/ClassTable/CreatedClass'
import TeacherClassTable from '../components/Teacher/ClassTable/TeacherClassTable'
import PushStudentGrade from '../components/Teacher/ClassTable/PushStudentGrade'
import TeacherCourseTable from '../components/Teacher/CourseTable/TeacherCourseTable'
import TeacherMaterial from '../components/Teacher/MaterialTable/TeacherMaterial'
import TeacherMaterialTable from '../components/Teacher/MaterialTable/TeacherMaterialTable'
import MyMaterialList from '../components/Teacher/MaterialTable/MyMaterialList'
import TeacherAllFollowPost from '../components/Teacher/Talk/TeacherAllFollowPost'
import TeacherAllMainPost from '../components/Teacher/Talk/TeacherAllMainPost'
import TeacherComment from '../components/Teacher/Talk/TeacherComment'
import TeacherDiscuss from '../components/Teacher/Talk/TeacherDiscuss'
import TeacherCommentAndDiscussNav from '../components/Teacher/Talk/TeacherCommentAndDiscussNav'
import TeacherCommentTable from '../components/Teacher/Talk/TeacherCommentTable'
import TeacherDiscussTable from '../components/Teacher/Talk/TeacherDiscussTable'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/',
      name:'HelloWorld',
      component:HelloWorld
    },
    {
      path:'/AdminLogin',
      name:'AdminLogin',
      component:AdminLogin
    },
    {
      path:'/AdminHead',
      name:'AdminHead',
      component:AdminHead
    },
    {
      path:'/AdminChange',
      name:'AdminChange',
      component:AdminChange
    },
    {
      path: '/AdminClassTable',
      name: 'AdminClassTable',
      component: AdminClassTable,
      children: [
        {
          path: 'AdminClassTable',
          name: 'AdminClassTable',
          component: AdminClassTable
        }
      ]
    },
    {
      path:'/AdminCourseTable',
      name:'AdminCourseTable',
      component:AdminCourseTable,
      children: [
        {
          path: 'AdminCourseTable',
          name: 'AdminCourseTable',
          component: AdminCourseTable
        }
      ]
    },
    {
      path:'/AdminMaterialTable',
      name:'AdminMaterialTable',
      component:AdminMaterialTable,
      children: [
        {
          path: 'AdminMaterialTable',
          name: 'AdminMaterialTable',
          component: AdminMaterialTable
        }
      ]
    },
    {
      path:'/StudentTable',
      name:'StudentTable',
      component:StudentTable,
      children: [
        {
          path: 'StudentTable',
          name: 'StudentTable',
          component: StudentTable
        }
      ]
    },
    {
      path:'/TeacherTable',
      name:'TeacherTable',
      component:TeacherTable,
      children: [
        {
          path: 'TeacherTable',
          name: 'TeacherTable',
          component: TeacherTable
        }
      ]
    },
    {
      path:'/AdminCommentAndDiscussNav',
      name:'AdminCommentAndDiscussNav',
      component:AdminCommentAndDiscussNav,
      children: [
        {
          path: 'AdminComment',
          name: 'AdminComment',
          component: AdminComment
        },
        {
          path: 'AdminCommentTable',
          name: 'AdminCommentTable',
          component: AdminCommentTable
        },
        {
          path: 'AdminDiscuss',
          name: 'AdminDiscuss',
          component: AdminDiscuss
        },
        {
          path: 'AdminDiscussTable',
          name: 'AdminDiscussTable',
          component: AdminDiscussTable
        }
      ]
    },
    {
      path:'/StudentLogin',
      name:'StudentLogin',
      component:StudentLogin
    },
    {
      path:'/StudentRegister',
      name:'StudentRegister',
      component:StudentRegister
    },
    {
      path:'/StudentHead',
      name:'StudentHead',
      component:StudentHead
    },
    {
      path:'/StudentChange',
      name:'StudentChange',
      component:StudentChange
    },
    {
      path:'/StudentClass',
      name:'StudentClass',
      component:StudentClass,
      children: [
        {
          path: 'SelectClass',
          name: 'SelectClass',
          component: SelectClass
        },
        {
          path: 'SelectedClass',
          name: 'SelectedClass',
          component: SelectedClass
        }
      ]
    },
    {
      path:'/StudentCourseTable',
      name:'StudentCourseTable',
      component:StudentCourseTable,
      children: [
        {
          path: 'StudentCourseTable',
          name: 'StudentCourseTable',
          component: StudentCourseTable
        }
      ]
    },
    {
      path:'/StudentMaterialTable',
      name:'StudentMaterialTable',
      component:StudentMaterialTable,
      children: [
        {
          path: 'StudentMaterialTable',
          name: 'StudentMaterialTable',
          component: StudentMaterialTable
        }
      ]
    },
    {
      path: '/StudentAllComment',
      name: 'StudentAllComment',
      component: StudentAllComment,
      children:[
        {
          path: 'StudentAllComment',
          name: 'StudentAllComment',
          component: StudentAllComment
        }
      ]
    },
    {
      path:'/StudentCommentAndDiscussNav',
      name:'StudentCommentAndDiscussNav',
      component:StudentCommentAndDiscussNav,
      children: [
        {
          path: 'StudentAllFollowPost',
          name: 'StudentAllFollowPost',
          component: StudentAllFollowPost
        },
        {
          path: 'StudentAllMainPost',
          name: 'StudentAllMainPost',
          component: StudentAllMainPost
        },
        {
          path: 'StudentComment',
          name: 'StudentComment',
          component: StudentComment
        },
        {
          path: 'StudentDiscuss',
          name: 'StudentDiscuss',
          component: StudentDiscuss
        },
        {
          path: 'StudentCommentTable',
          name: 'StudentCommentTable',
          component: StudentCommentTable
        },
        {
          path: 'StudentDiscussTable',
          name: 'StudentDiscussTable',
          component: StudentDiscussTable
        }
      ]
    },
    {
      path:'/TeacherLogin',
      name:'TeacherLogin',
      component:TeacherLogin
    },
    {
      path:'/TeacherRegister',
      name:'TeacherRegister',
      component:TeacherRegister
    },
    {
      path:'/TeacherHead',
      name:'TeacherHead',
      component:TeacherHead
    },
    {
      path:'/TeacherChange',
      name:'TeacherChange',
      component:TeacherChange
    },
    {
      path:'/TeacherClass',
      name:'TeacherClass',
      component:TeacherClass,
      children: [
        {
          path: 'CreatedClass',
          name: 'CreatedClass',
          component: CreatedClass
        },
        {
          path: 'TeacherClassTable',
          name: 'TeacherClassTable',
          component: TeacherClassTable
        },
        {
          path: 'PushStudentGrade',
          name: 'PushStudentGrade',
          component: PushStudentGrade
        }
      ]
    },
    {
      path:'/TeacherCourseTable',
      name:'TeacherCourseTable',
      component:TeacherCourseTable,
      children:[
        {
          path: 'TeacherCourseTable',
          name: 'TeacherCourseTable',
          component: TeacherCourseTable
        }
      ]
    },
    {
      path:'/TeacherMaterial',
      name:'TeacherMaterial',
      component:TeacherMaterial,
      children: [
        {
          path: 'TeacherMaterialTable',
          name: 'TeacherMaterialTable',
          component: TeacherMaterialTable
        },
        {
          path: 'MyMaterialList',
          name: 'MyMaterialList',
          component: MyMaterialList
        }
      ]
    },
    {
      path:'/TeacherCommentAndDiscussNav',
      name:'TeacherCommentAndDiscussNav',
      component:TeacherCommentAndDiscussNav,
      children: [
        {
          path: 'TeacherAllFollowPost',
          name: 'TeacherAllFollowPost',
          component: TeacherAllFollowPost
        },
        {
          path: 'TeacherAllMainPost',
          name: 'TeacherAllMainPost',
          component: TeacherAllMainPost
        },
        {
          path: 'TeacherComment',
          name: 'TeacherComment',
          component: TeacherComment
        },
        {
          path: 'TeacherDiscuss',
          name: 'TeacherDiscuss',
          component: TeacherDiscuss
        },
        {
          path: 'TeacherCommentTable',
          name: 'TeacherCommentTable',
          component: TeacherCommentTable
        },
        {
          path: 'TeacherDiscussTable',
          name: 'TeacherDiscussTable',
          component: TeacherDiscussTable
        }
      ]
    }
  ]
})

