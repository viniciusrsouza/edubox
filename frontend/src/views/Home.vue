<template>
  <div class="home-container">
    <Navbar />
    <div class="home-top">
      <div class="home-title">{{ t("courses") }}</div>
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            class="btn-container ma-4 white--text"
            color="#3b5c78"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon class="me-2">mdi-plus-circle-outline</v-icon>
            {{ t("new_course") }}
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in add_options"
            :key="index"
            link
            :href="item.endpoint"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
    <div class="home-content">
      <Card v-for="course in getCourses()" :key="course.id" :course="course" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Navbar from "../components/navbar/Navbar.vue";
import Card from "../components/Courses/Card.vue";
import t from "../locale";
import CoursesService from "../services/courses_service";

export default Vue.extend({
  name: "Home",
  components: { Navbar, Card },
  methods: {
    t,
    getCourses: function () {
      return this.courses.filter((c) => {
        return c.title
          .toLowerCase()
          .startsWith(this.$store.state.navbar.search.toLowerCase());
      });
    },
  },
  data: () => ({
    add_options: [
      { title: t("create_course"), endpoint: "create_course" },
      { title: t("join_course"), endpoint: "" },
    ],
    courses: [],
  }),
  mounted: function () {
    CoursesService.getAll()
      .then(({ data }) => {
        this.courses = [...this.courses, ...data.results];
      })
      .catch((err) => {
        console.log(err.response.data);
      });
  },
});
</script>

<style lang="scss" scoped>
.home-title {
  font-size: 2rem;
  font-weight: 500;
  color: $primary;
  padding: 0.5em 1em;
  text-transform: capitalize;
}

.home-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.home-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 350px));
  gap: 2em;
  margin: 1em 2em;
}
</style>
