import store from "@/store";
import api from "./api_axios";

const service: services.PostService = {
    _getCourse() {
        const state: any = store.state;
        return state.course.course as models.Course;
    },
    async getAll() {
        const course = this._getCourse();
        const params = { limit: 100 };
        return (await api.get(`posts/${course.id}/`, { params })).data;
    },
    async get(id) {
        const course = this._getCourse();
        return (await api.get(`posts/${course.id}/${id}`)).data;
    },
    async create(payload) {
        const course = this._getCourse();
        return (await api.post(`posts/`, payload)).data;
    },
};

export default service;