<template>
  <div>
    <Navbar />
    <three-column-template>
      <template v-slot:sidebar>
        <side-bar />
      </template>
      <template v-slot:content>
        <PersonListContent />
      </template>
      <template v-slot:calendar>
        <v-btn large color="#3b5c78" class="white--text"><v-icon left dark>mdi-account-plus-outline</v-icon> Add People </v-btn>
      </template>
    </three-column-template>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import SideBar from "../components/CourseDetail/SideBar/SideBar.vue";
import ThreeColumnTemplate from "../components/CourseDetail/ThreeColumnTemplate.vue";
import Navbar from "../components/Navbar.vue";
import PersonListContent from "../components/CourseDetail/PersonList/PersonListContent.vue";
export default Vue.extend({
  components: {
    SideBar,
    ThreeColumnTemplate,
    Navbar,
    PersonListContent,
  },
});
</script>

<style scoped>
.text-color-blue {
  color: #3b5c78;
}
</style>