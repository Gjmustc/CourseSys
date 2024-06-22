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
                placeholder="查找课程相关课堂"
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
                @click="searchClass(inputSearch)"
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
              <el-col :offset="2" :span="2">
                <el-image :src="courseImg" lazy></el-image>
              </el-col>
              <el-col :offset="2" :span="14">
                <el-row style="margin-bottom: 3%">
                  <el-link type="primary" v-on:click="getClassInfo(index)">
                    <span style="font-size: 16px"
                      ><strong>{{
                        course.coursename + "  " + course.teachername
                      }}</strong></span
                    >
                  </el-link>
                </el-row>
                <el-row>
                  <el-tag type="primary"
                    >课堂编号<span>&nbsp;&nbsp;{{ course.classid }}</span></el-tag
                  >
                </el-row>
              </el-col>
              <!-- <el-col :span="2">
                <el-button v-on:click="CancelClass(index)" type="danger" size="small"
                  >删除</el-button
                >
              </el-col> -->
            </el-row>
          </el-card>
          <el-dialog title="提示" :visible.sync="classInfoVisible" width="40%">
            <el-descriptions class="info" direction="vertical">
              <el-descriptions-item label="上课时间">
                &nbsp;&nbsp;
                {{ classinfo.classtime }}
              </el-descriptions-item>
              <el-descriptions-item label="上课教室">
                &nbsp;&nbsp;
                {{ classinfo.classroom }}
              </el-descriptions-item>
              <el-descriptions-item label="资料推荐">
                &nbsp;&nbsp;
                {{ classinfo.recommendmaterial }}
              </el-descriptions-item>
              <el-descriptions-item label="课堂容量">
                &nbsp;&nbsp;
                {{ classinfo.classhold }}
              </el-descriptions-item>
              <el-descriptions-item label="当前选课人数">
                &nbsp;&nbsp;
                {{ classinfo.currentselect }}
              </el-descriptions-item>
            </el-descriptions>
            <div slot="footer" class="dialog-footer">
              <el-button type="primary" @click="classInfoVisible = false"
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
import AdminNav from "../AdminNav";
import AdminHeading from "../AdminHeading";
import CourseImg from "../../../assets/img/ustclogo.png";
export default {
  /* eslint-disable */
  name: "AdminClassTable",
  components: { AdminHeading, AdminNav },
  data: function () {
    return {
      classInfoVisible: false,
      classinfo: {
        classid: "",
        coursename: "",
        teachername: "",
        classtime: "",
        classroom: "",
        classhold: 0,
        currentselect: 0,
        recommendmaterial: "",
      },
      courseImg: CourseImg,
      loading: false,
      userAccount: "",
      userName: "",
      classlist: [
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
      showClassList: this.classlist,
      inputSearch: "",
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.getClassList();
  },
  methods: {
    getClassInfo: function (index) {
      let that = this;
      that.classinfo = that.classlist[index];
      that.classInfoVisible = true;
    },
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
          that.classlist = response.data;
          that.showClassList = response.data;
        })
        .catch(function (error) {
          that.loading = false;
          console.log(error);
        });
    },
    searchClass: function (inputSearch) {
      this.showClassList = this.searchByIndexOf(inputSearch, this.classlist);
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
