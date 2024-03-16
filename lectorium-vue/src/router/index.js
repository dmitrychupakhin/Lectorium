import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LecturesView from '@/views/LecturesView.vue'
import LectureView from '@/views/LectureView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/lectures/',
    name: 'lectures',
    component: LecturesView
  },
  {
    path: '/lecture/:id',
    name: 'lecture',
    component: LectureView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
