<template>
  <v-expansion-panels multiple class="assignment-list-container">
    <AssignmentCard
      v-for="assignment in assignments"
      :key="assignment.id"
      :assignment="assignment"
    />
  </v-expansion-panels>
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
        description:
          "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Delectus voluptatibus voluptates facere, nihil quis corrupti. Odit natus sequi commodi ex delectus et voluptatem eaque, quo voluptas est nobis ut tenetur velit laudantium molestias placeat culpa eligendi repellendus aliquid tempora doloribus! Consequatur nam consequuntur corrupti inventore asperiores ut reiciendis voluptatem qui.",
        due_date: "March 24, 2021",
      },
      {
        id: 2,
        title: "Activity 2",
        posted_date: "11:24",
        description:
          "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Delectus voluptatibus voluptates facere, nihil quis corrupti. Odit natus sequi commodi ex delectus et voluptatem eaque, quo voluptas est nobis ut tenetur velit laudantium molestias placeat culpa eligendi repellendus aliquid tempora doloribus! Consequatur nam consequuntur corrupti inventore asperiores ut reiciendis voluptatem qui.",
        due_date: "March 24, 2021",
      },
      {
        id: 3,
        title: "Activity 3",
        posted_date: "11:24",
        description:
          "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Delectus voluptatibus voluptates facere, nihil quis corrupti. Odit natus sequi commodi ex delectus et voluptatem eaque, quo voluptas est nobis ut tenetur velit laudantium molestias placeat culpa eligendi repellendus aliquid tempora doloribus! Consequatur nam consequuntur corrupti inventore asperiores ut reiciendis voluptatem qui.",
        due_date: "March 24, 2021",
      },
    ],
  }),
});
</script>
<style></style>
