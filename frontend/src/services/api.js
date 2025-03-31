import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

// Auth APIs
export const loginUser = (data) => api.post("/auth/login", data);
export const signupUser = (data) => api.post("/auth/signup", data);

// Summarization API
export const summarizeDocument = (formData) =>
  api.post("/summarize", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

// Fetch History
export const fetchHistory = () => api.get("/summarize/history");

export default api;
