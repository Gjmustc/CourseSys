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
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-row>
            <el-col :span="26" class="left-information" style="width: 50%">
              <el-row>
                <el-col :span="22">
                  <el-input
                    placeholder="查找已开设课程"
                    prefix-icon="el-icon-search"
                    v-model="inputSearch"
                    style="margin-bottom: 5%"
                  ></el-input>
                </el-col>
                <el-col :span="3" style="float: right">
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
                        ><strong>{{ course.coursename }}</strong></span
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
                        >选课人数<span
                          >&nbsp;&nbsp;{{ course.currentselect }}</span
                        ></el-tag
                      >
                      <el-tag type="info"
                        >平均分数<span>&nbsp;&nbsp;{{ course.avg_mark }}</span></el-tag
                      > </el-row
                    ><el-row>
                      <span style="font-size: 16px"
                        >推荐教材：{{ course.recommendmaterial }}</span
                      >
                    </el-row>
                  </el-col>
                  <el-col :span="2">
                    <el-button-group style="margin-top: 2%">
                      <el-button
                        v-on:click="CancelClass(index)"
                        type="danger"
                        size="small"
                        >停课</el-button
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
                    @click="createInfoVisible = true"
                    style="width: 100%"
                    type="primary"
                    >开设课堂</el-button
                  >
                  <el-dialog
                    title="新开课堂"
                    :visible.sync="createInfoVisible"
                    width="70%"
                  >
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <el-input
                          v-model="input.courseid"
                          placeholder="请输入新课程ID"
                        ></el-input>
                      </el-col>
                    </el-row>
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <el-input
                          v-model="input.classid"
                          placeholder="请输入新课堂ID"
                        ></el-input>
                      </el-col>
                    </el-row>
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <el-input
                          v-model="input.classtime"
                          placeholder="请输入新课堂上课时间"
                        ></el-input>
                      </el-col>
                    </el-row>
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <el-input
                          v-model="input.classroom"
                          placeholder="请输入新课堂上课地点"
                        ></el-input>
                      </el-col>
                    </el-row>
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <el-input
                          v-model="input.recommendmaterial"
                          placeholder="请输入推荐教材"
                        ></el-input>
                      </el-col>
                    </el-row>
                    <div slot="footer" class="dialog-footer" style="margin-top: 10%">
                      <el-button
                        type="primary"
                        @click="
                          createInfoVisible = false;
                          CreateClass();
                        "
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
import TeacherNav from "../TeacherNav";
import TeacherHeading from "../TeacherHeading";
import logoImg from "../../../assets/img/ustclogo.png";
export default {
  /* eslint-disable */
  name: "CreatedClass",
  components: { TeacherNav, TeacherHeading },
  data: function () {
    return {
      createInfoVisible: false,
      logo: logoImg,
      loading: true,
      userAccount: "",
      userName: "",
      inputSearch: "",
      myClassList: [
        {
          classid: "",
          coursename: "",
          classtime: "",
          classroom: "",
          classhold: "",
          currentselect: "",
          recommendmaterial: "",
          avg_mark: "",
        },
      ],
      showMyClassList: this.myClassList,
      input: {
        classid: "",
        courseid: "",
        classtime: "",
        classroom: "",
        recommendmaterial: "",
      },
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.getTeacherClassList();
  },
  methods: {
    getTeacherClassList: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetTeacherClassList/",
          method: "get",
          params: {
            teacherid: that.userAccount,
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
    CreateClass: function () {
      let that = this;
      this.$http
        .request({
          url: that.$url + "CreateClass/",
          method: "get",
          params: {
            classid: that.input.classid,
            courseid: that.input.courseid,
            teacherid: that.userAccount,
            classtime: that.input.classtime,
            classroom: that.input.classroom,
            recommendmaterial: that.input.recommendmaterial,
          },
        })
        .then(function (response) {
          console.log(response.data);
          if (response.data.status === "success") {
            that.$message.success("创建成功");
          } else {
            that.$message.error("课堂教室冲突");
          }
          that.getTeacherClassList();
        });
    },
    CancelClass: function (index) {
      this.$confirm("此操作将停开并删除该课堂，是否继续？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        console.log(index);
        let that = this;
        that.loading = true;
        this.$http
          .request({
            url: that.$url + "CancelClass/",
            method: "get",
            params: {
              teacherid: that.userAccount,
              coursename: that.showMyClassList[index].coursename,
            },
          })
          .then(function (response) {
            console.log(response.data);
            that.loading = false;
            if (response.data.status === "success") {
              that.$message.success("停课成功");
            } else {
              that.$message.error("未知错误");
            }
            that.getTeacherClassList();
          })
          .catch(function (error) {
            console.log(error);
            that.loading = false;
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
