FROM node:14.16.0-alpine3.10

RUN mkdir -p /app

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .