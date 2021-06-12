<template>
  <div class="grid-container">
    <div class="left-container">
      <slot name="sidebar" />
    </div>
    <div class="middle-container">
      <slot name="content" />
    </div>
    <div class="right-container">
      <slot name="calendar" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({});
</script>

<style lang="scss" scoped>
.grid-container {
  display: grid;
  grid-template-areas: "lft mid rgt" ". mid .";
  grid-template-columns: auto minmax(0px, 1000px) auto;
  gap: 2em;
  padding: 2em;

  @media (max-width: 1024px) {
    grid-template-areas: "lft mid mid" "rgt mid mid" ". mid mid";
  }

  @media (max-width: 768px) {
    grid-template-areas: "mid mid mid";

    .left-container {
      display: none;
    }

    .right-container {
      display: none;
    }
  }
}

.left-container {
  grid-area: lft;
}

.middle-container {
  grid-area: mid;
}

.right-container {
  grid-area: rgt;
}
</style>
