import { Themes, Languages } from "@/constants";
import { Commit, Value } from "./types";

const global_settings = {
  state: {
    language: Languages.EN_US,
    theme: Themes.LIGHT,
  },
  mutations: {
    set_language(state: State, value: Languages): void {
      state.language = value;
    },
  },
  actions: {
    set_language(
      { commit }: Commit<Languages>,
      { value }: Value<Languages>
    ): void {
      commit("set_language", value);
    },
  },
};

export interface State {
  language: Languages;
  theme: Themes;
}

export default global_settings;
