<template>
  <div class="navbar-container">
    <div class="navbar-logo-container">
      <div class="navbar-home-logo" @click="redirectHome">
        <img class="navbar-logo" src="../../../public/logo-aibox.png" />
        <span class="navbar-title">{{ t("edubox") }}</span>
      </div>
    </div>
    <div class="narbar-searchbar"><SearchField /></div>
    <div class="navbar-user-options">
      <v-btn text class="mx-4" @click="logout"> {{ t("logout") }} </v-btn>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../locale";
import SearchField from "./SearchField.vue";

export default Vue.extend({
  name: "Navbar",
  components: { SearchField },
  methods: {
    t,
    logout() {
      localStorage.setItem("access", "");
      localStorage.setItem("refresh", "");
      this.$router.go();
    },
    redirectHome() {
      if (this.$router.currentRoute.path !== "/") this.$router.push("/");
    },
  },
});
</script>

<style lang="scss" scoped>
.navbar-container {
  position: sticky;
  top: 0;
  background: white;
  z-index: 100;
  display: flex;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1), 0 3px 10px 0 rgba(0, 0, 0, 0.08);
  justify-content: space-between;
  align-items: center;
}

.navbar-home-logo {
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;

  * {
    user-select: none;
  }
}

.navbar-logo {
  height: 3em;
  margin: 0.5em;
}

.navbar-title {
  font-size: 1.4rem;
  font-weight: 500;
  color: $primary;
  text-transform: capitalize;
}

.navbar-logo-container {
  width: 100%;
  display: flex;
  justify-content: flex-start;
}

.navbar-user-options {
  width: 100%;
  display: flex;
  justify-content: flex-end;
}
</style>
