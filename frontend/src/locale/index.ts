import en_US from "./en-US";

const t = (key: string) => {
  // TODO add language selector
  const lang = en_US;
  return lang.has(key) ? lang.get(key) : "";
};

export default t;
