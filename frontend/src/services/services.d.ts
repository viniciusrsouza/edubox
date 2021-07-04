import { PostWithAuthor } from "@/models/models";

// common
export interface SuccessResponse {
  success: boolean;
}

// generics
export interface GetListResponse<T> {
  count: number;
  results: T[];
  next?: string;
  previous?: string;
}

export interface Service<T> {
  getAll(includes: string | null = null): Promise<GetListResponse<T>>;
  get(id: string): Promise<T>;
  create(payload: T): Promise<T>;
}

// assignments
export interface AssignmentService extends Service<models.Assignment> {
  _getCourse(): models.Course;
}

export interface PostService extends Service<models.Post> {
  _getCourse(): models.Course;
}

// courses
export interface CourseService extends Service<models.Course> {
  join(code: string): any;
  getAllForSideBar(): Promise<GetListResponse<models.Course>>;
}

// auth
export interface AuthService {
  login(payload: models.LoginPayload): Promise<SuccessResponse>;
  signup(payload: models.SignupPayload): Promise<SuccessResponse>;
}

// user
export interface UserService {
  fetchUser(): Promise<models.User>;
}

// member
export interface MemberService {
  _getCourse(): models.Course;
  getAll(): Promise<GetListResponse<T>>;
}

export as namespace services;
