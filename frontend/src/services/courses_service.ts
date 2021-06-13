import api from "./api_axios";

const CoursesService = {
  async getAll(): Promise<GetAllResponse> {
    const params = { limit: 100 };
    return await api.get("courses/", { params });
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

interface GetAllResponse {
  data: {
    results: [];
  };
}

export default CoursesService;
