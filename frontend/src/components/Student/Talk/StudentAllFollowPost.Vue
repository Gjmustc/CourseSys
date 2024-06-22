<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'90px':'400px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container class="follow">
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-page-header
            @back="returndiscusstable"
            :content="maintitle"
            style="margin-bottom: 2%"
          >
          </el-page-header>
          <el-row>
            <el-col :span="22">
              <el-input
                placeholder="查找您的相关跟贴"
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
                @click="searchFollowPost(inputSearch)"
                circle
              ></el-button>
            </el-col>
          </el-row>
          <el-card
            v-for="(follow, index) in showfollowpostList"
            :key="index"
            v-loading="loading"
            shadow="hover"
            style="font-size: small; margin-bottom: 2%"
          >
            <div slot="header" class="clearfix">
              <el-row>{{ follow.mainid }}</el-row>
              <el-row>{{ follow.posttime }}</el-row>
              <el-button
                v-on:click="deleteMyFollowPost(index)"
                type="text"
                style="font-size: smaller; float: right"
              >
                删除跟帖
              </el-button>
            </div>
            <div
              style="
                font-size: x-small;
                text-overflow: ellipsis;
                max-height: 50px;
                overflow: hidden;
                white-space: nowrap;
              "
            >
              <span v-html="follow.content"></span>
            </div>
          </el-card>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from "../StudentNav";
import StudentHeading from "../StudentHeading";
import { del } from "vue";

export default {
  name: "StudentAllFollowPost",
  components: { StudentNav, StudentHeading },
  data: function () {
    return {
      loading: true,
      userAccount: "",
      userName: "",
      inputSearch: "",
      followpostlist: [
        {
          followid: "",
          userid: "",
          mainid: "",
          content: "",
          posttime: "",
        },
      ],
      showfollowpostList: this.followpostlist,
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.showMyFollowPosts();
  },
  methods: {
    showMyFollowPosts: function () {
      let that = this;
      this.$http
        .request({
          url: that.$url + "GetStudentFollowPosts/",
          method: "get",
          params: {
            studentid: that.userAccount,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.followpostlist = response.data;
          that.showfollowpostList = response.data;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
    deleteMyFollowPost: function (index) {
      let that = this;
      this.$http
        .request({
          url: that.$url + "DeleteFollow/",
          method: "get",
          params: {
            followid: that.followpostlist[index].followid,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.showMyFollowPosts();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    searchFollowPost: function (inputSearch) {
      this.showMyFollowPosts = this.searchByIndexOf(inputSearch, this.followpostlist);
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
        if (list[i].content.indexOf(keyWord) >= 0) {
          arr.push(list[i]);
        }
      }
      return arr;
    },
    returndiscusstable: function () {
      let that = this;
      that.$router.push({
        name: "StudentDiscussTable",
      });
    },
  },
};
</script>

<style scoped>
@import "../../../assets/css/back.css";

.el-row-button {
  width: 100% !important;
}

.el-row-button :hover {
  background-color: initial;
}

.el-row-button-head :hover {
  background-color: hsla(0, 0%, 74%, 0.2);
}
</style>
