export interface Commit<T> {
  commit(type: string, value: T): unknown;
}

export interface Value<T> {
  value: T;
}
