<template>
  <div>
    <AssignmentCard
      v-for="assignment in assignments"
      :key="assignment.id"
      :assignment="assignment"
    />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import AssignmentCard from "./AssignmentCard.vue";
export default Vue.extend({
  components: {
    AssignmentCard,
  },
  data: () => ({
    assignments: [
      {
        id: 1,
        title: "Activity 1",
        posted_date: "11:24",
        description: "Lorem ipsum blablabla",
        due_date: "March 24, 2021",
      },
      {
        id: 2,
        title: "Activity 2",
        posted_date: "11:24",
        description: "Lorem ipsum blablabla",
        due_date: "March 24, 2021",
      },
      {
        id: 3,
        title: "Activity 3",
        posted_date: "11:24",
        description: "Lorem ipsum blablabla",
        due_date: "March 24, 2021",
      },
    ],
  }),
});
</script>
<style>
</style>