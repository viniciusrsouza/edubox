<template>
  <v-expansion-panels multiple class="assignment-list-container">
    <AssignmentCard v-for="post in assignments" :key="post.id" :post="post" />
  </v-expansion-panels>
</template>

<script lang="ts">
import { Post } from "@/models/models";
import Vue from "vue";
import AssignmentCard from "./AssignmentCard.vue";
export default Vue.extend({
  components: {
    AssignmentCard,
  },
  data: () => ({
    assignments: [] as Post[],
  }),
  async created() {
    const res = await this.$services.post.getAll("assignment");
    this.assignments = res.results;
  },
});
</script>
<style></style>
