<template>
  <v-container>
    <v-row class="mb-6">
      <v-col>
        <slot name="sidebar"></slot>
      </v-col>
      <v-col cols="6">
        <slot name="content"></slot>
      </v-col>
      <v-col>
        <slot name="calendar"></slot>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({});
</script>

<style>
</style>