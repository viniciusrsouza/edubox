<template>
  <v-card class="distance-top" elevation="8">
    <v-row class="mb-6 no-margin-bottom">
      <v-col cols="1" class="margin">
        <v-icon>mdi-thumb-up-outline</v-icon>
      </v-col>
      <v-col cols="10">
        <p>{{ post.content }}</p>
      </v-col>
    </v-row>
    <v-list-item>
      <v-list-item-avatar>
        <v-img src="@/assets/undraw/undraw_male_avatar_323b.svg"></v-img>
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title> by {{ post.created_by }} </v-list-item-title>
      </v-list-item-content>
    </v-list-item>

    <div v-if="postResponses.length > 1">
      <div v-if="showLess === true" class="align-right">
        <a class="a-margin" @click="showLess = !showLess">{{
          t("CoursePage.Feed.Post.ShowMore")
        }}</a>
      </div>
      <div v-else class="align-right">
        <a class="a-margin" @click="showLess = !showLess">{{
          t("CoursePage.Feed.Post.ShowLess")
        }}</a>
      </div>
      <div v-if="showLess">
        <PostResponse
          v-for="response in postResponses.slice(0, 1)"
          :key="response.id"
          :response="response"
        />
      </div>
      <div v-else>
        <PostResponse
          v-for="response in postResponses"
          :key="response.id"
          :response="response"
        />
      </div>
    </div>
    <div v-else>
      <PostResponse
        v-for="response in postResponses"
        :key="response.id"
        :response="response"
      />
    </div>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import PostResponse from "./PostResponse.vue";
import t from "../../../locale";
export default Vue.extend({
  name: "Post",

  components: {
    PostResponse,
  },
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
    postResponses: [
      {
        id: 1,
        content:
          "Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.",
        created_by: "Vinicius Souza",
        created_at: "03/02/2021 13:53:00",
      },
      {
        id: 2,
        content:
          "Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.",
        created_by: "Matheus Mosca",
        created_at: "03/02/2021 13:53:00",
      },
      {
        id: 3,
        content:
          "Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.",
        created_by: "Matheus Mosca",
        created_at: "03/02/2021 13:53:00",
      },
      {
        id: 4,
        content:
          "Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.",
        created_by: "Matheus Mosca",
        created_at: "03/02/2021 13:53:00",
      },
    ],
  }),
});

interface Post {
  id: number;
  content: string;
  created_by: string;
  created_at: string;
}
</script>

<style scoped>
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
</style>
