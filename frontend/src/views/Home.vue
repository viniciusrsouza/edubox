<template>
  <div class="home-container">
    <Navbar />
    <div class="home-top">
      <div class="home-title">{{ t("courses") }}</div>
      <Button
        :text="t('new_course')"
        icon="plus-circle-outline"
        :primary="true"
        :click="() => addCourse()"
      />
    </div>
    <div class="home-content">
      <Card v-for="course in courses" :key="course.id" :course="course" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Navbar from "../components/Navbar.vue";
import Button from "../components/Button.vue";
import Card from "../components/Courses/Card.vue";
import t from "../locale";
import api from "../services/api_axios";

export default Vue.extend({
  name: "Home",
  components: { Navbar, Button, Card },
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
