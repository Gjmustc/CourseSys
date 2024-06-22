<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'90px':'400px'">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <TeacherHeading></TeacherHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
          <h2>CourseSys</h2>
          <p>
            CourseSys是一个基于Django+Vue+MySQL框架开发的小型B/S应用，面向教师开放的功能主要有：
          </p>
          <ul>
            <li>介绍课程：介绍本学期开设的课程详情</li>
            <li>管理课堂：对不同课程可选择开设课堂或停止开课</li>
            <li>查看成绩: 查看开设课堂对应的学生成绩及平均成绩</li>
            <li>上传教材：根据上课需求上传资料到教材库中</li>
            <li>查看评价：在留言板的评价区查看学生评价及打分</li>
            <li>自由言论：在讨论区发帖跟帖自由讨论</li>
          </ul>

          <h2>导航指南</h2>
          <p>
            您可以通过左侧导航栏进行功能选择，点击对应的功能模块即可进入相应的管理页面。
          </p>
          <ul>
            <li>课程开设——查看学期课程信息</li>
            <li>课堂开设——查看学期课堂信息、选择开课或停课</li>
            <li>教材库——上传资料到资料库中</li>
            <li>讨论区——查看评课信息、自由讨论信息</li>
            <li>个人资料——管理个人信息</li>
          </ul>

          <h2>欢迎联系</h2>
          <p>如果您在使用过程中遇到问题，或者有任何建议，欢迎联系我们。</p>
          <el-link href="https://github.com/Gjmustc">Gjmustc</el-link>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from "./TeacherNav";
import TeacherHeading from "./TeacherHeading";
export default {
  name: "TeacherHead",
  components: { TeacherHeading, TeacherNav },
};
</script>

<style scoped>
@import "../../assets/css/back.css";
</style>
