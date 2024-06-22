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
            <el-col :span="23">
              <el-input
                placeholder="查找已开课堂"
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
            v-for="(course, index) in showClassList"
            :key="index"
            v-loading="loading"
            shadow="hover"
            style="margin-bottom: 2%"
          >
            <el-row>
              <el-col :offset="1" :span="16">
                <el-row>
                  <span style="font-size: 16px"
                    ><strong>{{
                      course.coursename + " " + course.teachername
                    }}</strong></span
                  >
                </el-row>
                <el-row>
                  <el-tag type="info"
                    >课堂编号<span>&nbsp;&nbsp;{{ course.classid }}</span></el-tag
                  >
                  <el-tag type="info"
                    >上课时间<span>&nbsp;&nbsp;{{ course.classtime }}</span></el-tag
                  >
                  <el-tag type="info"
                    >上课地点<span>&nbsp;&nbsp;{{ course.classroom }}</span></el-tag
                  >
                </el-row>
                <el-row>
                  <el-tag type="info"
                    >课程容量<span>&nbsp;&nbsp;{{ course.classhold }}</span></el-tag
                  >
                  <el-tag type="info"
                    >已选人数<span>&nbsp;&nbsp;{{ course.currentselect }}</span></el-tag
                  >
                </el-row>
                <el-row>
                  <span style="font-size: 16px"
                    >推荐教材：{{ course.recommendmaterial }}</span
                  >
                </el-row>
              </el-col>
              <el-col :span="2">
                <el-button-group style="margin-top: 2%">
                  <el-button v-on:click="selectClass(index)" type="primary"
                    >选课</el-button
                  >
                </el-button-group>
              </el-col>
            </el-row>
          </el-card>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
@import "../../../assets/css/back.css";
.info {
  margin-bottom: 20px;
  word-break: break-all;
}
</style>

<script>
import StudentNav from "../StudentNav";
import StudentHeading from "../StudentHeading";
import CourseImg from "../../../assets/img/buaa_class_img.jpg";
export default {
  /* eslint-disable */
  name: "SelectClass",
  components: { StudentNav, StudentHeading },
  data: function () {
    return {
      loading: false,
      userAccount: "",
      userName: "",
      classList: [
        {
          classid: "302301.01",
          coursename: "计算机网络",
          teachername: "张三",
          classtime: "周一1-2节",
          classroom: "东区1-101",
          classhold: 60,
          currentselect: 41,
          recommendmaterial: "无",
        },
        {
          classid: "302301.02",
          coursename: "计算机网络",
          teachername: "张三",
          classtime: "周一1-2节",
          classroom: "东区1-101",
          classhold: 60,
          currentselect: 41,
          recommendmaterial: "无",
        },
      ],
      showClassList: this.classList,
      inputSearch: "",
      message: "",
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.getClassList();
  },
  methods: {
    getClassList: function () {
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
          that.showClassList = response.data;
        })
        .catch(function (error) {
          that.loading = false;
          console.log(error);
        });
    },
    selectClass(index) {
      console.log(index);
      let that = this;
      this.$http
        .request({
          url: that.$url + "SelectClass/",
          method: "get",
          params: {
            studentid: this.userAccount,
            classid: this.showClassList[index].classid,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.message = response.data.message;
          if (that.message === "select class success") {
            that.$message.success("选课成功");
          } else if (that.message === "class already selected") {
            that.$message.info("已选择该课程");
          } else if (that.message === "class is full") {
            that.$message.info("课堂容量已达上限");
          } else if (that.message === "time conflict") {
            that.$message.info("选课时间冲突");
          } else {
            that.$message.error("!");
          }
        });
    },
    searchCourse: function (inputSearch) {
      this.showClassList = this.searchByIndexOf(inputSearch, this.classList);
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
