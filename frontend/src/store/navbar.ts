import { Commit, Value } from "./types";

const navbar = {
  state: {
    search: "",
  },
  mutations: {
    update_search: (state: State, value: string): void => {
      state.search = value;
    },
  },
  actions: {
    update_search({ commit }: Commit<string>, { value }: Value<string>): void {
      commit("update_search", value);
    },
  },
};

interface State {
  search: string;
}

export default navbar;
