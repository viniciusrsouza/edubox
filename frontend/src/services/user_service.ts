import api from "./api_axios";

const service: services.UserService = {
  async fetchUser() {
    return (await api.get("users/")).data;
  },
};

export default service;
