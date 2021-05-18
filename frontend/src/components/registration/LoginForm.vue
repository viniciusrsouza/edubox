<template>
  <v-form>
    <v-card-text>
      <LogoAndName />
      <TextForm :icon="'mdi-account'" :inputPlaceholder="'Email'" />
      <TextForm :icon="'mdi-lock'" :inputPlaceholder="'Password'" />
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
import LogoAndName from "../LogoAndName.vue";
import TextForm from "./TextForm.vue";
import api from "../../services/api_service";

export default Vue.extend({
  name: "LoginForm",
  components: {
    LogoAndName,
    TextForm,
  },
  methods: {
    login() {
      api.post("/token", { username: "asd", password: "asd" });
    },
  },
});
</script>

<style scoped></style>
