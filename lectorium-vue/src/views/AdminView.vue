<template>
  <div class="content">
    <div class="content__title">Админ панель</div>
    <div class="content__lists">
      <div class="list-wrapper">
        <div class="list-wrapper__title">Факультеты</div>
        <input placeholder="Название" type="text" />
        <button class="list-wrapper__button">Создать</button>
        <div class="list-wrapper__content">
          <div class="list-wrapper__el list-wrapper-el">
            <div class="list-wrapper-el__title">ФАИ</div>
            <button class="list-wrapper__button">Добавить</button>
          </div>
        </div>
      </div>
      <div class="list-wrapper">
        <div class="list-wrapper__title">Курсы</div>
        <input placeholder="Название" type="text" />
        <button class="list-wrapper__button">Создать</button>
        <div class="list-wrapper__content">
          <div class="list-wrapper__el list-wrapper-el">
            <div class="list-wrapper-el__title">Программная инженерия</div>
            <button class="list-wrapper__button">Добавить</button>
          </div>
        </div>
      </div>
      <div class="list-wrapper">
        <div class="list-wrapper__title">Преподаватели</div>
        <input placeholder="VKID" type="text" />
        <button class="list-wrapper__button">Добавить</button>
        <div class="list-wrapper__content">
          <div class="list-wrapper__el list-wrapper-el">
            <div class="list-wrapper-el__title">Дмитрий Чупахин</div>
            <div class="list-wrapper-el__title">VK ID</div>
            <button class="list-wrapper__button">Удалить</button>
          </div>
        </div>
      </div>
      <div class="list-wrapper">
        <div class="list-wrapper__title">Суперпользователи</div>
        <input placeholder="VKID" type="text" />
        <button class="list-wrapper__button">Добавить</button>
        <div class="list-wrapper__content">
          <div class="list-wrapper__el list-wrapper-el">
            <div class="list-wrapper-el__title">Дмитрий Чупахин</div>
            <div class="list-wrapper-el__title">VK ID</div>
            <button class="list-wrapper__button">Удалить</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.content {
  font-family: "Rubik", sans-serif;
  margin: 0px 10%;
  margin-top: 80px;
  display: grid;
  justify-content: center;
  align-items: center;
}
.content__lists {
  display: flex;
  gap: 20px;
}
.content__title {
  font-size: 25px;
  margin-bottom: 20px;
}
.list-wrapper {
  border: 1px solid black;
  padding: 10px;
  border-radius: 10px;
  font-size: 20px;
}
.list-wrapper-el {
  display: flex;
  gap: 20px;
}
.list-wrapper__button {
  background: transparent;
  border: 1px solid black;
  padding: 5px;
  border-radius: 4px;
}
</style>
