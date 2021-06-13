import en_US from "./en-US";
import pt_BR from "./pt-BR";

const t = (key: string): string => {
  // TODO add language selector
  const lang = en_US;
  return lang.get(key) || "";
};

export default t;
