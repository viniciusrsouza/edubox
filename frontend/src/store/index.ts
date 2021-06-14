import Vue from "vue";
import Vuex from "vuex";

import navbar from "./navbar";
import global_settings from "./global_settings";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: { navbar, global_settings },
});
