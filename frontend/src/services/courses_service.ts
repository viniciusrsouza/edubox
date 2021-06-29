import api from "./api_axios";

const CoursesService = {
  async getAll(): Promise<GetAllResponse> {
    const params = { limit: 100 };
    return (await api.get("courses/", { params })).data;
  },

  async get(id: string): Promise<Course> {
    return (await api.get(`courses/${id}`)).data;
  },

  async create(payload: CreatePayload) {
    await api.post("courses/", payload);
    return { success: true };
  },

  async join(code: string) {
    return (await api.post(`membership/${code}`)).data;
  },
};

interface CreatePayload {
  title: string;
  description: string;
}

interface GetAllResponse {
  count: number;
  results: [];
  next?: string;
  previous?: string;
}

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

export default CoursesService;
