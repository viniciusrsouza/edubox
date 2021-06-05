const navbar = {
  state: {
    search: "",
  },
  mutations: {
    update_search: (state: State, value: string) => {
      state.search = value;
    },
  },
  actions: {
    update_search: ({ commit }: any, { value }: any) => {
      commit("update_search", value);
    },
  },
};

interface State {
  search: string;
}

export default navbar;
