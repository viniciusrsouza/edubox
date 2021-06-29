import { Location } from "vue-router";
import router from ".";

export function redirect(
  { path, query, params }: Location,
  pushing = true
): void {
  if (pushing) {
    router.push({ path, query, params });
    return;
  }
  router.replace({ path, query, params });
}
