<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'90px':'400px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-page-header
            @back="returnCommentTable"
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
          <el-row>
            <div style="font-size: medium">给课程评分</div>
            <el-rate style="font-size: medium" v-model="rank" show-text> </el-rate>
          </el-row>
          <el-row> &nbsp; </el-row>
          <el-row>
            <el-col>
              <el-input
                class="input"
                v-model="contentInput"
                type="textarea"
                :rows="3"
                placeholder="对于课程内容、讲课质量、考核方式等的评价"
              >
              </el-input>
            </el-col>
            <el-button
              v-on:click="CommentClass"
              type="primary"
              size="small"
              style="float: right"
              >添加评价</el-button
            >
          </el-row>
          <el-divider></el-divider>
          <div v-for="comment in commentList" v-bind:key="comment">
            <el-row v-loading="loading">
              <el-col :span="1">
                <el-image :src="studentImg" fit="contain" lazy></el-image>
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
import StudentNav from "../StudentNav";
import StudentHeading from "../StudentHeading";
import StudentImg from "../../../assets/img/student.png";
import courseImg from "../../../assets/img/ustclogo.png";
export default {
  name: "StudentComment",
  components: { StudentNav, StudentHeading },
  data: function () {
    return {
      loading: true,
      courseImg: courseImg,
      studentImg: StudentImg,
      userAccount: "",
      userName: "",
      classid: "",
      stuid: "",
      coursename: "",
      teachername: "",
      selectnum: 0,
      avg_mark: 0,
      materials: [],
      classrank: 0,
      rank: 0,
      contentInput: "",
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
    this.selectnum = this.$route.query.selectnum;
    this.stuid = this.cookie.getCookie("userAccount");
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
    CommentClass: function () {
      let that = this;
      that.getTime();
      this.$http
        .request({
          url: that.$url + "CommentClass/",
          method: "get",
          params: {
            studentid: that.stuid,
            classid: that.classid,
            class_rank: that.rank,
            comment: that.contentInput,
          },
        })
        .then(function (response) {
          console.log(response.data);
          if (response.data.status === "success") {
            that.$message.success("评价成功");
            that.getCommentList();
            that.contentInput = "";
          } else {
            that.$message.error("未知错误");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    returnCommentTable: function () {
      let that = this;
      that.$router.push({
        name: "StudentCommentTable",
      });
    },
  },
};
</script>
