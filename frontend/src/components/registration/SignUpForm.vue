<template>
  <v-form>
    <v-card-text>
      <LogoAndName />
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
      />
      <TextForm
        :icon="'mdi-lock'"
        :inputPlaceholder="t('confirm_password')"
        :setValue="(e) => (confirm_password = e)"
      />
      <v-checkbox>
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
      <v-btn
        elevation="2"
        x-large
        color="#3B5C78"
        style="width: 100%"
        class="white--text"
        @click="signup"
        >Sign Up</v-btn
      >
    </v-card-text>
  </v-form>
</template>

<script lang="ts">
import Vue from "vue";
import LogoAndName from "./LogoAndName.vue";
import TextForm from "./TextForm.vue";
import t from "../../locale";
import api from "../../services/api_axios";

export default Vue.extend({
  name: "SignUpForm",
  methods: {
    t,
    signup() {
      const payload = {
        full_name: this.full_name,
        email: this.email,
        password: this.password,
        confirm_password: this.confirm_password,
      };
      api.post("/users/create/", payload).then((res) => console.log(res));
    },
  },
  components: {
    LogoAndName,
    TextForm,
  },
  data: () => ({
    full_name: String,
    email: String,
    password: String,
    confirm_password: String,
  }),
});
</script>

<style scoped></style>
