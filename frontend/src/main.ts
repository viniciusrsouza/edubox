import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import Locale from "./plugins/locale";
import Services from "./plugins/services";

Vue.use(Services);
Vue.use(Locale);

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
