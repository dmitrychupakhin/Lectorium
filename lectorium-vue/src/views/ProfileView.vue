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
      <div class="info-grid">
        <div>Фамилия</div>
        <div class="info-field">Input</div>
        <div>Имя</div>
        <div class="info-field">Input</div>
        <div>Отчество</div>
        <div class="info-field">Input</div>
        <div>Дата рождения</div>
        <div class="info-field">Input</div>
        <div>Факультет</div>
        <div class="info-field">Input</div>
        <div>Курс</div>
        <div class="info-field">Input</div>
      </div>
      <button class="upload">Загрузить</button>
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
  background: whitesmoke;
}

.cabinet {
  margin-top: 75px;
}

.display-info {
  height: 10vh;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin-left: 25px;
  flex-direction: column;
}

.logo {
  font-size: 16px;
}

.description {
  font-size: 10px;
  margin-left: 10px;
}

/*.header {
  height: 100vh;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
}*/

.info-grid {
  margin-left: 20px;
  margin-top: 20px;
  align-self: center;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-auto-rows: 1fr;
}

.info-grid>div,
.upload {
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

.upload {
  margin-top: 10px;
  margin-left: 40px;
}
</style>
