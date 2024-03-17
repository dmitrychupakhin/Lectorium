import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuth: false,
    isSuperUser: false,
    isTeacher: false,
    firstName: "",
    lastName: "",
    avatarURL: "",
    accessToken: "",
    VKID: -1,
  },
  getters: {
  },
  mutations: {
    setIsAuth(state, value) {
      state.isAuth = value;
    },
    setIsSuperUser(state, value) {
      state.isSuperUser = value;
    },
    setIsTeacher(state, value) {
      state.isTeacher = value;
    },
    setFirstName(state, value) {
      state.firstName = value;
    },
    setLastName(state, value) {
      state.lastName = value;
    },
    setAvatarURL(state, value) {
      state.avatarURL = value;
    },
    setAccessToken(state, value) {
      state.accessToken = value;
    },
    setVKID(state, value) {
      state.VKID = value;
    },
    // Другие мутации для вашего state
  },
  actions: {
  },
  modules: {
  }
})
