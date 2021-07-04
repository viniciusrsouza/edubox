<template>
  <div>
    <v-card>
      <NewPost />
    </v-card>
    <CoursePosts :key="course.id" />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import NewPost from "./NewPost.vue";
import CoursePosts from "./CoursePosts.vue";
import { mapState } from "vuex";
export default Vue.extend({
  components: {
    NewPost,
    CoursePosts,
  },

  computed: {
    ...mapState("course", ["course"]),
  },
});
</script>

<style></style>
