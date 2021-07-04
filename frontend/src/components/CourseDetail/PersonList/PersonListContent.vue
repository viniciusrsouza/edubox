<template>
  <div>
    <Person v-for="person in people" :key="person.id" :person="person" />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Person from "./Person.vue";
import MemberService from "../../../services/members_service";
export default Vue.extend({
  name: "PersonListContent",
  components: {
    Person,
  },

  mounted: function(){
    MemberService.getAll().then((res)=> {
      console.log(res);
    })
  },

  data: () => ({
    people: [
      {
        id: 1,
        name: "Julia Maria",
        email: "julia@gmail.com",
        picture_source: "https://randomuser.me/api/portraits/women/10.jpg",
      },
      {
        id: 2,
        name: "Julia Maria",
        email: "julia@gmail.com",
        picture_source: "https://randomuser.me/api/portraits/women/10.jpg",
      },
      {
        id: 3,
        name: "Julia Maria",
        email: "julia@gmail.com",
        picture_source: "https://randomuser.me/api/portraits/women/10.jpg",
      },
      {
        id: 4,
        name: "Julia Maria",
        email: "julia@gmail.com",
        picture_source: "https://randomuser.me/api/portraits/women/10.jpg",
      },
      {
        id: 5,
        name: "Julia Maria",
        email: "julia@gmail.com",
        picture_source: "https://randomuser.me/api/portraits/women/10.jpg",
      },
      {
        id: 6,
        name: "Julia Maria",
        email: "julia@gmail.com",
        picture_source: "https://randomuser.me/api/portraits/women/10.jpg",
      },
    ],
  }),
});
</script>

<style></style>
