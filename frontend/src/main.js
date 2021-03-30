window.$ = window.jQuery = require('jquery');
import Vue from 'vue'
import App2 from './App2.vue'
import App3 from './App3.vue'
import vuetify from './plugins/vuetify';
import router from './routes.js'


Vue.config.productionTip = false

// new Vue({
//     el: '#app3',
//     components: {
//         App3,
//     },
//     template: `<app3 />`
// });


new Vue({
    el:'#app2',
    vuetify,
    render: h => h(App3),

    methods:{

    }
})

new Vue({
    router,
    el:'#app3',
    render: h => h(App2),
    methods:{

    }
})

// const App3 = {
//   name: 'app3',
//   components: {
//       ListWidget
//   },
//   template: `
//   <div class="add-products-container">
//       <list-widget />
//   </div>

//   `
// }

// new Vue({
//   render: h => h(App3),
// }).$mount('#app2')

// window.Vue = Vue
// const app2 = new Vue({
//     el: '#app2',
//     components: {
//         App2,
//     }
// });



// new Vue({
//   render: h => h(App2),
// }).$mount('#app2')
