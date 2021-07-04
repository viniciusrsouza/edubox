<template>
  <v-card class="mx-auto sidebar-container">
    <v-navigation-drawer permanent>
      <v-list>
        <v-list-item class="px-2" two-line>
          <v-list-item-avatar>
            <v-img src="@/assets/undraw/undraw_female_avatar_w3jk.svg"></v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="text-color-blue">
              {{ course.title }}
            </v-list-item-title>
            <v-list-item-subtitle> {{ professor.name }} </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list nav dense>
        <v-list-item link @click="redirect({ path: `/course/${course.id}` })">
          <v-list-item-icon>
            <v-icon class="text-color-blue"
              >mdi-newspaper-variant-outline</v-icon
            >
          </v-list-item-icon>
          <v-list-item-title class="text-color-blue">Feed</v-list-item-title>
        </v-list-item>
        <v-list-item
          link
          @click="redirect({ path: `/course/${course.id}/activity` })"
        >
          <v-list-item-icon>
            <v-icon class="text-color-blue">mdi-format-list-bulleted</v-icon>
          </v-list-item-icon>
          <v-list-item-title class="text-color-blue"
            >Activities</v-list-item-title
          >
        </v-list-item>
        <v-list-item
          link
          @click="redirect({ path: `/course/${course.id}/users` })"
        >
          <v-list-item-icon>
            <v-icon class="text-color-blue">mdi-account-multiple</v-icon>
          </v-list-item-icon>
          <v-list-item-title class="text-color-blue">People</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-divider></v-divider>
    <v-list nav dense class="courses">
      <v-list-item class="courses-btn">
        <v-list-item-content class="align-text-center text-color-blue">
          <v-list-item-title>
            Courses
            <v-icon x-small class="text-color-blue">mdi-open-in-new</v-icon>
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item link>
        <v-list-item-icon>
          <v-icon class="text-color-blue">mdi-plus-circle-outline</v-icon>
        </v-list-item-icon>
        <v-list-item-title class="text-color-blue" @click="updateDialog"
          >Join new course</v-list-item-title
        >
      </v-list-item>
      <v-dialog
        width="500"
        v-model="course_dialog"
        transition="dialog-bottom-transition"
      >
        <v-card>
          <v-card-title dark>
            {{ t("Home.CourseList.JoinCourse") }}
          </v-card-title>
          <v-card-text>
            <div class="course-dialog-text pb-2">
              {{ t("Home.CourseList.InsertCode") }}
            </div>
            <text-form
              :inputPlaceholder="t('Home.CourseList.CourseCode')"
              icon="mdi-alphabetical"
              v-model="course_code"
            />
          </v-card-text>
          <v-card-actions class="justify-end">
            <v-btn text @click="dismissDialog">{{ t("Common.Dismiss") }}</v-btn>
            <v-btn text @click="joinCourse" class="course-dialog-btn-join">
              {{ t("Home.CourseList.Join") }}
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <CourseListItem
        v-for="course in courses"
        :key="course.id"
        :course="course"
      />
    </v-list>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import CourseListItem from "./CourseListItem.vue";
import CoursesService, { Course } from "../../../services/courses_service";
import MemberService, { Member } from "../../../services/members_service";
import { redirect } from "../../../router/utils";
import { mapState } from "vuex";
import t from "../../../locale";
import TextForm from "../../registration/TextForm.vue";

export default Vue.extend({
  name: "SideBar",
  computed: {
    ...mapState("course", ["course"]),
  },
  components: {
    CourseListItem,
    TextForm
  },
  methods: {
    t,
    redirect,
    joinCourse() {
      CoursesService.join(this.course_code).then((res) => {
        console.log(res);
      });
    },

    dismissDialog() {
      this.course_dialog = false;
      this.course_code = "";
    },

    updateDialog(){
        this.course_dialog = true;
    },
  },

  mounted: function () {
    CoursesService.getAllForSideBar().then(({ results }) => {
      console.log(results);
      this.courses.push(...results);
    });

    MemberService.getProfessorByCourse(this.course.id).then(({ results }) => {
      this.professors.push(...results);
      this.professor = this.professors[0];
    });
  },

  data: () => ({
    courses: [] as Course[],
    professors: [] as Member[],
    professor: {} as Member,
    course_dialog: false,
    course_code: "",
  }),
});
</script>
>

<style lang="scss" scoped>
.align-text-center {
  text-align: center;
}
.text-color-blue {
  color: #3b5c78;
}

.sidebar-container {
  width: 256px;
}
</style>
