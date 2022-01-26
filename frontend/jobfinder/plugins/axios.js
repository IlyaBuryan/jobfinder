import Vue from 'vue';
import axios from 'axios';
axios.interceptors.request.use((config) => {
  // Do something before request is sent
  return config;
}, function (error) {
  // Do something with request error
  return Promise.reject(error);
});
Vue.use(axios);
