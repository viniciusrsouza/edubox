<template>
  <v-form>
    <v-card-text>
      <LogoAndName />
      <TextForm :icon="'mdi-account'" :inputPlaceholder="'Email'" :type="'email'" :id="'email'"/>
      <TextForm :icon="'mdi-lock'" :inputPlaceholder="'Password'" :type="'password'" :id="'pw'"/>
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
import api from '../../services/api_axios';
export default Vue.extend({
  name: "LoginForm",
  components: {
    LogoAndName,
    TextForm,
  },
  methods: {
    login() {
      let email = document.getElementById('email');
      let pw = document.getElementById('pw');
      let options = {
        "username": email,
        "password": pw
      }

      api.post('/token', options)
      .then((response) => {
        console.log(response);
      })
      .catch((err) => {
        console.log(err);
      })
    },
  },
});
</script>

<style scoped></style>
