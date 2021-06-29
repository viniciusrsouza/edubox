import Vue from "vue";
import Vuex from "vuex";

import navbar, { State as NavbarState } from "./navbar";
import snackbar, { State as SnackbarState } from "./snackbar";
import global_settings, {
  State as GlobalSettingsState,
} from "./global_settings";
import course, { State as CourseState } from "./course";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: { navbar, global_settings, snackbar, course },
});

export interface StoreState {
  navbar: NavbarState;
  snackbar: SnackbarState;
  global_settings: GlobalSettingsState;
  course: CourseState;
}
