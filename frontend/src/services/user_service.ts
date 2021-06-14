import api from "./api_axios";

const UserService = {
  async fetchUser(): Promise<UserResponse> {
    return (await api.get("users/")).data;
  },
};

interface UserResponse {
  id: number;
  email: string;
  name: string;
}

export default UserService;
