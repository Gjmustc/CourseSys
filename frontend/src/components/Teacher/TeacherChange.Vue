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
        <el-main>
          <el-row>{{ userAccount }} 密码修改 </el-row>
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
import TeacherNav from "./TeacherNav";
import TeacherHeading from "./TeacherHeading";
export default {
  name: "TeacherChange",
  components: { TeacherNav, TeacherHeading },
  data: function () {
    return {
      teacherID: "",
      userAccount: "",
      oldpassword: "",
      newpassword: "",
      confirmpassword: "",
    };
  },
  mounted: function () {
    this.teacherID = this.cookie.getCookie("userAccount");
  },
  methods: {
    changePassWord: function () {
      let that = this;
      if (that.newpassword === "") {
        that.$message.error("密码不能为空");
      } else {
        this.$http
          .request({
            url: that.$url + "TeacherChange/",
            method: "get",
            params: {
              useraccount: that.teacherID,
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
              that.$router.push({
                name: "TeacherLogin",
                params: {
                  useraccount: that.teacherID,
                },
              });
            } else if (that.status === "user not exists") {
              that.$message.error("该教师账户不存在");
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
  },
};
</script>

<style scoped>
@import "../../assets/css/back.css";
</style>
