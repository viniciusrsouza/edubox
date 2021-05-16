<template>
  <v-container>
    <img src="../assets/logo-aibox.png" alt="logo-aibox"/>
    <h1>Edubox</h1>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
    name: 'LogoAndName',

});
</script>

<style scoped>
    div{
        margin: auto;
        width: 85%;
        display: flex;
        text-align: center;
    }

    img{
        margin: auto;
    }

    h1{
        margin: auto;
        color: #3b5c75;
        font-size: 64px;
    }

</style>