<template>
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
</template>

<script lang="ts">
import Vue from "vue";
import SideBar from "../components/CourseDetail/SideBar.vue";
import ThreeColumnTemplate from "../components/CourseDetail/ThreeColumnTemplate.vue";
export default Vue.extend({
  components: {
    SideBar,
    ThreeColumnTemplate,
  },
});
</script>

<style>
</style>