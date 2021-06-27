/* eslint-disable @typescript-eslint/no-explicit-any */
import { Languages } from "@/constants";
import store from "@/store";
import en_US from "./en-US.json";
import pt_BR from "./pt-BR.json";

function t(path: string): string {
  const language: LanguageLookup = getLanguage();
  const tokens = path.split(".");
  const key = tokens.pop();

  if (!key) return "";

  let obj: LanguageLookup = language;
  tokens.forEach((token) => {
    if (!obj[token]) return "";
    obj = obj[token];
  });
  return obj[key] || "";
}

function getLanguage(): LanguageLookup {
  const state: any = store.state;
  const language: Languages = state.global_settings.language;

  switch (language) {
    case Languages.EN_US:
      return en_US;
    case Languages.PT_BR:
      return pt_BR;
    default:
      return en_US;
  }
}

interface LanguageLookup {
  [key: string]: any;
}

export default t;
