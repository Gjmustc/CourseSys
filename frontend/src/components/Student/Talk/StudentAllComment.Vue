<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'90px':'400px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container class="comment">
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-row>
            <el-col :span="22">
              <el-input
                placeholder="查找您的相关评论"
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
                @click="searchComment(inputSearch)"
                circle
              ></el-button>
            </el-col>
          </el-row>
          <el-card
            v-for="(comment, index) in showcommentList"
            :key="index"
            v-loading="loading"
            shadow="hover"
            style="font-size: small; margin-bottom: 2%"
          >
            <div slot="header" class="clearfix">
              <el-row>{{ comment.classid }}</el-row>
              <el-row>{{ comment.commenttime }}</el-row>
              <el-button
                v-on:click="deleteMyComment(index)"
                type="text"
                style="font-size: smaller; float: right"
              >
                删除评论
              </el-button>
            </div>
            <div>
              <el-rate
                v-model="comment.classrank"
                disabled
                show-score
                text-color="#ff9900"
              >
              </el-rate>
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
              <span v-html="comment.comment"></span>
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
  name: "StudentAllComment",
  components: { StudentNav, StudentHeading },
  data: function () {
    return {
      loading: true,
      userAccount: "",
      userName: "",
      inputSearch: "",
      commentlist: [
        {
          commentid: "",
          classid: "",
          classrank: "",
          commenttime: "",
          comment: "",
        },
      ],
      showcommentList: this.commentList,
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.showMyComment();
  },
  methods: {
    showMyComment: function () {
      let that = this;
      this.$http
        .request({
          url: that.$url + "GetStudentComments/",
          method: "get",
          params: {
            studentid: that.userAccount,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.commentlist = response.data;
          that.showcommentList = response.data;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
    deleteMyComment: function (index) {
      let that = this;
      this.$http
        .request({
          url: that.$url + "DeleteComment/",
          method: "get",
          params: {
            commentid: that.commentlist[index].commentid,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.showMyComment();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    searchComment: function (inputSearch) {
      this.showMyComment = this.searchByIndexOf(inputSearch, this.commentlist);
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
        if (list[i].comment.indexOf(keyWord) >= 0) {
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
