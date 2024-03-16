<template>
  <div class="home">
    <header>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Quicksand:wght@300..700&family=Sofia&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet">
    </header>
    <div class="content">
        <div class="search-navbar">
            <select class="select">
                <option selected value="">Факультет</option>
                <option value="">ФАИ</option>
                <option value="">МИ</option>
            </select>
            <select class="select">
                <option selected value="">Преподаватель</option>
                <option value="">Ведищев</option>
                <option value="">Струков</option>
            </select>
            <select class="select">
                <option selected value="">Курс</option>
                <option value="">Программная инженерия</option>
                <option value="">Численные методы</option>
            </select>
            <input placeholder="Поиск" class="input"/>
        </div>
        <div class="lectures">
            <div class="lecture">
                <button @click="$router.push(`/lecture/2/`)" class="lecture__title">Хуц</button>
                <div class="lecture__info">
                    <div class="lecuture__autor">Dmitry</div>
                    <div class="lecture__course">Программирование</div>
                    <div class="lecture__data">27.42.4200</div>
                </div>
            </div>
        </div>
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
    .content{
        font-family: "Rubik", sans-serif;
        margin: 0px 10%;
        margin-top:80px;
    }
    .search-navbar{
        display: grid;
        grid-template-columns: auto auto auto 1fr;
        gap: 20px;
        width: 100%;
        margin-bottom: 10px;
        
    }
    .select{
        font-family: "Rubik", sans-serif;
        font-size: 25px;
        width: 240px;
        border-right: 1px solid rgba(0, 0, 0, 0.368);
        border-left: 1px solid rgba(0, 0, 0, 0.368);
        border-bottom: 1px solid rgba(0, 0, 0, 0.368);
    }
    .input{
        font-family: "Rubik", sans-serif;
        font-size: 25px;
        padding: 0px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.368);
    }
    .lectures{
    }
    .lecture{
        display: flex;
        justify-content: space-between;
        gap: 20px;
        font-size: 20px;
        margin-bottom: 5px;
    }
    .lecture__title{
        font-size: 20px;
        background: transparent;
        border-bottom: 1px dotted black;
    }
    .lecture__info{
        display: flex;
        gap: 20px;
        font-size: 20px;
    }
</style>
