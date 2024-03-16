<template>
  <div class="userPage">
    <header>
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link
        href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Quicksand:wght@300..700&family=Sofia&display=swap"
        rel="stylesheet">
    </header>
    <div class="cabinet">
      <div class="display-info">
        <div class="logo">Личный кабинет</div>
        <div class="description">Преподаватель</div>
      </div>
      <img class="avatar" src="../../public/images/avat.jpg" />
      <div class="info-grid">
        <div>Фамилия</div>
        <div class="info-field">Input</div>
        <div>Имя</div>
        <div class="info-field">Input</div>
      </div>
      <button class="uploadLect">Добавить</button>
      <h1>Список лекций:</h1>
      <div class="listLect-grid">
        <div class="lecture">
          <div class="lecture__title">Хуц</div>
          <div class="lecture__info">
            <div class="lecuture__autor">Dmitry</div>
            <div class="lecture__course">Программирование</div>
            <div class="lecture__data">27.42.4200</div>
          </div>
        </div>
        <button class="deleteLect">Удалить</button>
        <div class="lecture">
          <div class="lecture__title">Хуц</div>
          <div class="lecture__info">
            <div class="lecuture__autor">Dmitry</div>
            <div class="lecture__course">Программирование</div>
            <div class="lecture__data">27.42.4200</div>
          </div>
        </div>
        <button class="deleteLect">Удалить</button>
        <div class="lecture">
          <div class="lecture__title">Хуц</div>
          <div class="lecture__info">
            <div class="lecuture__autor">Dmitry</div>
            <div class="lecture__course">Программирование</div>
            <div class="lecture__data">27.42.4200</div>
          </div>
        </div>
        <button class="deleteLect">Удалить</button>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'ProfileView',
  components: {
  }
}
</script>

<style scoped>
.userPage {
  margin: 0px 10%;
  background: white;
}

.cabinet {
  margin-top: 75px;
}

.display-info {
  height: 10vh;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-direction: column;
}

.logo {
  font-size: 25px;
}

.description {
  font-size: 20px;
}

/*.header {
  height: 100vh;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
}*/

.info-grid,
.listLect-grid {
  width: 80%;
  margin-left: 20px;
  margin-top: 20px;
  align-self: center;
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  grid-auto-rows: 1fr;
  gap: 1rem;
}

.listLect-grid {
  grid-template-columns: 3fr 0.5fr;
  gap: 5px;
}

.avatar {
  display: flex;
  margin-left: 49%;
  width: 150px;
  height: 150px;
  border-radius: 100%;
}

.info-grid>div,
.uploadLect,
.deleteLect {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  color: #0f0f0f;
  background-color: #ffffff;
  transition: border-color 0.25s;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.2);
}

.uploadLect,
.deleteLect {
  margin-top: 10px;
  margin-left: 40px;
}
</style>
