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
      <v-list v-for="(item, index) in user_options" :key="index">
        <v-menu offset-x left open-on-hover v-if="item.language">
          <template v-slot:activator="{ on: on2, attrs: attrs2 }">
            <v-list-item
              link
              @click="performAction(item.action)"
              v-on="on2"
              v-bind="attrs2"
            >
              <div class="navbar-options-icon">
                <v-icon>mdi-{{ item.icon }}</v-icon>
              </div>
              <v-list-item-title class="navbar-options-title">{{
                item.title
              }}</v-list-item-title>
            </v-list-item>
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
              <v-list-item-title class="navbar-options-title">{{
                item.title
              }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
        <v-list-item link @click="performAction(item.action)" v-else>
          <div class="navbar-options-icon">
            <v-icon>mdi-{{ item.icon }}</v-icon>
          </div>
          <v-list-item-title class="navbar-options-title">{{
            item.title
          }}</v-list-item-title>
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
import { Languages } from "@/constants";

export default Vue.extend({
  name: "navbar_options",
  components: { Profile, NotifiableButton },
  props: {
    className: String,
  },
  data: (): Data => ({
    user_options: [
      {
        title: t("Navbar.MyAccount"),
        icon: "account",
        action: { redirect: "/account" },
      },
      {
        title: t("Navbar.Settings"),
        icon: "cog",
        action: { redirect: "/settings" },
      },
      {
        title: "languages",
        icon: "translate",
        action: {},
        language: true,
      },
      {
        title: t("Navbar.Logout"),
        icon: "logout",
        action: { callback: "logout" },
      },
    ],
    languages: [
      {
        title: "English",
        icon: "",
        language: Languages.EN_US,
      },
      {
        title: "Portuguese",
        icon: "",
        language: Languages.PT_BR,
      },
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
      const obj = Object(this);
      return (
        (action.redirect && redirect({ path: action.redirect })) ||
        (action.callback && obj[action.callback]())
      );
    },
  },
});

interface Data {
  user_options: Array<UserOption>;
  languages: Array<Language>;
}

interface Language {
  title: string;
  icon: string;
  language: Languages;
}

interface UserOption {
  title: string;
  icon: string;
  action: Action;
  language?: boolean;
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

.navbar-options-title {
  text-transform: capitalize;
}
</style>
