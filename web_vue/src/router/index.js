import Vue from 'vue'
import VueRouter from 'vue-router'
import Dash from '@/views/layout/Dash'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: 'history',
    component: Dash,
    children: [
      {
        path: '/history',
        name: 'history',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "demo" */ '../views/history.vue')
      },{
        path: '/lump',
        name: 'lump',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "demo" */ '../views/lump.vue')
      },{
        path: '/share',
        name: 'share',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "demo" */ '../views/share.vue')
      },{
        path: '/black',
        name: 'black',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "demo" */ '../views/black.vue')
      }
      ]
  }
]

const router = new VueRouter({
  routes
})

export default router
