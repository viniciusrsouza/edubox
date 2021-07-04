import store from "@/store";
import api from "./api_axios";

const service: services.MemberService = {
  _getCourse() {
    const state: any = store.state;
    return state.course.course as models.Course;
  },
  async getAll() {
    const course = this._getCourse();
    const params = { limit: 100 };
    return (await api.get(`memberlist/${course.id}/`, { params })).data;
  },
};

export default service;
