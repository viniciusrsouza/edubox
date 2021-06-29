import Vue from "vue";
import Vuex from "vuex";

import navbar from "./navbar";
import snackbar from "./snackbar";
import global_settings from "./global_settings";
import course from "./course";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: { navbar, global_settings, snackbar, course },
});
