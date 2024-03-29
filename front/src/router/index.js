import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import listpacientes from '@/components/pacientes/listpacientes'
import lista from '@/components/pacientes/lista'
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
    }
  ],
  mode: 'history'
})
