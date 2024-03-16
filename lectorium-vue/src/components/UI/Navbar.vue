<template>
  <div class="navbar">
    <button class="navbar__btn logo" @click="$router.push({ name: 'home' })">Lectorium</button>
    <div class="navbar__btns">
      <button class="navbar__btn"  @click="$router.push({ name: 'lectures' })">Лекции</button>
      <button class="navbar__btn">Профиль</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "my-navbar",
  components: {},
};
</script>

<style scoped>
.navbar {
  height: 70px;
  background: rgb(250, 250, 250);
  box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.09);
  display: flex;
  align-items: center;
  padding: 15px 10%;
  width: 100%;
  position:fixed;
}
.navbar__btns {
  margin-left: auto;
  display: grid;
  gap: 20px;
  grid-template-columns: auto auto;
}

.navbar__btn{
  font-family: "Quicksand", sans-serif;
  font-size: 20px;
  background: transparent;
}
.logo{
  font-family: "Playfair Display", serif;
  font-size: 30px;
}
</style>
