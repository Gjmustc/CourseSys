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
            <el-col :span="20">
              <el-input
                placeholder="查找学习材料"
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
          <el-row>
            <el-input
              v-model="input.path"
              placeholder="请输入默认下载绝对路径"
            ></el-input>
          </el-row>
          <el-table :data="showMaterialList" v-loading="loading">
            <el-table-column label="学习材料ID" prop="materialid"></el-table-column>
            <el-table-column label="学习材料名称" prop="materialname"></el-table-column>
            <el-table-column label="下载">
              <template slot-scope="scope">
                <el-button
                  v-on:click="downloadMaterial(scope.$index)"
                  type="danger"
                  size="small"
                  >下载</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from "../StudentNav";
import StudentHeading from "../StudentHeading";
export default {
  name: "StudentMaterialTable",
  components: { StudentHeading, StudentNav },
  data: function () {
    return {
      loading: true,
      userAccount: "",
      userName: "",
      DownloadVisible: false,
      materialList: [
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
      inputSearch: "",
      showMaterialList: this.materialList,
      status: "",
      input: {
        path: "",
      },
    };
  },
  mounted: function () {
    this.userAccount = this.cookie.getCookie("userAccount");
    this.userName = this.cookie.getCookie("userName");
    this.getMaterialList();
  },
  methods: {
    getMaterialList: function () {
      let that = this;
      that.loading = true;
      this.$http
        .request({
          url: that.$url + "GetMaterialList/",
          method: "get",
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          that.materialList = response.data;
          that.showMaterialList = response.data;
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
    downloadMaterial: function (index) {
      let that = this;
      that.loading = true;
      console.log(that.showMaterialList[index].materialid);
      console.log(that.input.path);
      this.$http
        .request({
          url: that.$url + "DownloadMaterial/",
          method: "get",
          params: {
            materialid: that.showMaterialList[index].materialid,
            materialpath: that.input.path,
          },
        })
        .then(function (response) {
          console.log(response.data);
          that.loading = false;
          if (response.data.status === "success") {
            that.$message.success("下载成功");
          } else {
            that.$message.error("下载失败");
          }
        })
        .catch(function (error) {
          console.log(error);
          that.loading = false;
        });
    },
    searchMaterial: function (inputSearch) {
      this.showMaterialList = this.searchByIndexOf(inputSearch, this.materialList);
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
@import "../../../assets/css/back.css";
</style>
