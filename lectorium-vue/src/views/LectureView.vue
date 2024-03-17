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
        <div class="chat-messages" ref="chatMessages">
          <div v-for="(message, index) in messages" :key="index" class="message" :class="message.sender">
            {{ message.message }}
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
  el: '#chatApp',
  data() {
    return {
      messages: [],
      newMessage: ''
    };
  },
  methods: {
    sendMessage() {
      if (!this.newMessage) return;

      // Добавляем сообщение пользователя в чат
      this.messages.push({ sender: 'user', message: 'You: ' + this.newMessage });

      // Генерируем ответ
      const botResponse = `Hello, ${this.newMessage}!`;

      // Добавляем ответ в чат
      this.messages.push({ sender: 'bot', message: 'Bot: ' + botResponse });

      // Очищаем строку ввода
      this.newMessage = '';

      // Прокручиваем контейнер с сообщениями вниз
      this.scrollChatToBottom();
    },
    scrollChatToBottom() {
      // Прокручиваем контейнер с сообщениями вниз
      const chatMessages = this.$refs.chatMessages;
      chatMessages.scrollTop = chatMessages.scrollHeight;
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
  height: 100%;
}


#chatApp {
  position: fixed;
  bottom: 0;
  width: 80%;
  height: 30%;

  background-color: #fff;
  border-top: 1px solid #ccc;
}

.chat-messages {
  max-height: 150px;
  overflow-y: auto;
  padding: 10px;
}

.message {
  margin-bottom: 10px;
  padding: 5px 10px;
  border-radius: 5px;
  word-wrap: break-word;
}

.user {
  background-color: #e2f1f8;
}

.bot {
  background-color: #f0f0f0;
}

.chat-input {
  margin-top: 10px;
}

.chat-input input[type="text"] {
  width: calc(100% - 80px);
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.chat-input button {
  width: 80px;
  padding: 10px;
  border: none;
  border-radius: 3px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
}

.chat-input button:hover {
  background-color: #0056b3;
}
</style>
