<template>
    <div class="add-products-container">
        <list-widget />
    </div>
</template>
<script>

import Vue from 'vue';
import ListWidget from './ListWidget.vue';

const App3 = Vue.component('app3',{
    components: {
        ListWidget
    },
  }
)
export default App3;
</script>

<style>
* {
    font-family: sans-serif;
}

.add-products-container {
    position: absolute;
    border: 1px solid #DCDCDC;
    background-color: #F1F1F1;
    width: 440px;
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
