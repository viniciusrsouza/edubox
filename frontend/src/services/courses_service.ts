import api from "./api_axios";

const service: services.CourseService = {
  async getAll() {
    const params = { limit: 100 };
    return (await api.get("courses/", { params })).data;
  },

  async get(id: string) {
    return (await api.get(`courses/${id}`)).data;
  },

  async create(payload) {
    return (await api.post("courses/", payload)).data;
  },

  async join(code) {
    return (await api.post(`membership/${code}`)).data;
  },
};

export interface Course {
  id: number;
  title: string;
  description: string;
  favorite: boolean;
  created_at: string;
  owner: number;
  code: string;
  role: string;
}

export default service;
