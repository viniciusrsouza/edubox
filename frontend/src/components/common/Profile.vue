<template>
  <div class="profile">
    <v-img :src="path" />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "user_profile",
  props: {
    path: {
      type: String,
      default: require("@/assets/undraw/undraw_male_avatar_323b.svg"),
    },
  },
  data: () => ({}),
  methods: {},
});
</script>

<style lang="scss" scoped>
.profile {
  width: 32px;
  height: 32px;
}
</style>
