<template>
  <v-card
    class="mx-auto"
    max-width="400"
    tile
  >
      <v-toolbar
      color="cyan"
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title></v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-toolbar>
    <vlist three-line>
      <v-list-item v-for="(task, key) in products" :key="key" > 
        <v-list-item-content>
            <v-list-item-title>{{task.task}}</v-list-item-title>
        </v-list-item-content>
        <v-btn
        class="ma-2"
        v-on:click="removeItem(task.id,key)"
        text
        icon
        color="blue lighten-2"
      >
        <v-icon>mdi-thumb-up</v-icon>
      </v-btn>
    </v-list-item>
    </vlist>
    <div class="add-products">
      <ul>
          <li class="search-box">
              <input type="text" placeholder="Add Tasks..." v-model="title" @keyup.enter="addProduct" >
          </li>
      </ul>
    <input type="hidden" name="csrfmiddlewaretoken" v-model="csrf_token">
  </div>
</v-card>
</template>
<script>

import Vue from 'vue';
import axios from 'axios'
// import axiosDefaults from "axios/lib/defaults"
const ListWidget = Vue.component('list-widget',{

  data(){
      return{
          products: [],
          title:'',
          csrf_token: document.querySelector('[name="csrfmiddlewaretoken"]').value
      }
  },
  mounted(){
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios.defaults.xsrfCookieName = "csrftoken";  
      axios({
          method:'get',
          url: 'http://127.0.0.1:8000/api/tasks',
          xsrfHeaderName:"X-CSRFToken",
          xsrfCookieName:"csrftoken",
          timeout: 1000,
      }).then(response =>{
          console.log('API has received data')
          this.products = response.data
      })
      .catch(err => {
          console.log(err)
      })
  },
  methods:{
      addProduct(){
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.defaults.xsrfCookieName = "csrftoken";  
          console.log("Clicked")
          axios({
            method:'post',
            url: 'http://127.0.0.1:8000/api/tasks/',
            timeout: 1000,
            data:{
                task : this.title,
                key: 123
            }
          }).then(response => {
                this.title = '' 
                this.products.push(response.data)
          })
      },
      removeItem(key,position){
          console.log("Removed Task with ID:" + key)
          axios({
            method:'delete',
            url: 'http://127.0.0.1:8000/api/tasks/',
            timeout: 1000,
            data:{
                id:key
            }
          }).then(response => {
                console.log(response)
                console.log(this.products)
                this.products.splice(position,1)
          })
      }
  }
  }
)
export default ListWidget;
</script>

<style>
* {
    font-family: sans-serif;
}

.add-products-container {
    position: absolute;
    border: 1px solid #DCDCDC;
    background-color: #F1F1F1;
    width: 500px;
    max-height: 624px;
    overflow-x: hidden;
    overflow-y: auto;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    box-sizing: border-box;
    padding: 10px;
}

.add-products {
    position: relative;
    background-color: #FFF;
    border: 1px solid;
    overflow: hidden;
    margin-bottom: 2px;
}

.add-products ul {
    margin: 0;
    padding: 0;
}

.product {
    position: relative;
    list-style: none;
    padding: 8px;
    margin: 0px;
    background-color: #FAE200;
    display: inline-block;
    margin: 4px;
    border-radius: 5px;
}

.product span {
    font-size: 12px;
}

.product a {
    font-size: 12px;
    font-weight: bold;
    color: black;
    text-decoration: none;
    padding-left: 10px;
}

.search-box {
    position: relative;
    display: inline-block;
}

.search-box input {
    padding: 8px;
    font-size: 12px;
    outline: none;
    border: none;
    margin: 4px;
    background-color: transparent;
}

.products-list {
    font-size: 12px;
    line-height: 20px;
    font-weight: bold;
}
</style>
