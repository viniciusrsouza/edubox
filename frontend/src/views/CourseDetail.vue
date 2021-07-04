<template>
  <div>
    <v-progress-linear v-if="!this.course" indeterminate />
    <three-column-template v-else>
      <template v-slot:sidebar>
        <side-bar />
      </template>
      <template v-slot:content>
        <transition name="scale" mode="out-in">
          <router-view v-slot="{ Component }">
            <component :is="Component" />
          </router-view>
        </transition>
      </template>
      <template v-slot:calendar>
        <router-view name="calendar"></router-view>
      </template>
    </three-column-template>
  </div>
</template>

<script lang="ts">
import CoursesService from "@/services/courses_service";
import Vue from "vue";
import { mapActions, mapState } from "vuex";
import SideBar from "../components/CourseDetail/SideBar/SideBar.vue";
import ThreeColumnTemplate from "../components/CourseDetail/ThreeColumnTemplate.vue";
export default Vue.extend({
  components: {
    SideBar,
    ThreeColumnTemplate,
  },

  computed: {
    ...mapState("course", ["course"]),
  },

  methods: {
    ...mapActions("course", ["set_course"]),
  },

  async created() {
    const id = this.$route.params.id;
    const course = await CoursesService.get(id);
    this.set_course(course);
  },
});
</script>

<style scoped lang="scss">
.scale-enter-active,
.scale-leave-active {
  transition: all 0.1s ease;
}

.scale-enter,
.scale-leave-to,
.scale-leave-active {
  opacity: 0;
  transform: scale(0.9);
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.15s ease-out;
}
</style>
