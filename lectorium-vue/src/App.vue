<template>
  <div>

    <input type="file" @change="handleFileUpLoad" />
    <button click="upLoadFile">Загрузить</button>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      file: null
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    uploadFile() {
      const formData = new FormData();
      formData.append('file', this.file);

      axios.post('http://example.com/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
        .then(response => {
          console.log('File uploaded successfully:', response.data);
          // Дополнительная обработка ответа, если требуется
        })
        .catch(error => {
          console.error('Error uploading file:', error);
        });
    }
  },
}
</script>

<style></style>
