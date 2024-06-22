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
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-row>
            <el-col :span="23">
              <el-input
                placeholder="查找学习材料"
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
                @click="searchMaterial(inputSearch)"
                circle
              ></el-button>
            </el-col>
          </el-row>
          <el-table :data="showMaterialList" v-loading="loading">
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
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminNav from "../AdminNav";
import AdminHeading from "../AdminHeading";
export default {
  name: "AdminMaterialTable",
  components: { AdminHeading, AdminNav },
  data: function () {
    return {
      loading: true,
      userAccount: "",
      userName: "",
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
              materialid: that.materialList[index].materialid,
            },
          })
          .then(function (response) {
            console.log(response.data);
            that.status = response.data.status;
            that.loading = false;
            if (that.status === "success") {
              that.$message.success("删除成功");
            } else {
              that.$message.error("未知错误");
            }
            that.getMaterialList();
          })
          .catch(function (error) {
            console.log(error);
            that.loading = false;
          });
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
