<template>
  <div class="margin-bottom">
    <PostCard v-for="post in posts" :key="post.id" :post="post" />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import PostCard from "./Post.vue";
import PostService, { PostWithAuthor } from "../../../services/post_service";
export default Vue.extend({
  components: { PostCard },
  name: "CoursePosts",

  mounted: function (){
    PostService.getAllWithAuthor().then((res) => {
      this.posts.push(...res);
    })
  },

  props: {
    courseId: Number,
  },

  data: () => ({
    posts: [] as PostWithAuthor[],
  }),
});
</script>

<style scoped>
.margin-bottom {
  margin-bottom: 25px;
}
</style>
