<template>
    <TwoColumnTemplate >
      <LoginForm/>
    </TwoColumnTemplate>
</template>

<script lang="ts">
import Vue from "vue";
import TwoColumnTemplate from "../components/registration/TwoColumnTemplate.vue";
import LoginForm from "../components/registration/LoginForm.vue";
export default Vue.extend({
  name: "Login",
  components: {
    TwoColumnTemplate,
    LoginForm,
  },
});
</script>