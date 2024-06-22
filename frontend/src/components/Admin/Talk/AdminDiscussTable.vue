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
        <el-main>
          <el-row>
            <el-col :span="14" class="left-information" style="width: 50%">
              <el-row>
                <el-col :span="22">
                  <el-input
                    placeholder="查找相关发帖"
                    prefix-icon="el-icon-search"
                    v-model="inputSearch"
                    style="margin-bottom: 5%"
                  ></el-input>
                </el-col>
                <el-col :span="2">
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    style="float: right"
                    @click="searchDiscuss(inputSearch)"
                    circle
                  ></el-button>
                </el-col>
              </el-row>
              <el-card
                v-for="(mainpost, index) in showMainPostList"
                :key="index"
                shadow="hover"
                style="margin-bottom: 2%"
              >
                <div class="clearfix">
                  <el-col :span="8">
                    <el-image :src="logo" lazy></el-image>
                  </el-col>
                  <el-col :span="16">
                    <el-row>
                      <strong>{{ mainpost.title }}</strong>
                      <el-button
                        style="float: right; padding: 3px 0"
                        type="text"
                        v-on:click="enterMainPost(index)"
                        >进入帖子</el-button
                      >
                    </el-row>
                    <el-row
                      class="textitem"
                      style="font-size: 10px; margin-top: 2%; margin-bottom: 2%"
                    >
                      <el-tag size="mini">{{ mainpost.userid }}</el-tag>
                    </el-row>
                    <el-row>
                      <p style="color: gray; font-size: 12px">
                        发表于-{{ mainpost.posttime }}
                      </p>
                    </el-row>
                  </el-col>
                </div>
              </el-card>
            </el-col>
            <el-col :span="8" :offset="2" class="right-information">
              <el-card shadow="hover" style="width: 100%">
                <el-row>
                  <el-col :span="12">
                    <el-image :src="logo" lazy></el-image>
                  </el-col>
                  <el-col :span="12">
                    <el-descriptions :column="1">
                      <el-descriptions-item label="用户昵称">{{
                        userName
                      }}</el-descriptions-item>
                      <el-descriptions-item label="用户ID">{{
                        userName
                      }}</el-descriptions-item>
                    </el-descriptions>
                  </el-col>
                </el-row>
                <el-row>
                  <el-divider></el-divider>
                </el-row>
                <el-row>
                  <el-button
                    @click="buildThemeVisible = true"
                    style="width: 100%"
                    type="primary"
                    >新建主贴</el-button
                  >
                  <el-dialog
                    title="新建主帖"
                    :visible.sync="buildThemeVisible"
                    width="70%"
                  >
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <el-input
                          v-model="input.title"
                          placeholder="请输入标题"
                        ></el-input>
                      </el-col>
                    </el-row>
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <quill-editor
                          ref="text"
                          v-model="input.content"
                          style="height: 300px"
                        ></quill-editor>
                      </el-col>
                    </el-row>
                    <div slot="footer" class="dialog-footer" style="margin-top: 10%">
                      <el-button @click="buildThemeVisible = false">取消</el-button>
                      <el-button type="primary" @click="PostMain">确定</el-button>
                    </div>
                  </el-dialog>
                </el-row>
              </el-card>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminNav from "../AdminNav";
import AdminHeading from "../AdminHeading";
import { quillEditor } from "vue-quill-editor";
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";
import logo from "../../../assets/img/ustclogo.png";
export default {
  name: "AdminDiscussTable",
  components: { AdminNav, AdminHeading, quillEditor },
  data: function () {
    return {
      loading: true,
      userName: "",
      userName: "",
      inputSearch: "",
      logo: logo,
      input: {
        title: "",
        content: "",
      },
      MainPostList: [
        {
          mainid: 1,
          userid: 1,
          title: "这是一个标题",
          content: "这是一个内容",
          posttime: "2021-06-01 12:00:00",
        },
        {
          mainid: 2,
          userid: 2,
          title: "这是一个标题",
          content: "这是一个内容",
          posttime: "2021-06-01 12:00:00",
        },
        {
          mainid: 3,
          userid: 3,
          title: "这是一个标题",
          content: "这是一个内容",
          posttime: "2021-06-01 12:00:00",
        },
      ],
      showMainPostList: this.MainPostList,
      buildThemeVisible: false,
      time: "",
      status: "",
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.GetMainList();
  },
  methods: {
    GetMainList: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetMainList/",
          method: "get",
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.MainPostList = response.data;
          that.showMainPostList = response.data;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
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
    PostMain: function () {
      let that = this;
      that.getTime();
      this.$http
        .request({
          url: that.$url + "PostMain/",
          method: "get",
          params: {
            userid: that.userAccount,
            title: that.input.title,
            content: that.input.content,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.status = response.data.status;
          if (that.status === "success") {
            that.$message.success("创建成功");
            that.buildThemeVisible = false;
            that.GetMainList();
            that.input = {
              title: "",
              content: "",
            };
          } else {
            that.$message.error("未知错误");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    enterMainPost: function (index) {
      let that = this;
      this.$router.push({
        path: "/AdminCommentAndDiscussNav/AdminDiscuss",
        query: {
          mainid: that.MainPostList[index].mainid,
          title: that.MainPostList[index].title,
          content: that.MainPostList[index].content,
          maintime: that.MainPostList[index].posttime,
        },
      });
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie("userAccount");
      this.cookie.clearCookie("userName");
      this.$router.replace("/");
    },
    searchDiscuss: function (inputSearch) {
      this.showMainPostList = this.searchByIndexOf(inputSearch, this.MainPostList);
    },
    searchByIndexOf: function (keyWord, list) {
      if (!(list instanceof Array)) {
        return;
      } else if (keyWord === "") {
        return list;
      }
      const len = list.length;
      const arr = [];
      for (let i = 0; i < len; i++) {
        // 如果字符串中不包含目标字符会返回-1
        if (list[i].title.indexOf(keyWord) >= 0) {
          arr.push(list[i]);
        }
      }
      return arr;
    },
  },
};
</script>

<style scoped>
@import "../../../assets/css/back.css";
</style>
