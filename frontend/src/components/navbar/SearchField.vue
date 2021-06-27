<template>
  <div class="searchfield-container">
    <v-text-field
      :label="t('Navbar.Search')"
      dense
      outlined
      prepend-inner-icon="mdi-magnify"
      clearable
      hide-details="auto"
      @input="change"
    />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../locale";
export default Vue.extend({
  name: "SearchField",
  methods: {
    t,
    change(value: string) {
      this.$store.dispatch({
        type: "update_search",
        value: value || "",
      });
    },
  },
});
</script>

<style lang="scss">
.searchfield-container {
  width: 20em;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
</style>
