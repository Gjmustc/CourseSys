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
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-page-header
            @back="returnTeacherCommentTable"
            style="margin-bottom: 2%"
          ></el-page-header>
          <el-card shadow="hover" style="margin-bottom: 1%">
            <el-row>
              <el-col :offset="1" :span="3">
                <el-image :src="courseImg" lazy></el-image>
                <el-row> &nbsp; </el-row>
                <el-row style="text-align: center; font-size: medium"> 课程评分 </el-row>
                <el-rate
                  align="center"
                  v-model="classrank"
                  disabled
                  show-score
                  text-color="#ff9900"
                ></el-rate>
              </el-col>
              <el-col :offset="2" :span="17">
                <el-row>
                  <el-col :span="18">
                    <strong>{{ coursename }}</strong>
                  </el-col>
                </el-row>
                <el-row>
                  <el-divider> </el-divider>
                </el-row>
                <el-row>
                  <div style="font-size: small">
                    <h3>上课老师</h3>
                    <span v-html="teachername"></span>
                    <h3>上课人数</h3>
                    <span v-html="selectnum"></span>
                    <h3>课程资料</h3>
                    <span v-html="materials"></span>
                    <h3>课堂平均分</h3>
                    <span v-html="avg_mark"></span>
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
              <el-col :span="1">
                <el-image :src="TeacherImg" fit="contain" lazy></el-image>
              </el-col>
              <el-col :span="3" :offset="1">
                <el-row class="userName"> {{ comment.studentid }}: </el-row>
                <el-row class="time">{{ comment.commenttime }}</el-row>
              </el-col>
              <el-col :span="19" class="content">
                <el-row class="class-rank" v-html="comment.classrank"> </el-row>
                <el-row class="content-of-comment" v-html="comment.comment"> </el-row>
              </el-col>
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
import TeacherNav from "../TeacherNav";
import TeacherHeading from "../TeacherHeading";
import TeacherImg from "../../../assets/img/teacher.png";
import courseImg from "../../../assets/img/ustclogo.png";
export default {
  name: "TeacherComment",
  components: { TeacherNav, TeacherHeading },
  data: function () {
    return {
      loading: true,
      courseImg: courseImg,
      TeacherImg: TeacherImg,
      userAccount: "",
      userName: "",
      classid: "",
      coursename: "",
      teachername: "",
      selectnum: 0,
      avg_mark: 0,
      materials: "",
      contentInput: "",
      classrank: 0,
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
    this.classid = this.$route.query.classid;
    this.coursename = this.$route.query.coursename;
    this.teachername = this.cookie.getCookie("userName");
    this.selectnum = this.$route.query.selectnum;
    this.classrank = this.$route.query.classrank;
    this.getCommentList();
    this.getClassInfo();
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
    getClassInfo: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetClassInfo/",
          method: "get",
          params: {
            classid: that.classid,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.avg_mark = response.data.avg_mark;
          that.materials = response.data.recommendmaterial;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
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
    returnTeacherCommentTable: function () {
      let that = this;
      that.$router.push({
        name: "TeacherCommentTable",
      });
    },
  },
};
</script>
