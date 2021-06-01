<template>
  <div class="home-container">
    <Navbar />
    <three-column-template>
      <template v-slot:sidebar>
        <side-bar />
      </template>
      <template v-slot:content>
        <h1>Here might be a page title</h1>
      </template>
      <template v-slot:calendar>
        <h1>Here might be a page title</h1>
      </template>
    </three-column-template>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import SideBar from "../components/CourseDetail/SideBar.vue";
import ThreeColumnTemplate from "../components/CourseDetail/ThreeColumnTemplate.vue";
import Navbar from '../components/Navbar.vue'
export default Vue.extend({
  components: {
    SideBar,
    ThreeColumnTemplate,
    Navbar
  },
});
</script>

<style>
</style>