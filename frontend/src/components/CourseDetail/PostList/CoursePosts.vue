<template>
  <div class="margin-bottom">
    <Post v-for="post in posts" :key="post.id" :post="post" />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Post from "./Post.vue";
export default Vue.extend({
  components: { Post },
  name: "CoursePosts",

  props: {
    courseId: Number,
  },

  data: () => ({
    posts: [
      {
        id: 1,
        content:
          "A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.",
        created_by: "Matheus Mosca",
        created_at: "03/02/2021 13:53:00",
      },
      {
        id: 2,
        content:
          "A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.",
        created_by: "Matheus Mosca",
        created_at: "03/02/2021 13:53:00",
      },
      {
        id: 3,
        content:
          "A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.",
        created_by: "Matheus Mosca",
        created_at: "03/02/2021 13:53:00",
      },
      {
        id: 4,
        content:
          "A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.",
        created_by: "Matheus Mosca",
        created_at: "03/02/2021 13:53:00",
      },
    ],
  }),
});
</script>

<style scoped>
 .margin-bottom {
     margin-bottom: 25px;
 }
</style>