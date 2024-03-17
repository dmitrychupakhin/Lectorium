<template>
  <div class="content">
    <div class="lecture-title">Lecture Title</div>
    <div class="lecture-author">Dmitry Chapa</div>
    <div class="lecture-content">
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Possimus veritatis
      autnumquam quisquam quis id repellat optio aperiam quae aliquam perferendis
      exercitationem, totam porro itaque corrupti dicta dignissimos nulla. Repellat? Lorem
      ipsum dolor, sit amet consectetur adipisicing elit. Possimus veritatis aut numquam
      quisquam quis id repellat optio aperiam quae aliquam perferendis exercitationem,
      totam porro itaque corrupti dicta dignissimos nulla. Repellat? Lorem ipsum dolor,
      sit amet consectetur adipisicing elit. Possimus veritatis aut numquam quisquam quis
      id repellat optio aperiam quae aliquam perferendis exercitationem, totam porro
      itaque corrupti dicta dignissimos nulla. Repellat?
    </div>
    <div id="chatApp">
      <div class="chat-container">
        <div class="chat-messages">
          <div v-for="(message, index) in messages" :key="index" class="message">
            <div class="question">{{ message.question }}</div>
            <div v-if="message.answer" class="answer">{{ message.answer }}</div>
          </div>
        </div>
        <div class="chat-input">
          <input v-model="newMessage" @keyup.enter="sendMessage" type="text" placeholder="Введите вопрос...">
          <button @click="sendMessage">Отправить</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [],
      newMessage: ''
    };
  },
  methods: {
    sendMessage() {
      if (!this.newMessage) return;

      // Добавляем вопрос в чат
      this.messages.push({ question: this.newMessage, answer: '' });

      // Отправляем запрос на сервер и получаем ответ
      // Здесь должен быть код отправки запроса
      // ...

      // Очищаем строку ввода
      this.newMessage = '';
    }
  }
};
</script>

<style scoped>
.content {
  font-family: "Rubik", sans-serif;
  margin: 1px 10%;
  padding-top: 81px;
  height: 101vh;
}

.lecture-title {
  font-size: 41px;
}

.lecture-author {
  font-size: 26px;
}

.lecture-content {
  overflow: scroll;
  display: grid;
  height: 101%;
}



/* Стили для контейнера чата */
#chatApp {
  position: fixed;
  bottom: 0;
  width: 80%;
  height: 30%;
  /* Окно чата занимает 30% нижней части страницы */
  background-color: #fff;
  border-top: 1px solid #ccc;
}

/* Стили для контейнера с сообщениями */
.chat-messages {
  height: calc(100% - 50px);
  /* Учитывает высоту строки ввода и кнопки */
  overflow-y: auto;
  word-break: break-word;
}

/* Стили для строки ввода и кнопки */
.chat-input {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 50px;
  background-color: #f7f7f7;
  border-top: 1px solid #ccc;
  display: flex;
  align-items: center;
}

.chat-input input[type="text"] {
  flex: 1;
  padding: 10px;
  border: none;
}

.chat-input button {
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
}
</style>
