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
      <Card v-for="course in courses" :key="course.id" :course="course" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Navbar from "../components/Navbar.vue";
import Card from "../components/Courses/Card.vue";
import t from "../locale";
import api from "../services/api_axios";

export default Vue.extend({
  name: "Home",
  components: { Navbar, Card },
  methods: {
    t,
    addCourse: function () {
      console.log("teste");
      this.courses.push({
        id: ++this.last_id,
        title: "Artificial Intelligence",
        description:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam in mauris purus. Morbi vestibulum dui sed urna porta consequat. In a arcu rutrum, consectetur est ac, volutpat eros.",
        favorite: false,
      });
    },
  },
   mounted: function() {
      api.get("/api/courses/", {
          headers: { "Content-Type": "application/json" },
        })
        .then((response) => {
          //this.courses.push({...this.courses, ...response.data.results});
          this.courses = [...this.courses, ...response.data.results];
          console.log(response.data);
        })
        .catch((err) => {
          console.log(err.response.data);
        });
       
      //getCourses()
    },
  data: () => ({
    add_options: [
      { title: t("create_course"), endpoint: "creation" },
      { title: t("join_course"), endpoint: "" },
    ],
    courses: [
    ]
  }),
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
