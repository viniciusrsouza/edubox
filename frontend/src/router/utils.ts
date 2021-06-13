import router from ".";

export function redirect({ path, query, params }: endpoint, pushing = true) {
  if (pushing) router.push({ path, query, params });
  router.replace({ path, query, params });
}

interface endpoint {
  path?: string;
  query?: any;
  params?: any;
}
