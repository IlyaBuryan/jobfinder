FROM node:16
WORKDIR /client
COPY . /client/
WORKDIR /client
RUN npm install
ENV NUXT_HOST 0.0.0.0
ENV NUXT_PORT=3000
CMD ["npm", "run", "dev"]
