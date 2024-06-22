<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'300px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <AdminHeading></AdminHeading>
        </el-header>
        <el-main>
          <el-row
            ><span>{{ userName }} 密码修改 </span></el-row
          >
          <el-form label-width="100px">
            <el-form-item label="原密码">
              <el-col span="6">
                <el-input
                  placeholder="请输入原密码"
                  v-model="oldpassword"
                  show-password
                ></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="新密码">
              <el-col span="6">
                <el-input
                  placeholder="请输入新密码"
                  v-model="newpassword"
                  show-password
                ></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="确认新密码">
              <el-col span="6">
                <el-input
                  placeholder="请确认新密码"
                  v-model="confirmpassword"
                  show-password
                ></el-input>
              </el-col>
            </el-form-item>
            <el-form-item>
              <el-col span="6">
                <el-button v-on:click="changePassWord" type="primary">确认</el-button>
              </el-col>
            </el-form-item>
          </el-form>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminNav from "./AdminNav";
import AdminHeading from "./AdminHeading";
export default {
  name: "AdminChange",
  components: { AdminNav, AdminHeading },
  data: function () {
    return {
      adminaccount: "",
      userName: "",
      oldpassword: "",
      newpassword: "",
      confirmpassword: "",
    };
  },
  mounted: function () {
    this.adminaccount = this.cookie.getCookie("userAccount");
  },
  methods: {
    changePassWord: function () {
      let that = this;
      if (that.newpassword === "") {
        that.$message.error("密码不能为空");
      } else {
        this.$http
          .request({
            url: that.$url + "AdminChange/",
            method: "get",
            params: {
              adminaccount: that.adminaccount,
              oldpassword: that.oldpassword,
              newpassword: that.newpassword,
              newpassword_confirm: that.confirmpassword,
            },
          })
          .then(function (response) {
            console.log(response.data);
            that.status = response.data.message;
            if (that.status === "change success") {
              that.$message.success("修改成功");
              //   that.$router.push({
              //     name: 'AdminLogin',
              //     params: {
              //       userName: that.adminaccount
              //     }
              //   })
            } else if (that.status === "admin not exists") {
              that.$message.error("该管理员账户不存在");
            } else if (that.status === "password error") {
              that.$message.error("原密码错误");
            } else if (that.status === "password not match") {
              that.$message.error("新旧密码不一致");
            } else {
              that.$message.error("未知错误");
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    },
    //   goToHelloWorld: function () {
    //     this.cookie.clearCookie('userName')
    //     this.cookie.clearCookie('userName')
    //     this.$router.replace('/')
    //   }
  },
};
</script>

<style scoped>
@import "../../assets/css/back.css";
</style>
