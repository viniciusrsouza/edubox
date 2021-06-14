<template>
  <v-text-field
    solo
    :id="id"
    :label="inputPlaceholder"
    :prepend-inner-icon="icon"
    :type="type"
    class="textForm"
    :value="value"
    @input="$emit('update:value', $event)"
    :disabled="disabled"
  ></v-text-field>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "TextForm",
  props: {
    icon: String,
    inputPlaceholder: String,
    type: String,
    id: String,
    disabled: Boolean,
    value: String,
  },
});
</script>

<style lang="scss">
.textForm {
  /* width: 85%; */
  padding: 12px 20px;
  margin: auto;
  display: block;
  box-sizing: border-box;
}

.textForm label {
  text-transform: capitalize;
}
</style>
