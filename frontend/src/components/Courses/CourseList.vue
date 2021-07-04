<template>
  <div class="card-list-container">
    <div class="card-list-top">
      <div class="card-list-title">{{ t("Home.CourseList.Courses") }}</div>
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            class="btn-container ma-4 white--text"
            color="#3b5c78"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon class="me-2">mdi-plus-circle-outline</v-icon>
            {{ t("Home.CourseList.NewCourse") }}
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in getAddOptions()"
            :key="index"
            link
            @click="item.action()"
          >
            <v-list-item-title class="card-menu-item">{{
              item.title
            }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
    <div class="card-list-content" v-if="getCourses().length > 0">
      <Card v-for="course in getCourses()" :key="course.id" :course="course" />
    </div>
    <!-- <div class="card-list-no-data" v-else>
      <div class="no-data-text">
        {{ t("Home.CourseList.NoData") }}
      </div>
    </div> -->

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
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Card from "./Card.vue";
import t from "../../locale";
import CoursesService, { Course } from "../../services/courses_service";
import { redirect } from "@/router/utils";
import TextForm from "../registration/TextForm.vue";

export default Vue.extend({
  name: "CourseList",
  components: { Card, TextForm },
  methods: {
    t,
    getCourses(): Course[] {
      return this.courses.filter((c) => {
        return c.title
          .toLowerCase()
          .startsWith(this.$store.state.navbar.search.toLowerCase());
      });
    },

    getAddOptions() {
      const updateDialog = () => {
        this.course_dialog = true;
      };
      return [
        {
          title: t("Home.CourseList.CreateCourse"),
          action: () => redirect({ path: "/create_course" }),
        },
        {
          title: t("Home.CourseList.JoinCourse"),
          action: updateDialog,
        },
      ];
    },

    joinCourse() {
      CoursesService.join(this.course_code).then((res) => {
        console.log(res);
      });
    },

    dismissDialog() {
      this.course_dialog = false;
      this.course_code = "";
    },
  },
  data: () => ({
    courses: [] as Course[],
    course_dialog: false,
    course_code: "",
  }),
  mounted: function () {
    CoursesService.getAll()
      .then(({ results }) => {
        this.courses.push(...results);
      })
      .catch((err) => {
        console.log(err);
      });
  },
});
</script>

<style lang="scss" scoped>
.card-list-title {
  font-size: 2rem;
  font-weight: 500;
  color: $primary;
  padding: 0.5em 1em;
  text-transform: capitalize;
}

.card-list-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-list-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 350px));
  gap: 1.5em;
  margin: 1em 2em;
}

.course-dialog-btn-join {
  color: $primary;
}

.card-menu-item {
  text-transform: capitalize;
}
</style>
