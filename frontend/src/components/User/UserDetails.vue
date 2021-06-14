<template>
  <v-form class="centered d-flex flex-column justify-center align-center">
    <div class="d-inline-flex avatar">
      <v-avatar size="256" class="auto-margin">
        <img v-if="url" :src="url" />
      </v-avatar>
      <v-btn
        icon
        elevation="8"
        class="edit-icon"
        color="primary"
        large
        @click="fakeClick()"
      >
        <v-icon>mdi-image-edit</v-icon>
      </v-btn>
    </div>

    <v-card-text>
      <TextForm
        :icon="'mdi-account'"
        :inputPlaceholder="t('full_name')"
        :setValue="(e) => (full_name = e)"
        v-model="this.user.name"
      />
      <TextForm
        :icon="'mdi-at'"
        :inputPlaceholder="t('email')"
        v-model="this.user.email"
      />
      <TextForm
        :icon="'mdi-lock'"
        :inputPlaceholder="t('password')"
        type="password"
        disabled
        v-model="this.user.password"
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
    <input
      id="picker"
      type="file"
      @change="selectPicture"
      style="visibility: hidden"
    />
  </v-form>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../locale";
import TextForm from "../registration/TextForm.vue";
import UserService from "../../services/user_service";
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
      url: require("@/assets/undraw/undraw_profile_pic_ic5t.svg"),
      user: {
        name: "",
        email: "",
        password: "*********",
      },
    };
  },

  async mounted() {
    console.log("mounted");
    try {
      let user = await UserService.fetchUser();
      this.user = { ...user, password: "" };
      console.log(this.user);
    } catch (error) {
      console.log("error: ", error);
    }
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

.avatar {
  position: relative;
}

.edit-icon {
  position: absolute;
  bottom: 1em;
  right: 1em;
  background: white;
}
</style>
