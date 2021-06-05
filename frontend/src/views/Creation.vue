<template>
  <div>
    <Navbar />
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
</template>

<script lang="ts">
import Vue from "vue";
import Navbar from "../components/navbar/Navbar.vue";
import api from "../services/api_axios";
export default Vue.extend({
  name: "Creation",
  methods: {
    create() {
      const payload = { title: this.title, description: this.description };
      api.post("api/courses/", payload).then((res) => {
        if (res.status === 201) {
          this.$router.push("/");
        }
      });
    },
  },
  components: {
    Navbar,
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
</style>
