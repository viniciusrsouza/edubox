<template>
  <v-list-item class="px-2" two-line link @click="redirectToCourse">
    <v-list-item-avatar>
      <v-img :src="this.professor.photo"></v-img>
    </v-list-item-avatar>
    <v-list-item-content>
      <v-list-item-title class="text-color-blue">
        {{ course.title }}
      </v-list-item-title>
      <v-list-item-subtitle> {{ this.professor.name }} </v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>
</template>

<script lang="ts">
import Vue from "vue";
import { Course } from "../../../services/courses_service";
import MemberService, { Member } from "../../../services/members_service";
import { redirect } from "@/router/utils";
import { mapActions } from "vuex";
export default Vue.extend({
  name: "DisciplineListItem",
  props: {
    course: {
      type: Object as () => Course,
    },
  },

  data: () => ({
    professors: [] as Member[],
    professor: {} as Member,
  }),

  methods: {
    ...mapActions("course", ["set_course"]),
    async redirectToCourse() {
      redirect({ path: `/course/${this.course.id}` });
      const id = this.$route.params.id;
      const course = await this.$services.course.get(id);
      this.set_course(course);
    },
  },

  mounted: function () {
    MemberService.getProfessorByCourse(this.course.id).then(({ results }) => {
      this.professors.push(...results);
      this.professor = this.professors[0];
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