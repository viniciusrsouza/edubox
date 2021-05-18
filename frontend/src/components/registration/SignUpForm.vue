<template>
  <v-form>
    <v-card-text>
      <LogoAndName />
      <TextForm :icon="'mdi-account'" :inputPlaceholder="'Full Name'" />
      <TextForm :icon="'mdi-at'" :inputPlaceholder="'Email'" />
      <TextForm :icon="'mdi-lock'" :inputPlaceholder="'Password'" />
      <TextForm :icon="'mdi-lock'" :inputPlaceholder="'Confirm Password'" />
      <v-checkbox v-model="checkbox">
        <template v-slot:label>
          <div>
            I agree with the
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <a
                  target="_blank"
                  href="https://github.com/viniciusrsouza/edubox"
                  @click.stop
                  v-on="on"
                >
                  therms and conditions
                </a>
              </template>
              Opens in new window
            </v-tooltip>
            of the platform
          </div>
        </template>
      </v-checkbox>
      <v-btn elevation="2" x-large color="#3B5C78" style="width: 100%" class="white--text">Sign Up</v-btn>
    </v-card-text>
  </v-form>
</template>

<script lang="ts">
import Vue from "vue";
import LogoAndName from "../LogoAndName.vue";
import TextForm from "./TextForm.vue";
export default Vue.extend({
  name: "SignUpForm",
  components: {
    LogoAndName,
    TextForm,
  },
});
</script>

<style scoped>
</style>