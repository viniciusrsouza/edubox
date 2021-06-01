<template>
  <v-container fluid fill-height>
    <v-row no-gutters style="height: 100%">
      <v-col cols="8" style="text-align: center">
        <img
          src="../../assets/Online_Learning.png"
          alt="onlineLearning"
          style="position: relative; top: 50%; transform: translateY(-50%)"
        />
      </v-col>
      <v-col cols="4">
        <v-card style="height: 100%">
          <slot> </slot>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "TwoColumnTemplate",
});
</script>

<style scoped></style>
