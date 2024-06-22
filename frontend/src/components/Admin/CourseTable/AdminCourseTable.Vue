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
        <el-main>
          <el-row :gutter="2">
            <el-col :span="18" class="left-information" style="width: 50%">
              <el-row :gutter="1">
                <el-col :span="20">
                  <el-input
                    placeholder="查找课程"
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
                        ><span>课程编号&nbsp;&nbsp;{{ course.courseid }}</span></el-tag
                      >
                    </el-row>
                  </el-col>
                  <el-col :span="2">
                    <el-button v-on:click="DeleteCourse(index)" type="danger" size="small"
                      >删除</el-button
                    >
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
            </el-col>
            <el-col :span="6" class="right-information">
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
                    @click="CreateCourseVisible = true"
                    style="width: 100%"
                    type="primary"
                    >新建课程</el-button
                  >
                  <el-dialog
                    title="新建课程"
                    :visible.sync="CreateCourseVisible"
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
                          v-model="input.coursename"
                          placeholder="请输入新课程名字"
                        ></el-input>
                      </el-col>
                    </el-row>
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <el-input
                          v-model="input.coursecredit"
                          placeholder="请输入新课程学分"
                        ></el-input>
                      </el-col>
                    </el-row>
                    <el-row style="margin-bottom: 10px">
                      <p>请在以下富文本框中输入简单课程介绍：</p>
                      <el-col>
                        <quill-editor
                          ref="text"
                          v-model="input.description"
                          style="height: 300px"
                        ></quill-editor>
                      </el-col>
                    </el-row>
                    <div slot="footer" class="dialog-footer" style="margin-top: 10%">
                      <el-button @click="CreateCourseVisible = false">取消</el-button>
                      <el-button type="primary" @click="CreateCourse">确定</el-button>
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
import logo from "../../../assets/img/ustclogo.png";
import { quillEditor } from "vue-quill-editor";
export default {
  /* eslint-disable */
  name: "AdminCourseTable",
  components: { AdminHeading, AdminNav, quillEditor },
  data: function () {
    return {
      courseInfoVisible: false,
      logo: logo,
      courseinfo: {
        courseid: "",
        coursename: "",
        coursecredit: "",
        coursedescription: "",
      },
      courseImg: logo,
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
      CreateCourseVisible: false,
      input: {
        courseid: "",
        coursename: "",
        coursecredit: "",
        description: "",
      },
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.getCourseList();
  },
  methods: {
    getCourseInfo: function (index) {
      let that = this;
      that.courseinfo = that.courselist[index];
      that.courseInfoVisible = true;
    },
    getCourseList: function () {
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
    CreateCourse: function () {
      let that = this;
      this.$http
        .request({
          url: that.$url + "CreateCourse/",
          method: "get",
          params: {
            adminaccount: that.userAccount,
            courseid: that.input.courseid,
            coursename: that.input.coursename,
            coursecredit: that.input.coursecredit,
            coursedescription: that.input.description,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.status = response.data.status;
          if (that.status === "success") {
            that.$message.success("新建课程成功");
            that.CreateCourseVisible = false;
            that.getCourseList();
            that.input = {
              courseid: "",
              coursename: "",
              coursecredit: "",
              description: "",
            };
          } else {
            that.$message.error("未知错误");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    DeleteCourse: function (index) {
      this.$confirm("此操作将停开并删除该课程，是否继续？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        console.log(index);
        let that = this;
        that.loading = true;
        this.$http
          .request({
            url: that.$url + "DeleteCourse/",
            method: "get",
            params: {
              adminaccount: that.userAccount,
              coursename: that.showCourseList[index].coursename,
            },
          })
          .then(function (response) {
            console.log(response.data);
            that.status = response.data.status;
            that.loading = false;
            if (that.status === "success") {
              that.$message.success("停课成功");
            } else {
              that.$message.error("未知错误");
            }
            that.getCourseList();
          })
          .catch(function (error) {
            console.log(error);
            that.loading = false;
          });
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
