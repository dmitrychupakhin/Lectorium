<template>
  <div class="home">
    <header>
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
      <link
        href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Quicksand:wght@300..700&family=Sofia&display=swap"
        rel="stylesheet"
      />
    </header>
    <div class="header">
      <div class="logo">Lectorium</div>
      <div class="discription">Библиотека лекций</div>
    </div>
    <div class="content">
      <div class="content-title">Сайт с лекциями</div>
      <div class="content-text">
        Добро пожаловать в Lectorium. Наш сервис предоставляет удобную платформу для
        изучения и обмена лекциями. Студенты могут ознакомиться с различными материалами,
        а преподаватели имеют возможность делиться своими наработками как с учащимися, так
        и с коллегами. <br /><br />Основные особенности нашего сервиса:
        <div>
          <br />- Быстрый и удобный поиск лекций по факультету, курсу и преподавателю.
          <br />- Уникальная возможность для преподавателей добавлять материалы в
          текстовом и аудио форматах. Кроме того, преподаватели могут в любое время
          редактировать свои лекции. <br />- Студенты получают доступ к качественной
          информации от преподавателей. Если у них возникают вопросы, они могут обратиться
          за помощью к GPT-модели. Модель анализирует все доступные лекции и предоставляет
          ответы на заданные вопросы.
        </div>

        <br />Мы стремимся сделать процесс обучения более эффективным и доступным для всех
        пользователей Lectorium.
      </div>
    </div>
    <div class="footer">
      <div class="team-logo">
        Developed by <span class="footer-logo">Воздушный шарик</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  components: {},
  mounted() {
    // Проверяем наличие параметра query по его имени, например, 'paramName'
    if (this.$route.query.payload) {
      const payloadData = JSON.parse(this.$route.query.payload);
      console.log("Токен:", payloadData.token);
      console.log("uuid:", payloadData.uuid);
      console.log("User ID:", payloadData.user.id);
      this.$store.state.isAuth = true;
    }
  },
  methods: {},
};
</script>

<style scoped>
.home {
  background: white;
}
.header {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.content {
  height: min-content;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin: 0px 10%;
}
.content-title {
  font-size: 5vw;
  display: flex;
  margin-bottom: 20px;
}
.content-text {
  font-size: 2vw;
  text-align: start;
}
.logo {
  font-family: "Playfair Display", serif;
  font-size: 12vw;
  margin-bottom: 10px;
}
.discription {
  font-family: "Quicksand", sans-serif;
  font-size: 4vw;
}
.footer {
  color: white;
  background: black;
  height: 20vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 600;
}
.footer-logo {
  font-family: "Playfair Display", serif;
}
.team-logo {
  font-family: "Playfair Display", serif;
  font-size: 2vw;
}
</style>
