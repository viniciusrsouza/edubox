<template>
  <v-card class="bottom-distance">
    <v-list-item>
      <v-list-item-avatar>
        <v-img :src="person.photo"></v-img>
      </v-list-item-avatar>
      <v-list-item-title>{{ person.name }}</v-list-item-title>
      <v-list-item-title>Email: {{ person.email }}</v-list-item-title>
    </v-list-item>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "Person",
  props: {
    person: {
      type: Object as () => Person,
    },
  },
});

interface Person {
  name: string;
  email: string;
  photo: string;
  role: number;
}
</script>

<style scoped>
.bottom-distance {
  margin-bottom: 15px;
}
</style>