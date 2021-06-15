import api from "./api_axios";

const AuthService = {
  async login(payload: LoginPayload) {
    const res = await api.post("token/", payload);

    localStorage.setItem("access", res.data.access);
    localStorage.setItem("refresh", res.data.refresh);
    return { success: true };
  },

  async signup(payload: SignupPayload) {
    await api.post("users/", payload);
    return { success: true };
  },
};

interface LoginPayload {
  email: string;
  password: string;
}

interface SignupPayload {
  name: string;
  email: string;
  password: string;
  confirm_password: string;
}

export default AuthService;
