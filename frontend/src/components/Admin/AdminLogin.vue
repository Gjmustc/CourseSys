<template>
  <transition name="head-login-register">
    <div class="background">
      <br />
      <div class="register_block">
        <div class="register_head">
          <p>管理员登录</p>
        </div>
        <el-form>
          <div id="register-name">
            <el-form-item>
              <el-input
                class="inputs"
                type="text"
                placeholder="请输入您的管理员账号"
                v-model="adminaccount"
                clearable
              ></el-input>
            </el-form-item>
          </div>
          <div id="register-password">
            <el-form-item>
              <el-input
                class="inputs"
                type="text"
                placeholder="请输入您的密码"
                v-model="adminpassword"
                show-password
                clearable
              ></el-input>
            </el-form-item>
          </div>
          <div class="confirm-button">
            <el-button
              id="button_in"
              type="primary"
              size="small"
              v-on:click="goToAdminHead"
            >
              确认
            </el-button>
          </div>
          <div class="return-text">
            <el-link href="#/" style="font-size: 14px; color: rgb(11, 11, 10)"
              >返回</el-link
            >
          </div>
        </el-form>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "AdminLogin",
  data: function () {
    return {
      adminaccount: "",
      adminpassword: "",
      status: "",
    };
  },
  mounted() {
    window.addEventListener("keydown", this.keydown);
  },
  methods: {
    goToAdminHead: function () {
      let that = this;
      this.$http
        .request({
          url: that.$url + "AdminLogin/",
          method: "get",
          params: {
            adminaccount: that.adminaccount,
            password: that.adminpassword,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.status = response.data.message;
          if (that.status === "login success") {
            let loginInfo = {
              userAccount: that.adminaccount,
            };
            that.cookie.setCookie(loginInfo);
            that.$router.push({
              name: "AdminHead",
            });
          } else if (that.status === "admin not exists") {
            that.$message.error("管理员账号不存在");
          } else if (that.status === "password error") {
            that.$message.error("密码错误");
          } else {
            that.$message.info("请输入管理员账号");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    keydown(e) {
      if (e.keyCode === 13) {
        this.goToAdminHead();
      }
    },
    destroyed() {
      window.removeEventListener("keydown", this.keydown, false);
    },
  },
};
</script>

<style scoped>
@import "../../assets/css/login.css";
@import "../../assets/css/Transition/head-login-register.css";
</style>
