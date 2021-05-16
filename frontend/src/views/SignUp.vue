<template>
    <TwoColumnTemplate >
      <SignUpForm/>
    </TwoColumnTemplate>
</template>

<script lang="ts">
import Vue from "vue";
import TwoColumnTemplate from "../components/TwoColumnTemplate.vue";
import SignUpForm from '../components/SignUpForm.vue';
export default Vue.extend({
  name: "SignUp",
  components: {
    TwoColumnTemplate,
    SignUpForm,
  },
});
</script>