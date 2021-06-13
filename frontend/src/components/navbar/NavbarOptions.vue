<template>
  <div :class="`navbar-options-container ${className}`">
    <notifiable-button icon="calendar-month" />
    <notifiable-button notification />
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <div v-on="on" v-bind="attrs" class="navbar-options-ddl-button">
          <profile />
          <v-icon class="me-2">mdi-chevron-down</v-icon>
        </div>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in user_options"
          :key="index"
          link
          @click="performAction(item.action)"
        >
          <div class="navbar-options-icon">
            <v-icon>mdi-{{ item.icon }}</v-icon>
          </div>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../locale";
import Profile from "../common/Profile.vue";
import { redirect } from "../../router/utils";
import NotifiableButton from "../common/NotifiableButton.vue";

export default Vue.extend({
  name: "navbar_options",
  components: { Profile, NotifiableButton },
  props: {
    className: String,
  },
  data: (): Data => ({
    user_options: [
      {
        title: t("my_account"),
        icon: "account",
        action: { redirect: "/account" },
      },
      { title: t("settings"), icon: "cog", action: { redirect: "/settings" } },
      { title: t("logout"), icon: "logout", action: { callback: "logout" } },
    ],
  }),
  methods: {
    t,
    logout() {
      localStorage.setItem("access", "");
      localStorage.setItem("refresh", "");
      this.$router.go(0);
    },
    performAction(action: Action): boolean {
      return (
        (action.redirect && redirect({ path: action.redirect })) ||
        (action.callback && this[action.callback]())
      );
    },
  },
});

interface Data {
  user_options: Array<UserOption>;
}

interface UserOption {
  title: string;
  icon: string;
  action: Action;
}

interface Action {
  redirect?: string;
  callback?: string;
}
</script>

<style lang="scss">
.navbar-options-container {
  height: 4em;
  align-items: center;
  justify-content: center;
  gap: 1em;
}

.navbar-options-ddl-button {
  display: flex;
  padding-right: 1em;
  height: 100%;
  align-items: center;
  justify-content: center;
}

.navbar-options-ddl-button[aria-expanded="true"] {
  .v-icon {
    rotate: 180deg;
  }
}

.navbar-options-icon {
  margin-right: 1em;
}
</style>
