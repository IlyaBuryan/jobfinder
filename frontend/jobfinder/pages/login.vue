<template>
  <body class="login-page">
    <main>
      <div class="login-block">
        <img class="logo-form" src="/_nuxt/assets/img/logo.png" alt="" />
        <h1>Авторизация</h1>

        <form>
          <div class="form-group">
            <div class="input-group">
              <span class="input-group-addon"><i class="ti-user"></i></span>
              <input
                v-model="username"
                type="text"
                class="form-control"
                placeholder="Username"
              />
            </div>
          </div>
          <hr />
          <div class="form-group">
            <div class="input-group">
              <span class="input-group-addon"><i class="ti-unlock"></i></span>
              <input
                v-model="password"
                type="password"
                class="form-control"
                placeholder="Password"
              />
            </div>
          </div>
          <button class="btn btn-primary btn-block" v-on:click="auth">
            Авторизоваться
          </button>

          <div class="login-footer">
            <h6>или залогиниться через</h6>
            <ul class="social-icons">
              <li>
                <a class="facebook" href="#"><i class="fa fa-facebook"></i></a>
              </li>
              <li>
                <a class="twitter" href="#"><i class="fa fa-twitter"></i></a>
              </li>
              <li>
                <a class="linkedin" href="#"><i class="fa fa-linkedin"></i></a>
              </li>
            </ul>
          </div>
        </form>
      </div>
      <div class="login-links">
        <nuxt-link class="pull-left" to="/pass-restore"
          >Забыли пароль?</nuxt-link
        >
        <nuxt-link class="pull-right" to="/register"
          >Зарегистрируйтесь</nuxt-link
        >
      </div>
    </main>
  </body>
</template>

<script>
import { baseUrl, decode } from "../store/constants.js";
import Cookies from "universal-cookie";
import axios from "axios";

export default {
  layout: "login_reg",

  data: () => ({
    username: "",
    password: "",
  }),
  methods: {
    auth(event) {
      console.log("Начинаем отправлять запрос");
      event.preventDefault();
      axios
        .post(`${baseUrl()}/token/`, {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          const token = response.data;
          this.set_token(token.access);
          console.log(token);
          console.log("Ура мы авторизовались!");
        })
        .catch((error) => console.log(error));
    },

    set_token(token) {
      const cookies = new Cookies();
      cookies.set("token", token, { path: "/" });
      this.$router.replace("/");
    },
  },
};
</script>

<style scoped lang="scss">
.login-page main {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  width: 100%;
  max-width: 460px;
}
.logo-form {
  width: 360px;
}
.login-block {
  background-color: #fff;
  padding: 60px;
  box-shadow: 0 3px 50px 0 rgb(0 0 0 / 10%);
  text-align: center;
  border-radius: 5px;
}
.login-block .form-group {
  margin-top: 15px;
  margin-bottom: 15px;
}
.btn-primary {
  background-color: #29aafe;
  border-color: #29aafe !important;
}
*,
:after,
:before {
  box-sizing: border-box;
}
.login-block h1 {
  font-family: Open Sans, sans-serif;
  font-size: 22px;
  color: #96a2b2;
  margin-bottom: 60px;
  margin-top: 40px;
}
.login-links {
  padding: 15px 5px 0;
  font-size: 13px;
  color: #96a2b2;
}

.text-center {
  text-align: center;
}
.btn-primary {
  background-color: #29aafe;
  border-color: #29aafe !important;
}
.btn {
  margin-top: 50px;
  width: 100%;
  height: 44px;
  line-height: 44px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-radius: 3px;
  padding: 0 30px;
  color: #fff;
  transition: 0.2s linear;
}
[class*=" ti-"],
[class^="ti-"] {
  font-family: themify;
  font-style: normal;
}
.login-block .input-group-addon {
  color: #29aafe;
  font-size: 19px;
  opacity: 0.5;
  background-color: transparent;
  border: none;
  padding: 6px 12px;
}
.login-block .form-control {
  background-color: transparent;
  border: none;
}
.input-group {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}
.ti-user:before {
  content: "\263A";
}
.ti-unlock:before {
  content: "\1F511";
}
.login-footer {
  margin-top: 60px;
  opacity: 0.5;
  transition: opacity 0.3s ease-in-out;
}
.login-block h6 {
  font-size: 11px;
  text-transform: uppercase;
  margin-top: 0;
}
.social-icons {
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}
.social-icons a {
  background-color: #eceeef;
  color: #818a91;
  font-size: 16px;
  display: inline-block;
  line-height: 44px;
  width: 44px;
  height: 44px;
  text-align: center;
  margin-right: 8px;
  border-radius: 100%;
  transition: all 0.2s linear;
}
.social-icons li {
  display: inline-block;
  margin-bottom: 4px;
}
.social-icons a.facebook:hover {
  background-color: #3b5998;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-linkedin:before {
  content: "\f0e1";
}
a {
  color: #337ab7;
  text-decoration: none;
}
.social-icons a.facebook:hover {
  background-color: #3b5998;
}
.social-icons a.twitter:hover {
  background-color: #00aced;
}
.social-icons a.linkedin:hover {
  background-color: #007bb6;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
</style>
