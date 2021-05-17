<template>
  <TwoColumnTemplate>
    <SignUpForm />
  </TwoColumnTemplate>
</template>

<script lang="ts">
import Vue from "vue";
import TwoColumnTemplate from "../components/registration/TwoColumnTemplate.vue";
import SignUpForm from "../components/registration/SignUpForm.vue";
export default Vue.extend({
  name: "SignUp",
  components: {
    TwoColumnTemplate,
    SignUpForm,
  },
});
</script>