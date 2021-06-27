<template>
  <v-app>
    <v-main>
      <v-snackbar :value="this.$store.state.snackbar.show" @input="dismiss">
        {{ this.$store.state.snackbar.text }}

        <template v-slot:action="{ attrs }">
          <v-btn color="pink" text v-bind="attrs" @click="dismiss">
            {{ t("Common.Dismiss") }}
          </v-btn>
        </template>
      </v-snackbar>
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import t from "./locale/index";

export default Vue.extend({
  name: "App",

  components: {},

  methods: {
    t,
    dismiss() {
      this.$store.dispatch({
        type: "dismiss_snackbar",
      });
    },
  },

  data: () => ({}),
});
</script>

<style lang="scss">
.main-snackbar-button {
  color: $primary;
}
</style>
