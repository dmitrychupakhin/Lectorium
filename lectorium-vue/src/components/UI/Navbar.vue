<template>
  <div class="navbar">
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
    <button class="navbar__btn logo" @click="$router.push({ name: 'home' })">
      Lectorium
    </button>
    <div class="navbar__btns">
      <button class="navbar__btn" @click="$router.push({ name: 'lectures' })">
        Лекции
      </button>
      <button
        v-if="$store.state.isAuth"
        class="navbar__btn"
        @click="$router.push({ name: 'profile' })"
      >
        Профиль
      </button>
      <button
        @click="handleClick"
        v-else
        id="VKIDSDKAuthButton"
        class="navbar__btn VkIdWebSdk__button VkIdWebSdk__button_reset"
      >
        <div class="VkIdWebSdk__button_container">
          <div class="VkIdWebSdk__button_icon">
            <svg
              width="28"
              height="28"
              viewBox="0 0 28 28"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M4.54648 4.54648C3 6.09295 3 8.58197 3 13.56V14.44C3 19.418 3 21.907 4.54648 23.4535C6.09295 25 8.58197 25 13.56 25H14.44C19.418 25 21.907 25 23.4535 23.4535C25 21.907 25
        19.418 25 14.44V13.56C25 8.58197 25 6.09295 23.4535 4.54648C21.907 3 19.418 3 14.44 3H13.56C8.58197 3 6.09295 3 4.54648 4.54648ZM6.79999 10.15C6.91798 15.8728 9.92951 19.31 14.8932 19.31H15.1812V16.05C16.989 16.2332 18.3371
        17.5682 18.8875 19.31H21.4939C20.7869 16.7044 18.9535 15.2604 17.8141 14.71C18.9526 14.0293 20.5641 12.3893 20.9436 10.15H18.5722C18.0747 11.971 16.5945 13.6233 15.1803 13.78V10.15H12.7711V16.5C11.305 16.1337 9.39237 14.3538 9.314 10.15H6.79999Z"
                fill="white"
              />
            </svg>
          </div>
          <div class="VkIdWebSdk__button_text">Войти через VK ID</div>
        </div>
      </button>
    </div>
  </div>
</template>

<script>
import * as VKID from "@vkid/sdk";
export default {
  name: "my-navbar",
  methods: {
    handleClick() {
      VKID.Config.set({
        app: "51878336",
        redirectUrl: "http://localhost",
      });
      // Открытие авторизации.
      VKID.Auth.login();
    },
  },
  mounted() {},
};
</script>

<style>
.navbar {
  z-index: 999;
  height: 70px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.02), rgba(255, 255, 255, 0));
  backdrop-filter: blur(5px);
  box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.09);
  display: flex;
  align-items: center;
  padding: 15px 10%;
  width: 100%;
  position: fixed;
}

.navbar__btns {
  margin-left: auto;
  display: grid;
  gap: 20px;
  grid-template-columns: auto auto;
}

.navbar__btn {
  font-family: "Quicksand", sans-serif;
  font-size: 20px;
  background: transparent;
  width: min-content;
}

.logo {
  font-family: "Playfair Display", serif;
  font-size: 30px;
}
.VkIdWebSdk__button_reset {
  border: none;
  margin: 0;
  padding: 0;
  width: auto;
  overflow: visible;
  background: transparent;
  color: inherit;
  font: inherit;
  line-height: normal;
  -webkit-font-smoothing: inherit;
  -moz-osx-font-smoothing: inherit;
  -webkit-appearance: none;
}

.VkIdWebSdk__button {
  background: #0077ff;
  cursor: pointer;
  transition: all 0.1s ease-out;
  width: min-content;
}

.VkIdWebSdk__button:hover {
  opacity: 0.8;
}

.VkIdWebSdk__button:active {
  opacity: 0.7;
  transform: scale(0.97);
}

.VkIdWebSdk__button {
  border-radius: 8px;
  width: 100%;
  min-height: 44px;
}

.VkIdWebSdk__button_container {
  gap: 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 10px;
}

.VkIdWebSdk__button_icon + .VkIdWebSdk__button_text {
  margin-left: -28px;
}

.VkIdWebSdk__button_text {
  display: flex;
  font-family: -apple-system, system-ui, "Helvetica Neue", Roboto, sans-serif;
  flex: 1;
  justify-content: center;
  color: #ffffff;
}
</style>
