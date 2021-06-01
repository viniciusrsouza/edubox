<template>
  <v-form>
    <v-card-text>
      <LogoAndName />
      <TextForm
        :icon="'mdi-account'"
        :inputPlaceholder="'Email'"
        :type="'email'"
        :id="'email'"
        :setValue="setEmail"
      />
      <TextForm
        :icon="'mdi-lock'"
        :inputPlaceholder="'Password'"
        :type="'password'"
        :id="'pw'"
        :setValue="setPassword"
      />
      <v-btn
        elevation="2"
        x-large
        color="#3B5C78"
        style="width: 100%"
        class="white--text"
        @click="login"
        >Sign In</v-btn
      >
    </v-card-text>
  </v-form>
</template>

<script lang="ts">
import Vue from "vue";
import LogoAndName from "./LogoAndName.vue";
import TextForm from "./TextForm.vue";
import api from "../../services/api_axios";
export default Vue.extend({
  name: "LoginForm",
  components: {
    LogoAndName,
    TextForm,
  },
  methods: {
    login() {
      let options = JSON.stringify({
        username: this.email,
        password: this.password,
      });
      api.post("api/token/", options, {
          headers: { "Content-Type": "application/json" },
        })
        .then((response) => {
          localStorage.setItem("refresh", response.data.refresh);
          localStorage.setItem("access", response.data.access);
          this.$router.push("/");
        })
        .catch((err) => {
          console.log(err.response.data);
        });
    },
    setEmail(email: string) {
      this.email = email;
    },
    setPassword(password: string) {
      this.password = password;
    },
  },
  data: () => ({
    email: "",
    password: "",
  }),
});
</script>

<style scoped></style>
