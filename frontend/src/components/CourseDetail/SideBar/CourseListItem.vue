<template>
  <v-list-item class="px-2" two-line link>
    <v-list-item-avatar>
      <v-img :src="course.picture"></v-img>
    </v-list-item-avatar>
    <v-list-item-content>
      <v-list-item-title class="text-color-blue">
        {{course.title}}
      </v-list-item-title>
      <v-list-item-subtitle> {{course.professor}} </v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "DisciplineListItem",
  props: {
    course: {
      type: Object as () => Course,
    },
  },
});
interface Course {
  id: number;
  title: string;
  professor: string;
  picture: string;
}
</script>

<style>
.text-color-blue {
  color: #3b5c78;
}
</style>