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
        >Sign In</v-btn
      >
    </v-card-text>
  </v-form>
</template>

<script lang="ts">
import Vue from "vue";
import LogoAndName from "./LogoAndName.vue";
import TextForm from "./TextForm.vue";
export default Vue.extend({
  name: "LoginForm",
  components: {
    LogoAndName,
    TextForm,
  },
});
</script>

<style scoped>
</style>