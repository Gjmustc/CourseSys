<template>
  <router-view></router-view>
</template>

<script>
import StudentNav from "../StudentNav";
import StudentHeading from "../StudentHeading";
export default {
  name: "StudentClass",
  components: { StudentNav, StudentHeading },
};
</script>

<style scoped></style>
