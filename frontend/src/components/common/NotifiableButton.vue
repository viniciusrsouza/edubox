<template>
  <v-btn class="notifiable-button" elevation="2" icon>
    <div :class="`notification-indicator ${notification ? 'visible' : ''}`" />
    <v-icon>mdi-{{ icon }}</v-icon>
  </v-btn>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "notifiable_button",
  props: {
    notification: {
      type: Boolean,
      default: false,
    },
    icon: {
      type: String,
      default: "bell",
    },
  },
  data: () => ({}),
  methods: {},
});
</script>

<style lang="scss">
.notifiable-button {
  position: relative;

  .notification-indicator {
    display: none;
    width: 10px;
    height: 10px;
    position: absolute;
    top: -0.4em;
    right: 0;
    border-radius: 100%;
    background: $primary;
  }

  .notification-indicator.visible {
    display: block;
  }
}
</style>
