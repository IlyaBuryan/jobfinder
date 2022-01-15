FROM node:15-alpine
RUN npm set strict-ssl false
WORKDIR /client
COPY . /client/
RUN npm install
RUN npm install -g http-server
CMD ["npm", "run", "serve"]