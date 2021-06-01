<template>
  <div>
    <Navbar />
    <three-column-template>
      <template v-slot:sidebar>
        <side-bar />
      </template>
      <template v-slot:content>
        <router-view />
      </template>
      <template v-slot:calendar>
        <h1>Calendar placeholder</h1>
      </template>
    </three-column-template>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import SideBar from "../components/CourseDetail/SideBar/SideBar.vue";
import ThreeColumnTemplate from "../components/CourseDetail/ThreeColumnTemplate.vue";
import Navbar from "../components/Navbar.vue";
export default Vue.extend({
  components: {
    SideBar,
    ThreeColumnTemplate,
    Navbar,
  },
  mounted: function (){
    /*this.$route.query.id tem o valor do id do curso atual*/ 
    console.log(this.$route.query.id);
  }
});
</script>

<style></style>
