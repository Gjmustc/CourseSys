<template>
  <el-container class="background">
    <el-aside class="aside" width="show?'90px':'400px'">
      <TeacherNav></TeacherNav>
    </el-aside>
    <el-container class="main">
      <el-header>
        <TeacherHeading></TeacherHeading>
      </el-header>
      <el-main style="padding-left: 10%; padding-right: 10%">
        <el-form label-position="left" v-loading="loading">
          <el-form-item style="width: 50px" label="课号">
            <el-col :span="6">
              <el-input
                placeholder="请输入成绩对应课堂号"
                v-model="classid"
                style="width: 250px"
              ></el-input>
            </el-col>
          </el-form-item>
          <el-form-item style="width: 50px" label="学号">
            <el-col :span="6">
              <el-input
                placeholder="请输入成绩对应学生学号"
                v-model="studentid"
                style="width: 250px"
              ></el-input>
            </el-col>
          </el-form-item>
          <el-form-item style="width: 50px" label="成绩">
            <el-col :span="6">
              <el-input
                placeholder="请输入学生成绩"
                v-model="grade"
                style="width: 250px"
              ></el-input>
            </el-col>
          </el-form-item>
          <el-form-item>
            <el-col :span="6">
              <el-button v-on:click="PushStudentGrade" type="primary">确认</el-button>
            </el-col>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import TeacherNav from "../TeacherNav";
import TeacherHeading from "../TeacherHeading";
export default {
  name: "PushStudentGrade",
  components: { TeacherNav, TeacherHeading },
  data: function () {
    return {
      loading: false,
      userAccount: "",
      userName: "",
      classid: "",
      studentid: "",
      grade: "",
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
  },
  methods: {
    PushStudentGrade: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "PushStudentGrade/",
          method: "get",
          params: {
            studentid: that.studentid,
            classid: that.classid,
            grade: that.grade,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          if (response.data.status === "success") {
            that.$message.success("成绩上传成功");
            classid = "";
            studentid = "";
            grade = "";
          } else {
            that.$message.error("未知错误");
          }
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
  },
};
</script>

<style scoped>
@import "../../../assets/css/nav.css";
@import "../../../assets/css/back.css";
</style>
