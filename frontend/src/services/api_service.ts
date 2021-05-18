class API {
  baseUrl = "http://localhost:5001/api";

  async post(endpoint: string, body: Record<string, unknown>) {
    return fetch(`${this.baseUrl}${endpoint}/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
  }
}

const api = new API();
export default api;
