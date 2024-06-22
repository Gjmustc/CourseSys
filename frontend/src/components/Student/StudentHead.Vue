<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'90px':'400px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
          <div v-bind:style="{ fontSize: '20px', float: left }">
            <h2>CourseSys</h2>
            <p>
              CourseSys是一个基于Django+Vue+MySQL框架开发的小型B/S应用，面向学生开放的功能主要有：
            </p>
            <ul>
              <li>介绍课程：介绍本学期开设的课程详情</li>
              <li>选择课堂：对不同课程开设的多个课堂选择其中之一</li>
              <li>查看成绩: 查看已选课堂对应成绩及平均GPA</li>
              <li>下载教材：根据上课需求下载教材库中的资料</li>
              <li>评价课堂：在讨论区评价课堂进行打分</li>
              <li>自由言论：在讨论区发帖跟帖自由讨论</li>
            </ul>
          </div>
          <div v-bind:style="{ fontSize: '20px', float: left }">
            <h2>导航指南</h2>
            <p>
              您可以通过左侧导航栏进行功能选择，点击对应的功能模块即可进入相应的管理页面。
            </p>
            <ul>
              <li>课程开设——查看学期课程信息</li>
              <li>课堂开设——查看学期课堂信息、选择课堂、查看已获成绩</li>
              <li>教材库——下载资料库中的资料</li>
              <li>讨论区——发布评课信息、自由讨论信息</li>
              <li>个人资料——管理个人信息</li>
            </ul>
          </div>
          <div v-bind:style="{ fontSize: '10px', float: left }">
            <h2>欢迎联系</h2>
            <p>如果您在使用过程中遇到问题，或者有任何建议，欢迎联系我们。</p>
            <el-link href="https://github.com/Gjmustc">Gjmustc</el-link>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from "./StudentNav";
import StudentHeading from "./StudentHeading";
export default {
  name: "StudentHead",
  components: { StudentHeading, StudentNav },
};
</script>

<style scoped>
@import "../../assets/css/back.css";
</style>
