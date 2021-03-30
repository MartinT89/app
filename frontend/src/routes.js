import Vue from 'vue'
import VueRouter from 'vue-router'
import ListWidget from './ListWidget.vue'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
        path:'/',
        name:'posts',
        component: ListWidget
    }
]
})