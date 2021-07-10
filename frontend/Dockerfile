FROM node:14.4.0-alpine3.10

WORKDIR /usr/src/frontend

COPY ["package.json", "./"]

RUN npm install

COPY . .

EXPOSE 3000