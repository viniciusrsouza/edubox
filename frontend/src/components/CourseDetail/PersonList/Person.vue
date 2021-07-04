<template>
  <v-card class="bottom-distance">
    <v-list-item>
      <v-list-item-avatar>
        <v-img :src="person_photo"></v-img>
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
  computed: {
    person_photo() {
      const _ = this.person.photo
        ? `http://localhost:5001${this.person.photo}`
        : require("../../../assets/undraw/undraw_male_avatar_323b.svg");
      console.log(_);
      return _;
    },
  },
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
