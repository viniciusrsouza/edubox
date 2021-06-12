<template>
  <v-form class="centered">
    <div class="d-flex align-center">
      <v-avatar size="256" class="auto-margin" @click="fakeClick()">
        <img v-if="url" :src="url"
      /></v-avatar>
    </div>

    <v-card-text>
      <TextForm
        :icon="'mdi-account'"
        :inputPlaceholder="t('full_name')"
        :setValue="(e) => (full_name = e)"
      />
      <TextForm
        :icon="'mdi-at'"
        :inputPlaceholder="t('email')"
        :setValue="(e) => (email = e)"
      />
      <TextForm
        :icon="'mdi-lock'"
        :inputPlaceholder="t('password')"
        :setValue="(e) => (password = e)"
        type="password"
      />
      <v-btn
        elevation="2"
        x-large
        color="#3B5C78"
        style="width: 100%"
        class="white--text"
        >{{ t("save_changes") }}</v-btn
      >
    </v-card-text>
    <input id="picker" type="file" @change="selectPicture" style="visibility: hidden;"/>
  </v-form>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../locale";
import TextForm from "../registration/TextForm.vue";
export default Vue.extend({
  components: {
    TextForm,
  },
  methods: {
    t,
    selectPicture(e: any) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
    },
    fakeClick() {
      let element: HTMLElement = document.querySelector(
        'input[type="file"]'
      ) as HTMLElement;
      element.click();
    },
  },

  data() {
    return {
      url: null,
    };
  },
});
</script>

<style lang="scss" scoped>
.centered {
  width: 20%;
  margin: auto;
}

.auto-margin {
  margin: auto;
}
</style>