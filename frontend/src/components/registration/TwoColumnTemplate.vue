<template>
  <div class="two-column-wrap">
    <div class="two-column-container">
      <div class="two-column-left">
        <img
          src="../../assets/Online_Learning.png"
          alt="onlineLearning"
          style="position: relative; top: 50%; transform: translateY(-50%)"
        />
      </div>
      <div class="two-column-right">
        <slot />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "TwoColumnTemplate",
});
</script>

<style lang="scss" scoped>
.two-column-wrap {
  background: $background;
  height: 100%;
}

.two-column-container {
  display: flex;
  justify-content: flex-end;
  width: 100%;
  height: 100%;
  max-width: 1920px;
  margin: 0 auto;
  background: $content-background;

  .two-column-right,
  & {
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1), 0 3px 10px 0 rgba(0, 0, 0, 0.08);
  }
  .two-column-right {
    padding: 2em;
  }
  .two-column-left {
    width: 100%;
    text-align: center;
  }
}

@media (max-width: 1024px) {
  .two-column-container {
    justify-content: center;
    .two-column-left {
      display: none;
    }
  }
}
</style>
