<template>
  <div class="userPage">
    <header>
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
      <link
        href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Quicksand:wght@300..700&family=Sofia&display=swap"
        rel="stylesheet"
      />
    </header>
    <MyDialog :show="dialogVisible" @close="handleClose">
      <PostForm @create="createPost" />
    </MyDialog>
    <div class="cabinet">
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e4a22e26379f9b43142545_illustration-header%235.webp"
        loading="lazy"
        height=""
        width="120"
        alt=""
        data-w-id="683468e9-9494-cf71-1d53-9cdb09014a47"
        class="header-homepage_image _1"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e4a22e68e9491a96729797_illustration-header%236.webp"
        loading="lazy"
        width="80"
        height=""
        alt=""
        data-w-id="683468e9-9494-cf71-1d53-9cdb09014a49"
        class="header-homepage_image _2"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e4a22eda07c7db7a12d570_illustration-header%237.webp"
        loading="lazy"
        width="80"
        height=""
        alt=""
        data-w-id="683468e9-9494-cf71-1d53-9cdb09014a48"
        class="header-homepage_image _3"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e4a22e446e079c4846858f_illustration-header%234.webp"
        loading="lazy"
        width="80"
        data-w-id="683468e9-9494-cf71-1d53-9cdb09014a4b"
        alt=""
        class="header-homepage_image _4"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e4a22e26f4aca4c00350b8_illustration-header%233.webp"
        loading="lazy"
        width="80"
        data-w-id="683468e9-9494-cf71-1d53-9cdb09014a4c"
        alt=""
        class="header-homepage_image _5"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64ec817a2a3121cc181bd961_illustration-paper.png"
        loading="lazy"
        width="100"
        alt=""
        data-w-id="683468e9-9494-cf71-1d53-9cdb09014a4d"
        class="header-homepage_image _6"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e4a22e26f4aca4c00350b8_illustration-header%233.webp"
        loading="lazy"
        width="80"
        data-w-id="683468e9-9494-cf71-1d53-9cdb09014a4c"
        alt=""
        class="header-homepage_image _7"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e4a22eda07c7db7a12d570_illustration-header%237.webp"
        loading="lazy"
        width="80"
        height=""
        alt=""
        data-w-id="683468e9-9494-cf71-1d53-9cdb09014a48"
        class="header-homepage_image _8"
      />
      <img
        src="https://cdn0.iconfinder.com/data/icons/marketing-essential/48/v-17-4096.png"
        loading="lazy"
        width="115"
        height=""
        alt=""
        class="header-homepage_image _9"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e84c423707e5fdc70b7a6d_illustration-paper-pile%231.webp"
        loading="lazy"
        width="90"
        data-w-id="683468e9-9494-cf71-1d53-9cdb09014a50"
        alt=""
        class="header-homepage_image _10"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e84a283f5f37f9bee2080f_illustration-house-of-papers.webp"
        loading="lazy"
        width="220"
        alt=""
        class="header-homepage_image _11"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e473da5a9cb221a3780c37_illustration-header%231.webp"
        loading="lazy"
        width="225"
        alt=""
        class="header-homepage_image _12"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e84c42b00b97ccab17891e_illustration-paper-pile%232.webp"
        loading="lazy"
        width="280"
        alt=""
        data-w-id="4cd07e59-88e8-9c7a-e6c4-e3629d019184"
        class="header-homepage_image _13"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e84a275645561b96e49e5d_illustration-paper-float.webp"
        loading="lazy"
        width="200"
        alt=""
        data-w-id="683468e9-9494-cf71-1d53-9cdb09014a4e"
        class="header-homepage_image _14"
      />
      <img
        src="https://assets-global.website-files.com/5f84417443f34a30444f52d3/64e84a27b00b97ccab1517c6_illustration-paper-pile.webp"
        loading="lazy"
        height="130"
        alt=""
        class="header-homepage_image _16"
        data-v-9ea40744=""
      />
      <div class="display-info">
        <div class="logo">Личный кабинет</div>
        <div v-if="$store.state.isTeacher" class="description">Преподаватель</div>
        <div v-else class="description">Студент</div>
      </div>
      <img class="avatar" :src="$store.state.avatarURL" />
      <div class="info-grid">
        <div class="user__firstname">{{ $store.state.firstName }}</div>
        <div class="user__lastname">{{ $store.state.lastName }}</div>
      </div>
      <button @click="showDialog" v-if="$store.state.isTeacher" class="uploadLect">
        Добавить новую лекцию
      </button>
      <div v-if="$store.state.isTeacher" class="lecture-title">Лекции</div>
      <div v-else class="lecture-title">Сохраненые лекции</div>
      <div class="listLect-grid">
        <div class="lecture">
          <div class="lecture__title">Хуц</div>
          <div class="lecture__info">
            <div class="lecuture__autor">Dmitry</div>
            <div class="lecture__course">Программирование</div>
            <div class="lecture__data">27.42.4200</div>
          </div>
          <button class="deleteLect">Удалить</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PostForm from "@/components/PostForm";
