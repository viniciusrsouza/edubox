<template>
  <v-container fluid>
    <v-textarea
      clearable
      auto-grow
      rows="1"
      clear-icon="mdi-close-circle"
      :label="t('write_new_post')"
      prepend-inner-icon="mdi-pencil-outline"
      value=""
    ></v-textarea>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../../locale";
export default Vue.extend({
  methods: { t },
});
</script>

<style>
</style>