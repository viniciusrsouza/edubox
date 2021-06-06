<template>
  <div>
    <three-column-template>
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
        <h1>Calendar placeholder</h1>
      </template>
    </three-column-template>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import SideBar from "../components/CourseDetail/SideBar/SideBar.vue";
import ThreeColumnTemplate from "../components/CourseDetail/ThreeColumnTemplate.vue";
export default Vue.extend({
  components: {
    SideBar,
    ThreeColumnTemplate,
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
