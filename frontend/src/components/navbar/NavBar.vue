<template>
  <div class="navbar-container">
    <div class="navbar-content">
      <div class="navbar-logo-container">
        <div class="navbar-home-logo" @click="redirectHome">
          <img class="navbar-logo" src="../../../public/logo-aibox.png" />
          <span class="navbar-title">{{ t("Common.Edubox") }}</span>
        </div>
      </div>
      <div class="narbar-searchbar"><SearchField /></div>
      <navbar-options className="navbar-user-options" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../locale";
import NavbarOptions from "./NavbarOptions.vue";
import SearchField from "./SearchField.vue";

export default Vue.extend({
  name: "NavBar",
  components: { SearchField, NavbarOptions },
  methods: {
    t,
    redirectHome() {
      if (this.$router.currentRoute.path !== "/") this.$router.push("/");
    },
  },
});
</script>

<style lang="scss">
.navbar-container {
  position: sticky;
  top: 0;
  background: white;
  z-index: 100;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1), 0 3px 10px 0 rgba(0, 0, 0, 0.08);
}

.navbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1920px;
  margin: 0 auto;
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
