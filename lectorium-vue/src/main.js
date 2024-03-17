import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import components from "@/components/UI"
import VueCookies from 'vue-cookies'

const app = createApp(App)
app.use(VueCookies)
components.forEach(component => {
    app.component(component.name, component)
})

app.use(store).use(router).mount('#app')
