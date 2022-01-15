FROM node:16-alpine
WORKDIR /client
COPY . /client/
RUN npm install
RUN npm install -g @vue/cli
CMD ["npm", "run", "serve"]