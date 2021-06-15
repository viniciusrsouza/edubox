<template>
  <v-form>
    <v-card-text>
      <LogoAndName />
      <TextForm
        :icon="'mdi-account'"
        :inputPlaceholder="'Email'"
        :type="'email'"
        :id="'email'"
        v-model="email"
      />
      <TextForm
        :icon="'mdi-lock'"
        :inputPlaceholder="'Password'"
        :type="'password'"
        :id="'pw'"
        v-model="password"
      />
      <v-btn
        elevation="2"
        x-large
        color="#3B5C78"
        style="width: 100%"
        class="white--text"
        @click="login"
        >Sign In</v-btn
      >
      <div class="separator my-10" />
      <div class="sign-up-container">
        <div class="text-sign-up">Not registered yet?</div>
        <v-btn
          elevation="2"
          x-large
          color="#3B5C78"
          style="width: 100%"
          class="white--text"
          @click="redirect"
        >
          Sign Up
        </v-btn>
      </div>
    </v-card-text>
  </v-form>
</template>

<script lang="ts">
import Vue from "vue";
import LogoAndName from "./LogoAndName.vue";
import TextForm from "./TextForm.vue";
import AuthService from "../../services/auth_service";
export default Vue.extend({
  name: "LoginForm",
  components: {
    LogoAndName,
    TextForm,
  },
  methods: {
    login() {
      let options = {
        email: this.email,
        password: this.password,
      };

      AuthService.login(options)
        .then(({ success }) => {
          if (success) this.$router.push("/");
        })
        .catch((err) => {
          console.log(err.response.data);
        });
    },
    teste(a: any) {
      console.log({ a });
    },
    redirect() {
      this.$router.push("/signup");
    },
  },
  data: () => ({
    email: "",
    password: "",
  }),
});
</script>

<style scoped lang="scss">
.separator {
  width: 80%;
  background-color: $primary;
  margin: auto;
  height: 1px;
}

.text-sign-up {
  color: $primary;
  font-weight: 500;
  width: 100%;
  text-align: center;
  padding-bottom: 0.5em;
}
</style>
