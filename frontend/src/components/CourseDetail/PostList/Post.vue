<template>
  <v-card class="distance-top" elevation="8">
    <v-row class="mb-6 no-margin-bottom">
      <v-col cols="1" class="margin d-flex justify-center">
        <v-icon>mdi-thumb-up-outline</v-icon>
      </v-col>
      <v-col>
        <v-row class="post-title"> {{ post.title }} </v-row>
        <v-row> {{ post.text }} </v-row>
      </v-col>
    </v-row>
    <v-list-item>
      <v-list-item-avatar>
        <v-img src="@/assets/undraw/undraw_male_avatar_323b.svg"></v-img>
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title> by {{ post.author.name }} </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../../locale";
export default Vue.extend({
  name: "PostCard",
  props: {
    post: {
      type: Object as () => Post,
    },
  },
  methods: {
    t,
  },
  data: () => ({
    showLess: true,
  }),
});

interface Post {
  id: number;
  author: {
    id: number;
    email: string;
    name: string;
  };
  course: number;
  title: string;
  text: string;
}
</script>

<style lang="scss" scoped>
.margin {
  margin-left: 10px;
}

.distance-top {
  margin-top: 25px;
}

.no-margin-bottom {
  margin-bottom: 0px !important;
}

.align-right {
  text-align: right;
}

.a-margin {
  margin-right: 10px;
}

.post-title {
  color: $primary;
  font-size: 1.6rem;
  font-weight: 500;
}
</style>
