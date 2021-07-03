// eslint-disable-next-line @typescript-eslint/no-unused-vars
import Vue from "vue";

declare module "vue/types/vue" {
  interface Vue {
    $services: {
      assignment: services.AssignmentService;
      course: services.CourseService;
      auth: services.AuthService;
      user: services.UserService;
    };
  }
}
