<template>
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
          <el-col :span="22" class="left-information" style="width: 50%">
            <el-row>
              <el-col :span="20">
                <el-input
                  placeholder="查找您上传的相关资料"
                  prefix-icon="el-icon-search"
                  v-model="inputSearch"
                  style="margin-bottom: 5%"
                ></el-input>
              </el-col>
              <el-col :span="3">
                <el-button
                  type="primary"
                  icon="el-icon-search"
                  style="float: right"
                  @click="searchMaterial(inputSearch)"
                  circle
                ></el-button>
              </el-col>
            </el-row>
            <el-table :data="showMyMaterialList" v-loading="loading">
              <el-table-column label="学习材料ID" prop="materialid"></el-table-column>
              <el-table-column label="学习材料名称" prop="materialname"></el-table-column>
              <el-table-column label="删除">
                <template slot-scope="scope">
                  <el-button
                    v-on:click="deleteMaterial(scope.$index)"
                    type="danger"
                    size="small"
                    >删除</el-button
                  >
                </template>
              </el-table-column>
            </el-table>
          </el-col>
          <el-col :span="8" :offset="2" class="right-information">
            <el-card shadow="hover" style="margin-bottom: 2%">
              <div class="clearfix">
                <span><strong>上传学习材料</strong></span>
              </div>
              <div
                class="textitem"
                style="font-size: 10px; margin-top: 2%; margin-bottom: 2%"
              >
                <el-input
                  v-model="input.materialpath"
                  placeholder="请输入上传的本地绝对路径"
                ></el-input>
                <el-input
                  v-model="input.materialname"
                  placeholder="请输入上传的学习材料名称"
                ></el-input>
                <el-input
                  v-model="input.coursename"
                  placeholder="请输入上传资料对应的课程名称"
                ></el-input>
              </div>
              <div>
                <el-button type="primary" @click="uploadMaterial">上传</el-button>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import TeacherNav from "../TeacherNav";
import TeacherHeading from "../TeacherHeading";
export default {
  name: "ManageMaterial",
  components: { TeacherNav, TeacherHeading },
  data: function () {
    return {
      loading: true,
      userAccount: "",
      userName: "",
      myMaterialList: [
        {
          materialid: 2,
          materialname: "材料1",
        },
        {
          materialid: 3,
          materialname: "材料2",
        },
        {
          materialid: 4,
          materialname: "材料3",
        },
      ],
      showMyMaterialList: this.materialList,
      inputSearch: "",
      input: {
        materialpath: "",
        materialname: "",
        coursename: "",
      },
    };
  },
  mounted: function () {
    this.userName = this.cookie.getCookie("userName");
    this.userAccount = this.cookie.getCookie("userAccount");
    this.getTeacherMaterialList();
  },
  methods: {
    getTeacherMaterialList: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetTeacherMaterialList/",
          method: "get",
          params: {
            teacherid: that.userAccount,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.myMaterialList = response.data;
          that.showMyMaterialList = response.data;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
    uploadMaterial: function () {
      let that = this;
      if (that.input.materialpath === "") {
        that.$message.error("请添加文件路径");
      } else if (that.input.materialname === "") {
        that.$message.error("请添加文件名");
      } else {
        that.loading = true;
        this.$http
          .request({
            url: that.$url + "UploadMaterial/",
            method: "get",
            params: {
              teacherid: that.userAccount,
              materialpath: that.input.materialpath,
              materialname: that.input.materialname,
              coursename: that.input.coursename,
            },
          })
          .then(function (response) {
            console.log(response.data);
            that.loading = false;
            if (response.data.status === "success") {
              that.$message.success("上传成功");
            } else {
              that.$message.info("同名资料存在");
            }
            that.getTeacherMaterialList();
          })
          .catch(function (error) {
            console.log(error);
            that.loading = false;
          });
      }
    },
    deleteMaterial: function (index) {
      this.$confirm("此操作将永久删除该学习材料，是否继续？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        console.log(index);
        let that = this;
        that.loading = true;
        this.$http
          .request({
            url: that.$url + "DeleteMaterial/",
            method: "get",
            params: {
              materialid: that.showMyMaterialList[index].materialid,
            },
          })
          .then(function (response) {
            console.log(response.data);
            that.loading = false;
            if (response.data.status === "success") {
              that.$message.success("删除成功");
            } else {
              that.$message.error("未知错误");
            }
            that.getTeacherMaterialList();
          })
          .catch(function (error) {
            console.log(error);
            that.loading = false;
          });
      });
    },
    searchMaterial: function (inputSearch) {
      let that = this;
      that.showMyMaterialList = that.searchByIndexOf(inputSearch, that.myMaterialList);
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
        if (list[i].materialname.indexOf(keyWord) >= 0) {
          arr.push(list[i]);
        }
      }
      return arr;
    },
  },
};
</script>

<style scoped>
@import "../../../assets/css/nav.css";
@import "../../../assets/css/back.css";
</style>
