class API {
  url: string;
  constructor() {
    this.url = process.env.API_URL || "http://localhost:5001/api";
  }

  getURL(endpoint: string, params?: string) {
    const url = new URL(this.url);
    url.pathname += `/${endpoint}` || "";
    if (params) url.search = new URLSearchParams(params).toString();
    return url.href;
  }

  getHeaders() {
    const headers: any = {
      "Content-Type": "application/json",
    };
    const token = localStorage.getItem("access");
    if (token) {
      headers.Authorization = `Bearer ${token}`;
    }
    return headers;
  }

  async post(endpoint: string, payload: any) {
    const res = await fetch(this.getURL(endpoint), {
      method: "POST",
      headers: this.getHeaders(),
      body: JSON.stringify(payload),
    });
    return res.json();
  }

  async get(endpoint: string, params: any) {
    const res = await fetch(this.getURL(endpoint, params), {
      method: "GET",
      headers: this.getHeaders(),
    });
    return res.json();
  }
}

const api = new API();

export default api;
