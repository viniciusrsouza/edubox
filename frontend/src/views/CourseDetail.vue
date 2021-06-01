<template>
  <div>
    <Navbar />
    <three-column-template>
      <template v-slot:sidebar>
        <side-bar />
      </template>
      <template v-slot:content>
        <PostListContent/>
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
import PostListContent from '../components/CourseDetail/PostList/PostListContent.vue'
export default Vue.extend({
  components: {
    SideBar,
    ThreeColumnTemplate,
    Navbar,
    PostListContent
  },
});
</script>

<style>
</style>