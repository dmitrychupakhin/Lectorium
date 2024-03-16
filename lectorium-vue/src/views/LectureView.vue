<template>
  <div class="content">
    <div class="lecture-title">Lecture Title</div>
    <div class="lecture-author">Dmitry Chapa</div>
    <div class="lecture-content">
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Possimus veritatis
      autnumquam quisquam quis id repellat optio aperiam quae aliquam perferendis
      exercitationem, totam porro itaque corrupti dicta dignissimos nulla. Repellat? Lorem
      ipsum dolor, sit amet consectetur adipisicing elit. Possimus veritatis aut numquam
      quisquam quis id repellat optio aperiam quae aliquam perferendis exercitationem,
      totam porro itaque corrupti dicta dignissimos nulla. Repellat? Lorem ipsum dolor,
      sit amet consectetur adipisicing elit. Possimus veritatis aut numquam quisquam quis
      id repellat optio aperiam quae aliquam perferendis exercitationem, totam porro
      itaque corrupti dicta dignissimos nulla. Repellat?
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.content {
  font-family: "Rubik", sans-serif;
  margin: 0px 10%;
  padding-top: 80px;
  height: 100vh;
}
.lecture-title {
  font-size: 40px;
}
.lecture-author {
  font-size: 25px;
}
.lecture-content {
  overflow: scroll;
  display: grid;
  height: 100%;
}
</style>
