<template>
  <div class="margin-bottom">
    <PostCard v-for="post in posts" :key="post.id" :post="post" />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import PostCard from "./Post.vue";
import PostService from "../../../services/post_service";
import { Post } from "@/models/models";
export default Vue.extend({
  components: { PostCard },
  name: "CoursePosts",

  mounted: function () {
    PostService.getAll().then((res) => {
      this.posts.push(...res.results);
    });
  },

  props: {
    courseId: Number,
  },

  data: () => ({
    posts: [] as Post[],
  }),
});
</script>

<style scoped>
.margin-bottom {
  margin-bottom: 25px;
}
</style>
