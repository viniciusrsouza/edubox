<template>
  <v-btn
    class="btn-container ma-4 white--text"
    :color="primary ? '#3b5c78' : 'white'"
    @click="() => (click ? click() : '')"
  >
    <v-icon class="me-2">mdi-{{ icon }}</v-icon>
    {{ text }}
  </v-btn>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "Button",
  props: {
    text: String,
    icon: String,
    primary: Boolean,
    click: Function,
  },
});
</script>
