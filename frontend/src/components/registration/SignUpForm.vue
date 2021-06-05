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
        type="password"
      />
      <TextForm
        :icon="'mdi-lock'"
        :inputPlaceholder="t('confirm_password')"
        :setValue="(e) => (confirm_password = e)"
        type="password"
      />
      <v-checkbox @change="agreeChange">
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
        :disabled="!allFieldsValid()"
        @click="signup"
        >{{ t("sign_up") }}</v-btn
      >
    </v-card-text>
  </v-form>
</template>

<script lang="ts">
import Vue from "vue";
import LogoAndName from "./LogoAndName.vue";
import TextForm from "./TextForm.vue";
import t from "../../locale";
import AuthService from "../../services/auth_service";

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
      AuthService.signup(payload)
        .then(({ success }) => {
          if (success)
            AuthService.login({
              username: payload.email,
              password: payload.password,
            })
              .then((res) => {
                if (res.success) this.$router.push("/");
              })
              .catch((err) => {
                console.log(err.response.data);
              });
        })
        .catch((err) => {
          console.log(err.response.data);
        });
    },
    agreeChange(checked) {
      this.agree_with_terms = checked;
    },
    allFieldsValid(): boolean {
      return (
        this.full_name &&
        this.email &&
        this.password &&
        this.confirm_password &&
        this.agree_with_terms
      );
    },
  },
  components: {
    LogoAndName,
    TextForm,
  },
  data: () => ({
    full_name: "",
    email: "",
    password: "",
    confirm_password: "",
    agree_with_terms: false,
  }),
});
</script>

<style scoped></style>
