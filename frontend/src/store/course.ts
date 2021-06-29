import { Course } from "@/services/courses_service";
import { Commit } from "./types";

const INITIAL_STATE: Course | undefined = undefined;

const course = {
  namespaced: true,
  state: {
    course: INITIAL_STATE,
  },
  mutations: {
    set_course(state: State, value: Course | undefined): void {
      state.course = value;
    },
  },
  actions: {
    set_course({ commit }: Commit<Course>, value: Course): void {
      commit("set_course", value);
    },
  },
};

export interface State {
  course: Course | undefined;
}

export default course;
