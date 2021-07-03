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
  getAll(): Promise<GetListResponse<T>>;
  get(id: string): Promise<T>;
  create(payload: T): Promise<T>;
}

// assignments
export interface AssignmentService extends Service<models.Assignment> {
  _getCourse(): models.Course;
}

// courses
export interface CourseService extends Service<models.Course> {
  join(code: string): any;
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

export as namespace services;
