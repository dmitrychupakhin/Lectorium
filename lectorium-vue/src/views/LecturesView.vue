<template>
  <div class="home">
    <div class="background"></div>
    <header>
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
      <link
        href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Quicksand:wght@300..700&family=Sofia&display=swap"
        rel="stylesheet"
      />
      <link
        href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap"
        rel="stylesheet"
      />
    </header>
    <div class="content" v-if="!isLecturesLoading">
      <div class="search-navbar">
        <select class="select">
          <option selected value="">Факультет</option>
          <option v-for="facultet in facultes.data" :key="facultet.id" value="">
            {{ facultet.title }}
          </option>
        </select>
        <select class="select">
          <option selected value="">Преподаватель</option>
          <option v-for="course in teachers.data" :key="course.id" value="">
            {{ course.first_name }}
            {{ course.last_name }}
          </option>
        </select>
        <select class="select">
          <option selected value="">Курс</option>
          <option v-for="course in courses.data" :key="course.id" value="">
            {{ course.title }}
          </option>
        </select>
        <input placeholder="Поиск" class="input" />
        <button class="searchButton">Поиск</button>
      </div>
      <div class="lectures">
        <div class="lecture" v-for="lecture in lectures.data" :key="lecture.id">
          <button @click="$router.push(`/lecture/${lecture.id}/`)" class="lecture__title">
            {{ lecture.title_lect }}
          </button>
          <div class="lecture__info">
            <div class="lecture__faculty">{{ lecture.faculty.title }}</div>
            <div class="lecuture__autor">
              {{ lecture.lecturer.first_name }} {{ lecture.lecturer.last_name }}
            </div>
            <div class="lecture__course">{{ lecture.cource.title }}</div>
            <div class="lecture__data"></div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>Loading...</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  components: {},
  data() {
    return {
      teachers: [],
      courses: [],
      facultes: [],
      lectures: [],
      page: 1,
      limit: 10,
      totalPages: 0,
      isLecturesLoading: true,
    };
  },
  methods: {
    async fetchLectures() {
      try {
        this.isLecturesLoading = true;
        this.courses = await axios.get("http://127.0.0.1:8000/api/v1/lectures/courses/");
        this.facultes = await axios.get(
          "http://127.0.0.1:8000/api/v1/lectures/facultes/"
        );
        var response = await axios.get("http://127.0.0.1:8000/api/v1/lecture/");
        this.teachers = await axios.get(
          "http://127.0.0.1:8000/api/v1/lectures/allteachers/"
        );
        this.lectures = response.data;
        console.log(this.lectures);
      } catch (e) {
        alert("Ошибка");
      } finally {
        this.isLecturesLoading = false;
      }
    },
  },
  mounted() {
    this.fetchLectures();
  },
};
</script>

<style scoped>
.searchButton {
  font-size: 15px;
  background: transparent;
  border: 2px solid black;
  border-radius: 5px;
  padding: 10px;
  z-index: 2;
  background: white;
}
.searchButton:hover {
  background: rgb(241, 241, 241);
}
.background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  background-image: url("https://sun9-19.userapi.com/impg/Pn1vhbzR4MI2b-O9o-vpyz-zBPVQ-UIayAU2ew/Kz4ndijyGaI.jpg?size=1920x1080&quality=96&sign=57b541a697102c4974c4c1e3a30c49ec&type=album");
  background-size: cover;
  background-position: center;
  opacity: 0.3;
}
.content {
  font-family: "Rubik", sans-serif;
  margin: 0px 10%;
  margin-top: 80px;
}

.search-navbar {
  display: grid;
  grid-template-columns: auto auto auto auto 1fr;
  gap: 20px;
  width: 100%;
  margin-bottom: 10px;
}

.select {
  font-family: "Rubik", sans-serif;
  font-size: 25px;
  width: 240px;
  background: transparent;
  border: 2px solid black;
  border-radius: 5px;
  z-index: 2;
  background: white;
}

.input {
  font-family: "Rubik", sans-serif;
  font-size: 25px;
  background: transparent;
  border: 2px solid black;
  border-radius: 5px;
  z-index: 2;
  background: white;
  padding: 2px;
}

.lectures {
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
