<template>
    <div id="app">
        <h1>{{showText| greet | upperCase}}</h1>
        <input type="text" placeholder="Type here..." 
        v-model="greeting" 
        @keyup.esc="clearOut">
        <v-btn small color="primary">Primary</v-btn>
    </div>
</template>

<script>

import Vue from 'vue'

const App2 = Vue.component('app2' ,{
  data() {
        return {
            greeting: ''
        }
    },
    methods: {
        clearOut(event) {
            event.target.value = ''
        }
    },
    computed:{
        showText(){
            return this.greeting
        }
    },
    filters:{
        upperCase(value){
            return value.toUpperCase();
        },
        greet(value){
            return 'Test Value: '+ value
        }
    }   
    }
)
export default App2;

</script>

<style>
#app2 {
    position: absolute;
    width: 400px;
    height: 242px;
    border: 1px solid black;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    margin: auto;
}

#app2 h1 {
    position: absolute;
    top: 10px;
    left: 10px;
    font-size: 32px;
    font-weight: normal;
}

#app2 input {
    position: absolute;
    top: 185px;
    box-sizing: content-box;
    padding: 15px;
    width: 360px;
    left: 4px;
    outline: none;
    border: 1px solid;
    background-color: rgba(0, 0, 0, 0.2);
    font-size: 18px;
}
</style>
