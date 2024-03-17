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
  },
  actions: {
  },
  modules: {
  }
})
