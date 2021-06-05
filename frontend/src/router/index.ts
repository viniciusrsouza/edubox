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
    meta: { requiresAuth: true },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: { requiresUnauth: true },
  },
  {
    path: "/signup",
    name: "Sign Up",
    component: SignUp,
    meta: { requiresUnauth: true },
  },
  {
    path: "/creation",
    name: "New course",
    component: Creation,
    meta: { requiresAuth: true },
  },
  {
    path: "/course/:id",
    name: "Course Detail",
    component: CourseDetail,
    children: [
      {
        path: "",
        component: PostListContent,
        meta: { requiresAuth: true },
      },
      {
        path: "user",
        component: PersonListContent,
        meta: { requiresAuth: true },
      },
      {
        path: "activity",
        component: PersonListContent,
        meta: { requiresAuth: true },
      },
    ],
    meta: { requiresAuth: true },
  },
  {
    path: "/course_people",
    name: "Course People",
    component: CoursePeople,
    meta: { requiresAuth: true },
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

router.beforeEach((to, _, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!localStorage.getItem("access")) {
      next({
        path: "/login",
        query: {
          nextUrl: to.fullPath,
        },
      });
    }
  } else if (to.matched.some((record) => record.meta.requiresUnauth)) {
    if (localStorage.getItem("access")) next({ path: "/" });
  }
  next();
});

export default router;
