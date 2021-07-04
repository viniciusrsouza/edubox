export interface Assignment {
  id?: number;
  deadline?: string;
}

export interface Post {
  id: number;
  author:
    | number
    | {
        id: number;
        email: string;
        name: string;
      };
  assignment: null | Assignment;
  course: number;
  title: string;
  text: string;
  created_at?: string;
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

export interface Member {
  id: number;
  email: string;
  name: string;
  picture: string;
}

export as namespace models;
