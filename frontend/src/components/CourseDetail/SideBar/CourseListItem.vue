<template>
  <v-list-item class="px-2" two-line link>
    <v-list-item-avatar>
      <v-img :src="course.picture"></v-img>
    </v-list-item-avatar>
    <v-list-item-content>
      <v-list-item-title class="text-color-blue">
        {{ course.title }}
      </v-list-item-title>
      <v-list-item-subtitle> {{ course.professor }} </v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>
</template>

<script lang="ts">
import Vue from "vue";
import { Course } from "../../../services/courses_service";
import MemberService from "../../../services/members_service";
export default Vue.extend({
  name: "DisciplineListItem",
  props: {
    course: {
      type: Object as () => Course,
    },
  },

  mounted: function () {
    MemberService.getProfessorByCourse(this.course.id).then((res) => {
      console.log(res);
    });
  },
});
// interface Course {
//   id: number;
//   title: string;
//   professor: string;
//   picture: string;
// }
</script>

<style>
.text-color-blue {
  color: #3b5c78;
}
</style>