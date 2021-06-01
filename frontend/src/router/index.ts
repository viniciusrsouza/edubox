import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import SignUp from "../views/SignUp.vue";
import Creation from "../views/Creation.vue";
import CourseDetail from "../views/CourseDetail.vue";
import CoursePeople from "../views/CoursePeople.vue";
import PersonListContent from "../components/CourseDetail/PersonList/PersonListContent.vue";
import PostListContent from "../components/CourseDetail/PostList/PostListContent.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/signup",
    name: "Sign Up",
    component: SignUp,
  },
  {
    path: "/creation",
    name: "New course",
    component: Creation,
  },
  {
    path: "/course/:id",
    name: "Course Detail",
    component: CourseDetail,
    children: [
      {
        path: "",
        component: PostListContent,
      },
      {
        path: "user",
        component: PersonListContent,
      },
    ],
  },
  {
    path: "/course_people",
    name: "Course People",
    component: CoursePeople,
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router;
