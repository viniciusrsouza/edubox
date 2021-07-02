FROM node:16.3.0-alpine3.13

RUN mkdir -p /app
WORKDIR /app
COPY package*.json ./

RUN apk add --no-cache --virtual .gyp \
  python3 \
  make \
  g++ \
  && npm install \
  && apk del .gyp

COPY . .