import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import SignUp from '../views/SignUp.vue';
import Creation from "../views/Creation.vue";
import CourseDetail from '../views/CourseDetail.vue';

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
    path: '/signup',
    name: 'Sign Up',
    component: SignUp
  },
  {
    path: '/creation',
    name: 'New course',
    component: Creation
  },
  {
    path: '/course_detail',
    name: 'Course Detail',
    component: CourseDetail
  }
];

const router = new VueRouter({
  routes,
});

export default router;
