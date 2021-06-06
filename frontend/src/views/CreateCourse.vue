<template>
  <div>
    <div class="create-course-container">
      <div class="home-top">
        <div class="home-title">{{ "Create a new course here!" }}</div>
      </div>
      <v-container fluid fill-height>
        <v-row no-gutters style="height: 100%">
          <v-col cols="5">
            <v-form>
              <v-text-field
                label="Name"
                solo
                @change="(e) => (this.title = e)"
              ></v-text-field>
              <v-textarea
                label="Course Description"
                solo
                height="300"
                auto-grow
                @change="(e) => (this.description = e)"
              ></v-textarea>
              <v-btn
                elevation="2"
                x-large
                color="#3B5C78"
                style="width: 20%"
                class="white--text"
                @click="create"
                >Create</v-btn
              >
            </v-form>
          </v-col>
          <v-col cols="7" style="text-align: center">
            <img
              src="../assets/Teaching.png"
              alt="Teaching"
              style="position: relative; top: 50%; transform: translateY(-50%)"
            />
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import CoursesService from "../services/courses_service";
export default Vue.extend({
  name: "CreateCourse",
  methods: {
    create() {
      const payload = { title: this.title, description: this.description };
      CoursesService.create(payload).then(({ success }) => {
        if (success) this.$router.push("/");
      });
    },
  },
  data: () => ({
    title: "",
    description: "",
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

.create-course-container {
  height: 100%;
  max-width: 1920px;
  margin: 0 auto;
}
</style>
