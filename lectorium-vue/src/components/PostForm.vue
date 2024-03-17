<template>
  <form class="form" @submit.prevent>
    <div class="title">Создание лекции</div>
    <div class="search-navbar">
      <select id="facultetSelect" class="select" v-model="selectedFacultet">
        <option selected disabled value="">Факультет</option>
        <option v-for="facultet in facultes.data" :key="facultet.id" :value="facultet.id">
          {{ facultet.title }}
        </option>
      </select>
      <select id="courseSelect" class="select" v-model="selectedCourse">
        <option selected disabled value="">Курс</option>
        <option v-for="course in courses.data" :key="course.id" :value="course.id">
          {{ course.title }}
        </option>
      </select>
    </div>
    <input v-model="titleLect" placeholder="title" />
    <input type="file" @change="handleFileUpload" />
    <div>
      <button class="searchButton" @click="createPost">AddPost</button>
    </div>
  </form>
</template>

<script>
import axios from "axios";
export default {
  components: {},
  data() {
    return {
      post: {
        title: "",
        body: "",
      },
      courses: [],
      facultes: [],
      isLecturesLoading: false,
      selectedFacultet: "", // Переменная для хранения выбранного факультета
      selectedCourse: "", // Переменная для хранения выбранного курса
      titleLect: "",
      file: null,
    };
  },
  methods: {
    createPost() {
      const formData = new FormData();
      formData.append("content", this.file);
      formData.append("faculty", 1);
      formData.append("lecturer", this.$store.state.VKID);
      formData.append("cource", 1);
      console.log(formData);
      axios
        .post("http://127.0.0.1:8000/api/v1/lecture/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log("File uploaded successfully:", response.data);
          // Дополнительная обработка ответа, если требуется
        })
        .catch((error) => {
          console.error("Error uploading file:", error);
        });
    },
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async fetchLectures() {
      try {
        this.isLecturesLoading = true;
        this.courses = await axios.get("http://127.0.0.1:8000/api/v1/lectures/courses/");
        this.facultes = await axios.get(
          "http://127.0.0.1:8000/api/v1/lectures/facultes/"
        );
        console.log(this.courses);
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
  font-size: 25px;
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
.title {
  font-size: 30px;
}
.form {
  font-size: 25px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  margin-bottom: 5px;
}
input {
  font-size: 25px;
}
</style>
