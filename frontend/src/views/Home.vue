<template>
  <div>
    <Navbar />
    <div class="home-top">
      <div class="home-title">Courses</div>
      <Button text="New Course" icon="plus-circle-outline" :primary="true" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Navbar from "../components/Navbar.vue";
import Button from "../components/Button.vue";

export default Vue.extend({
  name: "Home",
  components: { Navbar, Button },
});
</script>

<style lang="scss" scoped>
.home-title {
  font-size: 2rem;
  font-weight: 500;
  color: $primary;
  padding: 0.5em;
}

.home-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
