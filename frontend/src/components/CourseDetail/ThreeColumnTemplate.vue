<template>
  <v-container>
    <v-row class="mb-6">
      <v-col>
        <slot name="sidebar"></slot>
      </v-col>
      <v-col cols="6">
        <v-card class="pa-2" outlined tile>
          <slot name="content"></slot>
        </v-card>
      </v-col>
      <v-col>
        <v-card class="pa-2" outlined tile>
          <slot name="calendar"></slot>
        </v-card>
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