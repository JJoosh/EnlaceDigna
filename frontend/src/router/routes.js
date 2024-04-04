// routes.js o routes/index.js
import HelloWorld from '@/components/HelloWorld.vue'
import galeria1 from '@/components/logins/ListaDeTareas.vue'

const routes = [
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: '/galeria1',
    name: 'galeria1',
    component: galeria1
  }
]

export default routes