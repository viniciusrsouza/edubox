import services from "@/services";
import { PluginObject } from "vue";
import { VueConstructor } from "vue/types/umd";

const Services: PluginObject<never> = {
  install(Vue: VueConstructor) {
    Vue.prototype.$services = services;
  },
};

export default Services;
