<template>
  <v-form>
    <v-card-text>
      <LogoAndName />
      <TextForm
        :icon="'mdi-account'"
        :inputPlaceholder="t('Auth.FullName')"
        v-model="full_name"
      />
      <TextForm
        :icon="'mdi-at'"
        :inputPlaceholder="t('Auth.Email')"
        v-model="email"
      />
      <TextForm
        :icon="'mdi-lock'"
        :inputPlaceholder="t('Auth.Password')"
        type="password"
        v-model="password"
      />
      <TextForm
        :icon="'mdi-lock'"
        :inputPlaceholder="t('Auth.ConfirmPassword')"
        type="password"
        v-model="confirm_password"
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
        >{{ t("Auth.SignUp") }}</v-btn
      >
    </v-card-text>
    <div class="sign-in-container">
      <div class="text-sign-in">Already have an account?</div>
      <v-btn
        elevation="2"
        x-large
        color="#3B5C78"
        style="width: 100%"
        class="white--text"
        @click="redirect"
      >
        Login
      </v-btn>
    </div>
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
        name: this.full_name,
        email: this.email,
        photo: null,
        password: this.password,
        confirm_password: this.confirm_password,
      };
      AuthService.signup(payload)
        .then(({ success }) => {
          if (success)
            AuthService.login({
              email: payload.email,
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
    agreeChange(checked: boolean) {
      this.agree_with_terms = checked;
    },
    allFieldsValid(): boolean {
      return !!(
        this.full_name &&
        this.email &&
        this.password &&
        this.confirm_password &&
        this.agree_with_terms
      );
    },
    redirect() {
      this.$router.push("/login");
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

<style scoped lang="scss">
.text-sign-in {
  color: $primary;
  font-weight: 500;
  width: 100%;
  text-align: center;
  padding-bottom: 0.5em;
}
</style>
