<template>
  <v-btn
    class="btn-container ma-4 white--text"
    :color="primary ? '#3b5c78' : 'white'"
  >
    <v-icon class="me-2">mdi-{{ icon }}</v-icon>
    {{ text }}
  </v-btn>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "Button",
  props: ["text", "icon", "primary"],
});
</script>