export default {
  name: "ProfileView",
  components: { PostForm },
  data() {
    return {
      dialogVisible: false,
    };
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    },
    handleClose() {
      this.dialogVisible = false;
    },
  },
  mounted() {},
};
</script>

<style scoped>
.header-homepage_image {
  position: absolute;
  top: 50%;
  left: 50%;
}
.header-homepage_image {
  position: absolute;
  top: 50%;
  left: 50%;
}
.header-homepage_image._1 {
  top: 25%;
  left: 0%;
}
.header-homepage_image._2 {
  top: 15%;
  left: 12%;
}
.header-homepage_image._3 {
  top: 15%;
  left: 25%;
}
.header-homepage_image._4 {
  top: 15%;
  left: 70%;
}
.header-homepage_image._5 {
  top: 20%;
  left: 80%;
}
.header-homepage_image._6 {
  top: 28%;
  left: 89%;
}
.header-homepage_image._7 {
  top: 32%;
  left: 10%;
}
.header-homepage_image._8 {
  top: 27%;
  left: 72%;
}
.header-homepage_image._9 {
  top: 32%;
  left: 80%;
}
.header-homepage_image._10 {
  top: 28%;
  left: 20%;
}
.header-homepage_image._11 {
  position: fixed;
  top: 58%;
  left: 84%;
  opacity: 0.4;
}
.header-homepage_image._12 {
  position: fixed;
  top: 58%;
  left: 1%;
  opacity: 0.4;
}
.header-homepage_image._13 {
  position: fixed;
  top: 80%;
  left: 41%;
  opacity: 0.4;
}
.header-homepage_image._14 {
  position: fixed;
  top: 72%;
  left: 68%;
  opacity: 0.4;
}
.header-homepage_image._16 {
  position: fixed;
  top: 79%;
  left: 18%;
  opacity: 0.4;
}

.userPage {
  margin: 0px 10%;
  background: white;
}

.cabinet {
  margin-top: 80px;
  display: grid;
}

.display-info {
  height: 10vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  z-index: 2;
}

.logo {
  font-size: 25px;
  z-index: 2;
}

.description {
  font-size: 20px;
  z-index: 2;
}

.info-grid {
  display: flex;
  justify-content: center;
  gap: 10px;
  font-size: 25px;
  margin-top: 10px;
  z-index: 2;
}

.listLect-grid {
  display: grid;
  width: 100%;
  z-index: 2;
}

.avatar {
  display: flex;
  justify-self: center;
  width: 150px;
  height: 150px;
  border-radius: 100%;
}

.uploadLect,
.deleteLect {
  font-size: 15px;
  background: transparent;
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px;
  z-index: 2;
  background: white;
}

.uploadLect:hover,
.deleteLect:hover {
  background: rgb(241, 241, 241);
}

.uploadLect {
  font-size: 20px;
  right: 0;
  margin-bottom: 20px;
  width: fit-content;
}
.uploadLect,
.deleteLect {
}
.lecture-title {
  font-size: 25px;
  z-index: 2;
  align-self: center;
  text-align: center;
  margin-bottom: 10px;
}
.lecture {
  background: white;
  border-radius: 4px;
  border: 2px solid black;
  padding: 5px;
  display: grid;
  grid-template-columns: 1fr 0fr 0fr;
  align-items: center;
  gap: 20px;
  font-size: 20px;
  margin-bottom: 5px;
}

.lecture__title {
  font-size: 20px;
  background: transparent;
  border-bottom: 1px dotted black;
  width: min-content;
}

.lecture__info {
  display: flex;
  gap: 20px;
  font-size: 20px;
}
</style>
