<template>
  <div>
      <Person v-for="person in people" :key="person.id" :person="person"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Person from './Person.vue'
export default Vue.extend({
    name: "PersonListContent",
    components: {
        Person
    },
    data: () => ({
        people: [
            {
                id: 1,
                name: "Julia Maria",
                email: "julia@gmail.com",
                picture_source: "https://randomuser.me/api/portraits/women/10.jpg"
            },
            {
                id: 1,
                name: "Julia Maria",
                email: "julia@gmail.com",
                picture_source: "https://randomuser.me/api/portraits/women/10.jpg"
            },
            {
                id: 1,
                name: "Julia Maria",
                email: "julia@gmail.com",
                picture_source: "https://randomuser.me/api/portraits/women/10.jpg"
            },
            {
                id: 1,
                name: "Julia Maria",
                email: "julia@gmail.com",
                picture_source: "https://randomuser.me/api/portraits/women/10.jpg"
            },
            {
                id: 1,
                name: "Julia Maria",
                email: "julia@gmail.com",
                picture_source: "https://randomuser.me/api/portraits/women/10.jpg"
            },
            {
                id: 1,
                name: "Julia Maria",
                email: "julia@gmail.com",
                picture_source: "https://randomuser.me/api/portraits/women/10.jpg"
            },
            {
                id: 1,
                name: "Julia Maria",
                email: "julia@gmail.com",
                picture_source: "https://randomuser.me/api/portraits/women/10.jpg"
            },
            {
                id: 1,
                name: "Julia Maria",
                email: "julia@gmail.com",
                picture_source: "https://randomuser.me/api/portraits/women/10.jpg"
            },
            {
                id: 1,
                name: "Julia Maria",
                email: "julia@gmail.com",
                picture_source: "https://randomuser.me/api/portraits/women/10.jpg"
            },
        ]
    }),
})
</script>

<style>

</style>