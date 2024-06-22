<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'300px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <AdminHeading></AdminHeading>
        </el-header>
        <el-main style="padding-right: 10%; padding-left: 10%">
          <el-row>
            <el-col :span="23">
              <el-input
                placeholder="查找学生"
                prefix-icon="el-icon-search"
                v-model="inputSearch"
                style="margin-bottom: 5%"
              ></el-input>
            </el-col>
            <el-col :span="1">
              <el-button
                type="primary"
                icon="el-icon-search"
                style="float: right"
                @click="searchStudent(inputSearch)"
                circle
              ></el-button>
            </el-col>
          </el-row>
          <el-card
            v-for="(student, index) in showStudentList"
            :key="index"
            style="margin-bottom: 2%"
          >
            <el-row>
              <el-col :offset="2" :span="2">
                <el-empty
                  :image-size="40"
                  style="margin: 0 !important; padding: 0 !important"
                ></el-empty>
              </el-col>
              <el-col :offset="4" :span="16">
                <el-row style="margin-bottom: 3%">
                  <span style="font-size: 16px"
                    ><strong>{{ student.studentname }}</strong></span
                  >
                </el-row>
                <el-row>
                  <el-tag type="info">学号</el-tag>
                  <span style="color: gray">&nbsp;&nbsp;{{ student.studentid }}</span>
                  <el-tag type="info">专业</el-tag
                  ><span style="color: gray">&nbsp;&nbsp;{{ student.major }}</span>
                  <el-tag type="info">入学年份</el-tag
                  ><span style="color: gray">&nbsp;&nbsp;{{ student.enrollyear }}</span>
                </el-row>
                <el-row>
                  <el-tag type="info">邮箱</el-tag
                  ><span style="color: gray">&nbsp;&nbsp;{{ student.useremail }}</span>
                </el-row>
              </el-col>
            </el-row>
          </el-card>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminNav from "../AdminNav";
import AdminHeading from "../AdminHeading";
export default {
  name: "AdminTable",
  components: { AdminHeading, AdminNav },
  data: function () {
    return {
      loading: true,
      userAccount: "",
      userName: "",
      showStudentList: this.studentList,
      studentList: [
        {
          studentid: 1,
          studentname: "张三",
          major: "计算机科学与技术",
          enrollyear: 2020,
          useremail: "example@qq.com",
        },
        {
          studentid: 2,
          studentname: "李四",
          major: "计算机科学与技术",
          enrollyear: 2020,
          useremail: "slio@qq.com",
        },
        {
          studentid: 3,
          studentname: "王五",
          major: "计算机科学与技术",
          enrollyear: 2020,
          useremail: "qoio@mail.ustc.edu.cn",
        },
      ],
      inputSearch: "",
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.getStudentList();
  },
  methods: {
    getStudentList: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetStudentList/",
          method: "get",
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.studentList = response.data;
          that.showStudentList = response.data;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
    searchStudent: function (inputSearch) {
      this.showStudentList = this.searchByIndexOf(inputSearch, this.studentList);
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
        if (list[i].studentname.indexOf(keyWord) >= 0) {
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
