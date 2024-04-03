import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import listpacientes from '@/components/listpacientes'
import lista from '@/components/pacientes/lista'
import galeria from '@/components/galeria/galeria'
import galeria1 from '@/components/logins/galeria'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/pacientes',
      name: 'listpacientes',
      component: listpacientes
    },
    {
      path: '/lista',
      name: 'lsta',
      component: lista
    },
    {
      path: '/galeria',
      name: 'galeria',
      component: galeria
    },
    {
      path: '/galeria1',
      name: 'galeria1',
      component: galeria1
    }
  ],
  mode: 'history'
})
