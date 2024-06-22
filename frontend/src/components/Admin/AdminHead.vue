<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'90px':'250px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <AdminHeading></AdminHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
          <div v-bind:style="{ fontSize: '20px', float: left }">
            <h2>CourseSys</h2>
            <p>
              CourseSys是一个基于Django+Vue+MySQL框架开发的小型B/S应用，面向管理员开放的功能主要有：
            </p>
            <ul>
              <li>课程管理：对课程进行开设、修改、删除</li>
              <li>课堂管理：对课堂教室时间安排进行统筹</li>
              <li>用户管理：对用户人员信息进行统一管理</li>
              <li>教材管理：对教材资料进行统一收管</li>
              <li>言论管理：对学生评价和自由讨论社区的帖子进行管理</li>
            </ul>
          </div>
          <div v-bind:style="{ fontSize: '20px', float: left }">
            <h2>导航指南</h2>
            <p>
              您可以通过左侧导航栏进行功能选择，点击对应的功能模块即可进入相应的管理页面。
            </p>
            <ul>
              <li>学生资料——管理平台学生信息</li>
              <li>教师资料——管理平台教师信息</li>
              <li>课程概览——管理平台课程信息</li>
              <li>课堂开设——管理平台课堂信息</li>
              <li>教材库——管理平台教材信息</li>
              <li>评课社区——查看学生评课信息</li>
              <li>讨论区——查看自由讨论社区信息</li>
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
import AdminNav from "./AdminNav";
import AdminHeading from "./AdminHeading";
export default {
  name: "AdminHead",
  components: { AdminHeading, AdminNav },
};
</script>

<style scoped>
@import "../../assets/css/back.css";
</style>
