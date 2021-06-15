const snackbar: SnackbarModule = {
  state: {
    text: "",
    show: false,
  },
  mutations: {
    update_text: (state: State, value: string) => {
      state.text = value;
    },
    update_show: (state: State, value: boolean) => {
      state.show = value;
    },
  },
  actions: {
    show_snackbar: ({ commit }: any, { value }: any) => {
      commit("update_text", value);
      commit("update_show", true);
    },
    dismiss_snackbar: ({ commit }: any) => {
      commit("update_text", "");
      commit("update_show", false);
    },
  },
};

interface State {
  text: string;
  show: boolean;
}

interface SnackbarModule {
  state: State;
  mutations: any;
  actions: any;
}

export default snackbar;
