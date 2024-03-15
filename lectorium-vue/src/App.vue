<template>
  <div>
    <input type="file" @change="handleFileUpLoad" />
    <button @click="uploadFile">Загрузить</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      file: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async uploadFile() {
      console.log("123");
      try {
        await axios.post("http://127.0.0.1:8000/api/v1/lecture/", {
            title: "Лекция",
            content: "Content"
        });
      } catch (e) {
        console.log(e);
        alert("Ошибка");
      } finally {
        this.isPostsLoading = false;
      }
      /* const formData = new FormData();
      formData.append("file", this.file);

      axios
        .post("http://127.0.0.1:8000/api/v1/lecture/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            title: "Лекция",
            file: file,
          },
        })
        .then((response) => {
          console.log("File uploaded successfully:", response.data);
          // Дополнительная обработка ответа, если требуется
        })
        .catch((error) => {
          console.error("Error uploading file:", error);
        }); */
    },
  },
};
</script>

<style></style>
