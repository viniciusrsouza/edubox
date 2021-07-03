import api from "./api_axios";

const service: services.AuthService = {
  async login(payload) {
    const res = await api.post("token/", payload);

    localStorage.setItem("access", res.data.access);
    localStorage.setItem("refresh", res.data.refresh);
    return { success: true };
  },

  async signup(payload) {
    await api.post("users/", payload);
    return { success: true };
  },
};

export default service;
