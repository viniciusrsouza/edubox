import t from "@/locale";
import pupa from "pupa";
import { PluginObject } from "vue";
import { VueConstructor } from "vue/types/umd";

const Locale: PluginObject<never> = {
  install(Vue: VueConstructor) {
    Vue.prototype.$t = t;
    Vue.prototype.$t_f = function <T>(path: string, object: T) {
      return pupa(t(path), object);
    };
  },
};

export default Locale;
