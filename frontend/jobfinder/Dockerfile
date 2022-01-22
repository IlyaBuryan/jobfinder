FROM node:16-alpine
WORKDIR /client
COPY . /client/
RUN npm install
ENV NUXT_HOST 0.0.0.0
ENV NUXT_PORT=3000
