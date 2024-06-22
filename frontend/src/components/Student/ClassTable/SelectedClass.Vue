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
          <el-row>
            <el-col :span="20" class="left-information" style="width: 50%">
              <el-row>
                <el-col :span="17">
                  <el-input
                    placeholder="查找已选课程"
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
                    @click="searchCourse(inputSearch)"
                    circle
                  ></el-button>
                </el-col> </el-row
              ><el-card
                v-for="(course, index) in showMyClassList"
                :key="index"
                shadow="hover"
                style="margin-bottom: 2%"
              >
                <el-row v-loading="loading">
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
                      <span style="font-size: 16px"
                        >推荐教材：{{ course.recommendmaterial }}</span
                      >
                    </el-row>
                    <el-row>
                      <span style="font-size: 20px">成绩：{{ course.grade }}</span>
                    </el-row>
                  </el-col>
                  <el-col :span="2">
                    <el-button-group style="margin-top: 2%">
                      <el-button v-on:click="dropClass(index)" type="danger" size="small"
                        >退课</el-button
                      >
                    </el-button-group>
                  </el-col>
                </el-row>
              </el-card>
            </el-col>
            <el-col :span="8" :offset="1" class="right-information">
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
                        userAccount
                      }}</el-descriptions-item>
                    </el-descriptions>
                  </el-col>
                </el-row>
                <el-row>
                  <el-divider></el-divider>
                </el-row>
                <el-row>
                  <el-button
                    @click="
                      GPAVisible = true;
                      getStudentGPA();
                    "
                    style="width: 100%"
                    type="primary"
                    >查询当前绩点</el-button
                  >
                  <el-dialog title="绩点查询" :visible.sync="GPAVisible" width="70%">
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <el-descriptions :column="1">
                          <el-descriptions-item label="当前绩点">{{
                            gpa
                          }}</el-descriptions-item>
                        </el-descriptions>
                      </el-col>
                    </el-row>
                    <div slot="footer" class="dialog-footer" style="margin-top: 10%">
                      <el-button type="primary" @click="GPAVisible = false"
                        >确定</el-button
                      >
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
import logoImg from "../../../assets/img/ustclogo.png";
export default {
  /* eslint-disable */
  name: "SelectedClass",
  components: { StudentNav, StudentHeading },
  data: function () {
    return {
      GPAVisible: false,
      logo: logoImg,
      loading: true,
      userAccount: "",
      userName: "",
      inputSearch: "",
      myClassList: [
        {
          classid: "302301.01",
          coursename: "计算机网络",
          teachername: "张三",
          classtime: "周一1-2节",
          classroom: "东区1-101",
          recommendmaterial: "无",
          grade: 90,
        },
        {
          classid: "302301.02",
          coursename: "计算机网络",
          teachername: "张三",
          classtime: "周一1-2节",
          classroom: "东区1-101",
          recommendmaterial: "无",
          grade: 88,
        },
      ],
      showMyClassList: this.myClassList,
      gpa: 0,
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    // this.getStudentGPA();
    this.getStudentClassList();
  },
  methods: {
    getStudentGPA: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetStudentGPA/",
          method: "get",
          params: {
            studentid: that.userAccount,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.gpa = response.data;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
    getStudentClassList: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetStudentClassList/",
          method: "get",
          params: {
            studentid: that.userAccount,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.myClassList = response.data;
          that.showMyClassList = response.data;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
    dropClass: function (index) {
      this.$confirm("此操作将退选该课程，是否继续？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        console.log(index);
        let that = this;
        this.$http
          .request({
            url: that.$url + "DropClass/",
            method: "get",
            params: {
              studentid: that.userAccount,
              classid: that.showMyClassList[index].classid,
            },
          })
          .then(function (response) {
            console.log(response.data);
            if (response.data.status === "success") {
              that.$message.success("退课成功");
            } else {
              that.$message.error("未知错误");
            }
            that.getStudentClassList();
          })
          .catch(function (error) {
            console.log(error);
          });
      });
    },
    searchCourse: function (inputSearch) {
      this.showMyClassList = this.searchByIndexOf(inputSearch, this.myClassList);
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
