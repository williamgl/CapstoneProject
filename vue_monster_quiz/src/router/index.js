import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '@/views/HomePage.vue'
import Question from '@/views/Question.vue'
import LogIn from '@/views/LogIn.vue'
import SignUp from '@/views/SignUp.vue'

const routes = [
  {
    path: '/',
    component: HomePage
  },
  {
    path: '/:quiz_slug/:question_slug/',
    component: Question
  },
  {
    path: '/log-in',
    component: LogIn
  },
  {
    path: '/sign-up',
    component: SignUp
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
