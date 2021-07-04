import store from "@/store";
import api from "./api_axios";

const service: services.MemberService = {
  _getCourse() {
    const state: any = store.state;
    return state.course.course as models.Course;
  },
  async getAll() {
    const course = this._getCourse();
    // const params = { limit: 100 };
    return (await api.get(`memberlist/${course.id}`)).data;
  },
};

export interface Member {
  id: number;
  email: string;
  name: string;
  picture: string;
}

export default service;
