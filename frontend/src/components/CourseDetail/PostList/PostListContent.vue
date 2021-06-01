<template>
  <div>
    <v-card>
      <NewPost />
    </v-card>
    <CoursePosts/>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import NewPost from "./NewPost.vue";
import CoursePosts from "./CoursePosts.vue";
export default Vue.extend({
  components: {
    NewPost,
    CoursePosts,
  },
});
</script>

<style>
</style>