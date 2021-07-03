export interface Assignment {
  id: number;
  title: string;
  course?: boolean;
  description?: string;
  deadline?: string;
  grade?: number;
}

export interface Course {
  id: number;
  title: string;
  description: string;
  favorite: boolean;
  created_at: string;
  owner: number;
  code: string;
  role: string;
}

export interface LoginPayload {
  email: string;
  password: string;
}

export interface SignupPayload {
  name: string;
  email: string;
  password: string;
  confirm_password: string;
}

export interface User {
  id: number;
  email: string;
  name: string;
}

export as namespace models;
