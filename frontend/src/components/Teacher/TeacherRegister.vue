<template>
  <transition name="head-login-register">
    <div class="background">
      <br />
      <div class="register_block">
        <div class="register_head">
          <p>教师注册</p>
        </div>
        <el-form rules="rules">
          <div id="register-n">
            <el-form-item>
              <el-input
                class="inputs"
                type="text"
                placeholder="请输入姓名"
                v-model="userName"
                clearable
              ></el-input>
            </el-form-item>
          </div>
          <div id="register-name">
            <el-form-item>
              <el-input
                class="inputs"
                type="text"
                placeholder="请输入工号"
                v-model="teacheID"
                clearable
              ></el-input>
            </el-form-item>
          </div>
          <div id="register-email">
            <el-form-item>
              <el-input
                class="inputs"
                type="text"
                placeholder="请输入邮箱"
                v-model="useremail"
                clearable
              ></el-input>
            </el-form-item>
          </div>
          <div id="register-password">
            <el-form-item>
              <el-input
                class="inputs"
                type="text"
                placeholder="请输入密码"
                v-model="userPassWord"
                show-password
                clearable
              ></el-input>
            </el-form-item>
          </div>
          <div id="confirm-password">
            <el-form-item>
              <el-input
                class="inputs"
                type="text"
                placeholder="请确认密码"
                v-model="userPassWord2"
                show-password
                clearable
              ></el-input>
            </el-form-item>
          </div>
          <div class="confirm-button">
            <el-button id="button_in" type="primary" size="small" v-on:click="Register">
              确认
            </el-button>
          </div>
          <div class="return-button">
            <el-button
              id="button_re"
              type="primary"
              plain="true"
              size="small"
              v-on:click="goToTeacherLogin"
            >
              返回
            </el-button>
          </div>
        </el-form>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: " TeacherRegister",
  data: function () {
    return {
      message: "",
      userName: "",
      teacheID: "",
      userPassWord: "",
      userPassWord2: "",
      useremail: "",
    };
  },
  mounted() {
    window.addEventListener("keydown", this.keydown);
  },
  methods: {
    goToTeacherLogin: function () {
      this.$router.push({
        name: "TeacherLogin",
      });
    },
    Register: function () {
      let that = this;
      if (that.userPassWord === "") {
        that.$message.error("密码不能为空");
      } else if (that.teacheID === "") {
        that.$message.error("用户名不能为空");
      } else if (that.userName === "") {
        that.$message.error("请添加您的昵称");
      } else {
        this.$http
          .request({
            url: that.$url + "TeacherRegister/",
            method: "get",
            params: {
              useraccount: that.teacheID,
              username: that.userName,
              password: that.userPassWord,
              password_confirm: that.userPassWord2,
              useremail: that.useremail,
            },
          })
          .then(function (response) {
            console.log(response);
            that.message = response.data.message;
            if (that.message === "register success") {
              that.$router.push({
                name: "TeacherLogin",
              });
            } else if (that.message === "user already exists") {
              that.$message.error("用户已存在");
            } else if (that.message === "password not match") {
              that.$message.error("密码不一致");
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    },
    keydown(e) {
      if (e.keyCode === 13) {
        this.Register();
      }
    },
  },
  destroyed() {
    window.removeEventListener("keydown", this.keydown, false);
  },
};
</script>

<style scoped>
@import "../../assets/css/register.css";
@import "../../assets/css/Transition/head-login-register.css";
</style>
