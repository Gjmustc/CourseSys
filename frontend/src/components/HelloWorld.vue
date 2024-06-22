<template>
  <transition name="head-login-register">
    <div class="welcome">
      <div class="navigator">
        <div class="navigator-left">
          <i class="el-icon-s-platform"
            ><span class="el-icon-s-platform-text">&nbsp;&nbsp;CourseSys</span></i
          >
        </div>
        <div class="navigator-right">
          <span
            ><el-button class="buttons" @click="goToStudentLogin"
              >学生登录</el-button
            ></span
          >
          <span>&nbsp;&nbsp;</span>
          <span
            ><el-button class="buttons" @click="goToTeacherLogin"
              >教师登录</el-button
            ></span
          >
          <span>&nbsp;&nbsp;</span>
          <span
            ><el-button class="buttons" @click="goToAdminLogin"
              >管理员登录</el-button
            ></span
          >
        </div>
      </div>
      <div class="introduction">
        <el-carousel height="600px">
          <el-carousel-item v-for="(item, index) in headImg" :key="index">
            <img :src="item.src" style="width: 100%; height: 100%" alt="" />
            <div class="cover">
              {{ item.title }}<br />
              <span style="font-size: 25px">{{ item.subTitle }}</span>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
      <div class="copyright">
        <div class="copyright-block">
          <div class="first-copyright-head">Platform</div>
          <div class="first-copyright-content">中科大数据库系统及应用</div>
        </div>
        <div class="copyright-block">
          <div class="author-head">Tech Stack</div>
          <div class="author-task">
            <span class="author-task">后端---Django</span>
          </div>
          <div class="author-task">
            <span class="author-task">前端---Vue</span>
          </div>
          <div class="author-task">
            <span class="author-task">数据库---MySQL</span>
          </div>
        </div>
        <div class="copyright-block">
          <div class="third-copyright-head">Contact Us</div>
          <div class="third-copyright-link">
            <p>
              <a href="https://github.com/Gjmustc" class="links">开发者账号</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import headimg1 from "../assets/img/headimg1.png";
import headimg2 from "../assets/img/headimg2.png";
import headimg3 from "../assets/img/headimg3.png";

export default {
  data: function () {
    return {
      headImg: [
        {
          title: "选课平台",
          subTitle: "Select your favorite course",
          src: headimg1,
        },
        {
          title: "贴吧中心",
          subTitle: "Post whatever you want",
          src: headimg2,
        },
        {
          title: "资料分享",
          subTitle: "Share your materials here",
          src: headimg3,
        },
      ],
      fullscreenLoading: false,
    };
  },
  methods: {
    goToStudentLogin() {
      this.$router.push({
        name: "StudentLogin",
      });
    },
    goToTeacherLogin() {
      this.$router.push({
        name: "TeacherLogin",
      });
    },
    goToAdminLogin() {
      this.$router.push({
        name: "AdminLogin",
      });
    },
  },
};
</script>

<style scoped>
@import "../assets/css/HelloWorld/copyright.css";
@import "../assets/css/HelloWorld/introduction.css";
@import "../assets/css/HelloWorld/navigator.css";
@import "../assets/css/Transition/head-login-register.css";
.welcome {
  margin-left: 80px;
  margin-right: 80px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
</style>
