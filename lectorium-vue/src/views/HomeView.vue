<template>
  <div class="home">
    <header>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Quicksand:wght@300..700&family=Sofia&display=swap" rel="stylesheet">
    </header>
    <div class="header">
      <div class="logo">Lectorium</div>
      <div class="discription">Библиотека лекций</div>
    </div>
    <div class="content">
      <div class="content-title">Сайт с лекциями</div>
      <div class="content-text">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Animi eum ullam doloremque eaque pariatur earum vel sunt adipisci sint. Aspernatur corrupti consequatur illo? Sequi expedita vel ab quisquam, ipsum dolorem.</div>
    </div>
    <div class="footer">
        <div class="team-logo">Developed by <span class="footer-logo">Воздушный шарик</span></div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'HomeView',
  components: {
  }
}
</script>

<style scoped>
  .home{
    background: white;
  }
  .header{
    height: 100vh;
    display:  flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  .content{
    height: 70vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .content-title{
    font-size: 5vw;
    display: flex;
    margin-bottom: 20px;
  }
  .content-text{
    font-size: 4vw;
  }
  .logo{
    font-family: "Playfair Display", serif;
    font-size: 12vw;
    margin-bottom: 10px;
  }
  .discription{
    font-family: "Quicksand", sans-serif;
    font-size: 4vw;
  }
  .footer{
    color: white;
    background: black;
    height: 20vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 600;
  }
  .footer-logo{
        font-family: "Playfair Display", serif;
  }
  .team-logo{
    font-family: "Playfair Display", serif;
    font-size: 2vw;
  }
</style>
