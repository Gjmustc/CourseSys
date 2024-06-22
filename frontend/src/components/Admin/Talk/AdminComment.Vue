<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'90px':'400px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <AdminHeading></AdminHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-page-header
            @back="returnCommentTable"
            style="margin-bottom: 2%"
          ></el-page-header>
          <el-card shadow="hover" style="margin-bottom: 1%">
            <el-row>
              <el-col :offset="1" :span="5">
                <el-image
                  style="width: 60%; height: 60%"
                  :src="courseImg"
                  lazy
                ></el-image>
                <el-row> &nbsp; </el-row>
                <el-row style="float: left; font-size: medium"> 课程评分 </el-row>
                <el-rate
                  align="center"
                  v-model="classrank"
                  disabled
                  show-score
                  text-color="#ff9900"
                ></el-rate>
              </el-col>
              <el-col :span="17">
                <el-row>
                  <strong>{{ coursename }}</strong>
                </el-row>
                <el-row>
                  <el-divider> </el-divider>
                </el-row>
                <el-row>
                  <div style="font-size: large">
                    <span>{{ "上课老师: " + teachername }}</span>
                    <span>{{ "上课人数：" + selectnum }}</span>
                  </div>
                </el-row>
              </el-col>
            </el-row>
          </el-card>
          <el-row>
            <el-divider></el-divider>
          </el-row>
          <el-divider></el-divider>
          <div v-for="comment in commentList" v-bind:key="comment">
            <el-row v-loading="loading">
              <el-col :span="2">
                <el-image :src="StudentImg" fit="contain" lazy></el-image>
              </el-col>
              <el-col :span="4">
                <el-row class="userName" style="margin-bottom: 2%; float: left">
                  {{ comment.studentid }}:
                </el-row>
                <el-row class="class-rank" style="margin-bottom: 2%; float: left">
                  {{ "评课打分： " + comment.classrank }}</el-row
                >
                <el-row class="time" style="float: left">{{
                  comment.commenttime
                }}</el-row>
              </el-col>
              <el-col :span="18" class="content">
                <el-row class="content-of-comment"> {{ comment.comment }}</el-row>
              </el-col>
            </el-row>
            <el-row class="delete" :span="2" style="float: right">
              <el-link type="danger" v-on:click="deleteComment(comment.commentid)"
                >删除</el-link
              >
            </el-row>
            <el-divider></el-divider>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
@import "../../../assets/css/back.css";
.buttons {
  margin-bottom: 10px;
}
.input {
  font-size: medium;
}
.time {
  font-size: small;
  color: #e2e2e2;
}
.userName {
  font-size: medium;
  color: #66b1ff;
}
.content {
  font-size: medium;
  word-break: break-all;
}
.content-of-comment {
  color: black;
}
</style>

<script>
import AdminNav from "../AdminNav";
import AdminHeading from "../AdminHeading";
import CourseImg from "../../../assets/img/ustclogo.png";
import StudentImg from "../../../assets/img/student.png";
export default {
  name: "AdminComment",
  components: { AdminNav, AdminHeading },
  data: function () {
    return {
      loading: true,
      StudentImg: StudentImg,
      userAccount: "",
      userName: "",
      classid: "",
      coursename: "",
      teachername: "",
      selectnum: 0,
      classrank: 0,
      contentInput: "",
      courseImg: CourseImg,
      commentList: [
        {
          commentid: "",
          studentid: "",
          classrank: "",
          commenttime: "",
          comment: "",
        },
      ],
    };
  },
  mounted() {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.classid = this.$route.query.classId;
    this.coursename = this.$route.query.coursename;
    this.teachername = this.$route.query.teachername;
    this.selectnum = this.$route.query.selectnum;
    this.classrank = this.$route.query.classrank;
    this.getCommentList();
  },
  methods: {
    getTime: function () {
      let dt = new Date();
      let yyyy = dt.getFullYear();
      let MM = (dt.getMonth() + 1).toString().padStart(2, "0");
      let dd = dt.getDate().toString().padStart(2, "0");
      let h = dt.getHours().toString().padStart(2, "0");
      let m = dt.getMinutes().toString().padStart(2, "0");
      let s = dt.getSeconds().toString().padStart(2, "0");
      this.time = yyyy + "-" + MM + "-" + dd + " " + h + ":" + m + ":" + s;
    },
    getCommentList: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetCommentList/",
          method: "get",
          params: {
            classid: that.classid,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.commentList = response.data;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
    deleteComment: function (commentId) {
      this.$confirm("此操作将永久删除该评价，是否继续？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      }).then(() => {
        let that = this;
        that.getTime();
        this.$http
          .request({
            url: that.$url + "DeleteComment/",
            method: "get",
            params: {
              commentid: commentId,
            },
          })
          .then(function (response) {
            console.log(response.data);
            if (response.data.status === "success") {
              that.$message.success("删除成功");
              that.getCommentList();
            } else {
              that.$message.error("未知错误");
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      });
    },
    returnCommentTable: function () {
      let that = this;
      that.$router.push({
        name: "AdminCommentTable",
      });
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie("userName");
      this.cookie.clearCookie("userAccount");
      this.$router.replace("/");
    },
  },
};
</script>
