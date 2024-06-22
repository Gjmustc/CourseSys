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
        <el-main style="padding-right: 10%; padding-left: 10%">
          <el-row>
            <el-col :span="23">
              <el-input
                placeholder="查找课程"
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
                @click="searchCourse(inputSearch)"
                circle
              ></el-button>
            </el-col>
          </el-row>
          <el-card
            v-for="(course, index) in showCourseList"
            :key="index"
            v-loading="loading"
            shadow="hover"
            style="margin-bottom: 2%"
          >
            <el-row>
              <el-col :offset="2" :span="2">
                <el-image :src="courseImg" lazy></el-image>
              </el-col>
              <el-col :offset="2" :span="14">
                <el-row style="margin-bottom: 3%">
                  <el-link type="primary" v-on:click="getCourseInfo(index)">
                    <span style="font-size: 16px"
                      ><strong>{{ course.coursename }}</strong></span
                    >
                  </el-link>
                </el-row>
                <el-row>
                  <el-tag type="primary"
                    >课程编号<span>&nbsp;&nbsp;{{ course.courseid }}</span></el-tag
                  >
                </el-row>
              </el-col>
            </el-row>
          </el-card>
          <el-dialog title="提示" :visible.sync="courseInfoVisible" width="40%">
            <el-descriptions class="info" direction="vertical">
              <el-descriptions-item label="课程名">
                &nbsp;&nbsp;
                {{ courseinfo.coursename }}
              </el-descriptions-item>
              <el-descriptions-item label="课程学分">
                &nbsp;&nbsp;
                {{ courseinfo.coursecredit }}
              </el-descriptions-item>
              <el-descriptions-item label="课程介绍">
                &nbsp;&nbsp;
                {{ courseinfo.coursedescription }}
              </el-descriptions-item>
            </el-descriptions>
            <div slot="footer" class="dialog-footer">
              <el-button type="primary" @click="courseInfoVisible = false"
                >确 定</el-button
              >
            </div>
          </el-dialog>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from "../TeacherNav";
import TeacherHeading from "../TeacherHeading";
import CourseImg from "../../../assets/img/ustclogo.png";
export default {
  /* eslint-disable */
  name: "TeacherCourseTable",
  components: { TeacherHeading, TeacherNav },
  data: function () {
    return {
      courseInfoVisible: false,
      courseinfo: {
        courseid: "",
        coursename: "",
        coursecredit: 0,
        coursedescription: "",
      },
      courseImg: CourseImg,
      loading: false,
      userAccount: "",
      userName: "",
      courselist: [
        {
          courseid: "1",
          coursename: "课程1",
          coursecredit: 3,
          coursedescription: "课程1描述",
        },
        {
          courseid: "2",
          coursename: "课程2",
          coursecredit: 3,
          coursedescription: "课程2描述",
        },
        {
          courseid: "3",
          coursename: "课程3",
          coursecredit: 3,
          coursedescription: "课程3描述",
        },
      ],
      showCourseList: this.courselist,
      inputSearch: "",
      status: "",
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.GetCourseList();
  },
  methods: {
    getCourseInfo: function (index) {
      let that = this;
      that.courseinfo = that.courselist[index];
      that.courseInfoVisible = true;
    },
    GetCourseList: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetCourseList/",
          method: "get",
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.courselist = response.data;
          that.showCourseList = response.data;
        })
        .catch(function (error) {
          that.loading = false;
          console.log(error);
        });
    },
    searchCourse: function (inputSearch) {
      this.showCourseList = this.searchByIndexOf(inputSearch, this.courselist);
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
.info {
  margin-bottom: 20px;
  word-break: break-all;
}
</style>
