<template>
  <div class="home-wrapper">
    <nav-bar />
    <div class="home-container">
      <router-view />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../locale";
import CoursesService from "../services/courses_service";
import NavBar from "../components/navbar/NavBar.vue";

export default Vue.extend({
  name: "Home",
  components: { NavBar },
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
.home-wrapper {
  background: $background;
  height: 100%;
}

.home-container {
  background: $content-background;
  max-width: 1920px;
  margin: 0 auto;
  height: 100%;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1), 0 3px 10px 0 rgba(0, 0, 0, 0.08);
}

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
