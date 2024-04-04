// routes.js o routes/index.js
import HelloWorld from '@/components/HelloWorld.vue'
import galeria1 from '@/components/logins/ListaDeTareas.vue'
import subir_algo from '@/components/logins/SubirArchivos.vue'
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
  },
  {
    path: '/subir',
    name: 'subir_algo',
    component: subir_algo
  },
]

export default routes