import store from "@/store";
import api from "./api_axios";

const service: services.AssignmentService = {
  _getCourse() {
    const state: any = store.state;
    return state.course.course as models.Course;
  },
  async getAll() {
    const course = this._getCourse();
    const params = { limit: 100 };
    return (await api.get(`courses/${course.id}/assignments`, { params })).data;
  },

  async get(id) {
    const course = this._getCourse();
    return (await api.get(`courses/${course.id}/assignments${id}`)).data;
  },

  async create(payload) {
    const course = this._getCourse();
    return (await api.post(`courses/${course.id}/assignments/`, payload)).data;
  },
};

export default service;
