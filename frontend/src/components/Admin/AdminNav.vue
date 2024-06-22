<template>
  <el-menu
    :default-active="this.$route.path"
    router
    :collapse="isCollapsed"
    class="el-head-menu"
  >
    <el-menu-item class="item" index="/AdminHead">
      <i class="el-icon-s-home"></i>
      <span class="item">首页</span>
    </el-menu-item>
    <el-submenu index="1">
      <template slot="title"
        ><i class="el-icon-s-custom"></i><span class="item">学生资料</span></template
      >
      <el-menu-item class="subitem" index="/StudentTable">学生信息</el-menu-item>
    </el-submenu>
    <el-submenu index="2">
      <template slot="title"
        ><i class="el-icon-s-check"></i><span class="item">教师资料</span></template
      >
      <el-menu-item class="subitem" index="/TeacherTable">教师信息</el-menu-item>
    </el-submenu>
    <el-submenu index="3">
      <template slot="title"
        ><i class="el-icon-document"></i><span class="item">课程开设</span></template
      >
      <el-menu-item class="subitem" index="/AdminCourseTable/AdminCourseTable"
        >课程信息</el-menu-item
      >
    </el-submenu>
    <el-submenu index="4">
      <template slot="title"
        ><i class="el-icon-document-copy"></i><span class="item">课堂开设</span></template
      >
      <el-menu-item class="subitem" index="/AdminClassTable/AdminClassTable"
        >课堂列表</el-menu-item
      >
    </el-submenu>
    <el-submenu index="5">
      <template slot="title"
        ><i class="el-icon-share"></i><span class="item">教材库</span></template
      >
      <el-menu-item class="subitem" index="/AdminMaterialTable/AdminMaterialTable"
        >资料清单</el-menu-item
      >
    </el-submenu>
    <el-submenu index="6">
      <template slot="title"
        ><i class="el-icon-s-comment"></i><span class="item">讨论区</span></template
      >
      <el-menu-item class="subitem" index="/AdminCommentAndDiscussNav/AdminCommentTable"
        >课程评价</el-menu-item
      >
      <el-menu-item class="subitem" index="/AdminCommentAndDiscussNav/AdminDiscussTable"
        >自由贴吧</el-menu-item
      >
    </el-submenu>
    <el-submenu index="7">
      <template slot="title"
        ><i class="el-icon-user"></i><span class="item">个人资料</span></template
      >
      <el-menu-item class="subitem" index="/AdminChange">个人信息</el-menu-item>
    </el-submenu>
  </el-menu>
</template>

<script>
import Utils from "../../assets/js/util.js";
export default {
  name: "AdminNav",
  data() {
    return {
      userAccount: "",
      userName: "",
      isCollapsed: this.$root.isCollapsed,
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    var that = this;
    Utils.$on("toggleCollapseAdmin", function (message) {
      console.log(message);
      that.toggleCollapse();
    });
  },
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie("userAccount");
      this.cookie.clearCookie("userName");
      this.$router.replace("/");
    },
    toggleCollapse: function () {
      this.isCollapsed = !this.isCollapsed;
      this.$root.isCollapsed = this.isCollapsed;
    },
  },
};
</script>

<style scoped>
@import "../../assets/css/nav.css";
</style>
