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
        <el-main style="padding-right: 10%; padding-left: 10%">
          <el-row>
            <el-col :span="14" class="left-information" style="width: 50%">
              <el-row>
                <el-col :span="22">
                  <el-input
                    placeholder="查找课堂相关评价"
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
                    @click="searchclass(inputSearch)"
                    circle
                  ></el-button>
                </el-col>
              </el-row>
              <el-card
                v-for="(classitem, index) in showclassList"
                :key="index"
                shadow="hover"
                style="font-size: small; margin-bottom: 2%"
              >
                <div slot="header" class="clearfix">
                  <el-col :span="2">
                    <el-image :src="classImg" lazy></el-image>
                  </el-col>
                  <span
                    ><strong>{{
                      classitem.coursename + " " + classitem.teachername
                    }}</strong></span
                  >
                  <el-button
                    v-on:click="commentclass(index)"
                    type="text"
                    style="font-size: small; float: right"
                  >
                    查看评价
                  </el-button>
                  <el-rate
                    v-model="classitem.classrank"
                    disabled
                    show-score
                    text-color="#ff9900"
                  >
                  </el-rate>
                </div>
                <div
                  style="
                    font-size: smaller;
                    text-overflow: ellipsis;
                    max-height: 50px;
                    overflow: hidden;
                    white-space: nowrap;
                  "
                >
                  {{
                    classitem.classtime +
                    " " +
                    classitem.classroom +
                    " " +
                    classitem.currentselect +
                    "人"
                  }}
                </div>
              </el-card>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from "../StudentNav";
import StudentHeading from "../StudentHeading";
import classImg from "../../../assets/img/ustclogo.png";
export default {
  name: "StudentCommentTable",
  components: { StudentNav, StudentHeading },
  data: function () {
    return {
      loading: true,
      userAccount: "",
      userName: "",
      inputSearch: "",
      classList: [
        {
          classid: 1,
          coursename: "前端测试课程1",
          teachername: "前端测试教师1",
          classtime: "周一1-2节",
          classroom: "东上院101",
          classhold: "120",
          currentselect: 0,
          classrank: 4.5,
        },
        {
          classid: 2,
          coursename: "前端测试课程2",
          teachername: "前端测试教师2",
          classtime: "周二1-2节",
          classroom: "东上院102",
          classhold: "120",
          currentselect: 0,
          classrank: 4,
        },
        {
          classid: 3,
          coursename: "前端测试课程3",
          teachername: "前端测试教师3",
          classtime: "周三1-2节",
          classroom: "东上院103",
          classhold: "120",
          currentselect: 0,
          classrank: 2.5,
        },
      ],
      classImg: classImg,
      showclassList: this.classList,
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.GetClassList();
  },
  methods: {
    GetClassList: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetClassList/",
          method: "get",
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.classList = response.data;
          that.showclassList = response.data;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
    commentclass: function (index) {
      let that = this;
      this.$router.push({
        path: "/StudentCommentAndDiscussNav/StudentComment",
        query: {
          classid: that.showclassList[index].classid,
          selectnum: that.showclassList[index].currentselect,
          classrank: that.showclassList[index].classrank,
        },
      });
    },
    searchclass: function (inputSearch) {
      this.showclassList = this.searchByIndexOf(inputSearch, this.classList);
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
        if (list[i].coursename.indexOf(keyWord) >= 0) {
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
