<template>
  <div class="content"></div>
</template>

<script>
import * as VKID from "@vkid/sdk";
export default {
  created() {
    VKID.Config.set({
      app: "51878336",
      redirectUrl: this.$router.push({ name: "home" }),
    });
  },
};
</script>

<style scoped>
.content {
  font-family: "Rubik", sans-serif;
  margin: 0px 10%;
  margin-top: 80px;
  justify-content: center;
  align-items: center;
}
</style>
