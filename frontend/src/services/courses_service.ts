import api from "./api_axios";

const CoursesService = {
  async getAll() {
    const params = { limit: 100 };
    return await api.get("courses", { params });
  },

  async create(payload: CreatePayload) {
    await api.post("courses/", payload);
    return { success: true };
  },
};

interface CreatePayload {
  title: string;
  description: string;
}

export default CoursesService;
