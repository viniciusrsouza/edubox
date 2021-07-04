<template>
  <div>
    <Person v-for="person in people" :key="person.id" :person="person" />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Person from "./Person.vue";
import MemberService, { Member } from "../../../services/members_service";
export default Vue.extend({
  name: "PersonListContent",
  components: {
    Person,
  },

  mounted: function () {
    MemberService.getAll().then((res) => {
      this.people.push(...res.results);
    });
  },

  data: () => ({
    people: [] as Member[],
  }),
});
</script>

<style></style>
