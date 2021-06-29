import api from "@/services/api_axios";
import { AxiosRequestConfig, AxiosResponse } from "axios";

const APIHelper = {
  async fetch<T>(
    method: Methods,
    endpoint: string,
    config: AxiosRequestConfig | undefined
  ) {
    let success = false,
      data: T | undefined = undefined,
      error: APIResponseError | undefined = undefined,
      response: AxiosResponse<T> | undefined;

    try {
      switch (method) {
        case Methods.GET:
          response = await api.get<T>(endpoint, config);
          break;
        case Methods.HEAD:
          response = await api.head<T>(endpoint, config);
          break;
        case Methods.POST:
          response = await api.post<T>(endpoint, config);
          break;
        case Methods.PUT:
          response = await api.put<T>(endpoint, config);
          break;
        case Methods.DELETE:
          response = await api.delete<T>(endpoint, config);
          break;
        case Methods.OPTIONS:
          response = await api.options<T>(endpoint, config);
          break;
        case Methods.PATCH:
          response = await api.patch<T>(endpoint, config);
          break;
      }
      data = response?.data;
      success = true;
    } catch (err) {
      error = {
        code: 1,
        message: "failed to fetch",
      };
      success = false;
    }
    const apiResponse: APIResponse<T> = {
      success: success,
      data: data,
      error: error,
    };
    return apiResponse;
  },
};

export interface APIResponseError {
  code?: number;
  message?: string;
}

export interface APIResponse<T> {
  success?: boolean;
  data?: T;
  error?: APIResponseError;
}

enum Methods {
  GET,
  HEAD,
  POST,
  PUT,
  DELETE,
  OPTIONS,
  PATCH,
}
