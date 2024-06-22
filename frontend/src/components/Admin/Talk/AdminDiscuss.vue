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
            @back="returndiscusstable"
            :content="maintitle"
            style="margin-bottom: 2%"
          >
          </el-page-header>
          <el-row class="buttons">
            <el-col :span="20">
              <el-input
                class="input"
                v-model="input.content"
                type="textarea"
                :rows="2"
                placeholder="在这里发布你的见解"
              >
              </el-input>
            </el-col>
            <el-col :span="4">
              <el-button
                v-on:click="PostFollow"
                type="primary"
                size="small"
                circle
                icon="el-icon-upload"
                >跟帖</el-button
              >
            </el-col>
          </el-row>
          <el-divider><strong>楼主</strong></el-divider>
          <el-row class="content">
            <span v-html="maincontent"></span>
          </el-row>
          <el-row>
            <el-col :span="9" class="time" style="float: left">
              {{ mainpostime }}
            </el-col>
            <el-col :span="2" class="delete" style="float: right">
              <el-link type="danger" v-on:click="deleteMainPost">删除</el-link>
            </el-col>
          </el-row>
          <el-divider><strong>跟贴</strong></el-divider>
          <div v-for="post in postList" v-bind:key="post.followid">
            <el-row class="userName" style="float: left">
              {{ post.userid }}
            </el-row>
            <el-row class="content">
              <span v-html="post.content"></span>
            </el-row>
            <el-row>
              <el-col :span="9" class="time" style="float: left">
                {{ post.posttime }}
              </el-col>
              <el-col :span="2" class="delete" style="float: right">
                <el-link type="danger" v-on:click="deletePost(post.followid)"
                  >删除</el-link
                >
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
  font-size: large;
}
.time {
  font-size: small;
  color: #e2e2e2;
}
.userName {
  font-size: small;
  color: #66b1ff;
}
.content {
  font-size: medium;
  word-break: break-all;
}
</style>

<script>
import AdminNav from "../AdminNav";
import AdminHeading from "../AdminHeading";
export default {
  name: "AdminDiscuss",
  components: { AdminNav, AdminHeading },
  data: function () {
    return {
      userName: "前端测试用户名",
      userName: "前端测试姓名",
      mainid: "",
      maintitle: "",
      maincontent: "",
      mainpostime: "",
      input: {
        content: "",
      },
      postList: [
        {
          followid: "测试ID",
          userid: "测试用户ID",
          content: "测试内容",
          posttime: "2024-05-02 10:00:00",
        },
        {
          followid: "测试ID",
          userid: "测试用户ID",
          content: "测试内容",
          posttime: "2024-05-02 10:00:00",
        },
      ],
      time: "",
      status: "",
    };
  },
  mounted() {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.mainid = this.$route.query.mainid;
    this.maintitle = this.$route.query.title;
    this.maincontent = this.$route.query.content;
    this.mainpostime = this.$route.query.maintime;
    this.getPostList();
  },
  methods: {
    getTime: function () {
      let that = this;
      let dt = new Date();
      let yyyy = dt.getFullYear();
      let MM = (dt.getMonth() + 1).toString().padStart(2, "0");
      let dd = dt.getDate().toString().padStart(2, "0");
      let h = dt.getHours().toString().padStart(2, "0");
      let m = dt.getMinutes().toString().padStart(2, "0");
      let s = dt.getSeconds().toString().padStart(2, "0");
      that.time = yyyy + "-" + MM + "-" + dd + " " + h + ":" + m + ":" + s;
    },
    deleteMainPost: function () {
      this.$confirm("此操作将永久删除该主贴及其跟贴，是否继续？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        let that = this;
        that.getTime();
        this.$http
          .request({
            url: that.$url + "DeleteMain/",
            method: "get",
            params: {
              mainid: that.mainid,
            },
          })
          .then(function (response) {
            console.log(response.data);
            that.status = response.data.status;
            if (that.status === "success") {
              that.$message.success("删除成功");
              that.returndiscusstable();
            } else {
              that.$message.error("未知错误");
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      });
    },
    getPostList: function () {
      let that = this;
      this.$http
        .request({
          url: that.$url + "GetFollowListByMain/",
          method: "get",
          params: {
            mainid: that.mainid,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.postList = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    PostFollow: function () {
      let that = this;
      that.getTime();
      this.$http
        .request({
          url: that.$url + "PostFollow/",
          method: "get",
          params: {
            mainid: that.mainid,
            userid: that.userAccount,
            content: that.input.content,
          },
        })
        .then(function (response) {
          console.log(response.data);
          if (response.data.status === "success") {
            that.$message.success("跟贴成功");
            that.getPostList();
            that.input.content = "";
          } else {
            that.$message.error("未知错误");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    deletePost: function (followid) {
      this.$confirm("此操作将永久删除该跟贴，是否继续？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        let that = this;
        that.getTime();
        this.$http
          .request({
            url: that.$url + "DeleteFollow/",
            method: "get",
            params: {
              followid: followid,
            },
          })
          .then(function (response) {
            console.log(response.data);
            that.status = response.data.status;
            if (that.status === "success") {
              that.$message.success("删除成功");
              that.getPostList();
            } else {
              that.$message.error("未知错误");
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      });
    },
    returndiscusstable: function () {
      let that = this;
      that.$router.push({
        name: "AdminDiscussTable",
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
