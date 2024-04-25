import axios, { AxiosInstance } from "axios";

const customFetch: AxiosInstance = axios.create({
  baseURL: "http://localhost:5000",
  timeout: 10000000,
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true,
});

export default customFetch;
