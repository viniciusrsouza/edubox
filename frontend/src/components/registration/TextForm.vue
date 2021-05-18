<template>
  
    <v-text-field
      solo
      :label="inputPlaceholder"
      :prepend-inner-icon="icon"
      class="textForm"
    ></v-text-field>
  
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "TextForm",
  props: ["icon", "inputPlaceholder"],
});
</script>


<style scoped>
.textForm {
  /* width: 85%; */
  padding: 12px 20px;
  margin: auto;
  display: block;
  box-sizing: border-box;
}
</style>