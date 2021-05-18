const axios = require("axios").default;

const instance = axios.create({
  baseURL: "http://localhost:5001/api/",
  timeout: 1000,
});

export default instance;
