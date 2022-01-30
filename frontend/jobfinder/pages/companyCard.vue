<template>
  <div class="wrapper">
    <form class="form-data">
      <!-- Page header -->
      <header class="page-header">
        <div class="container page-name">
          <h1 class="text-center">Добавьте свою компанию</h1>
          <p class="lead text-center">
            Создайте профиль своей компании и сделайте его доступным онлайн.
          </p>
        </div>

        <div class="container" v-if="is_authenticated">
          <div class="row">
            <div class="col-xs-12">
              <div class="row">
                <div class="col-xs-12 col-sm-4 col-lg-2">
                  <div class="form-group">
                    <input
                      type="file"
                      class="dropify"
                      data-default-file="assets/img/logo-default.png"
                    />
                    <span class="help-block">Квадратный логотип</span>
                  </div>
                </div>

                <div class="col-xs-12 col-sm-8 col-lg-10">
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control input-lg"
                      placeholder="Имя компании"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Сфера деятельности (например, интернет и программное обеспечение)"
                    />
                  </div>

                  <div class="form-group">
                    <textarea
                      class="form-control"
                      rows="3"
                      placeholder="Короткое описание"
                    ></textarea>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-xs-12">
              <div class="row">
                <div class="form-group col-xs-12 col-sm-6 col-md-4">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon"
                      ><i class="fa fa-map-marker"></i
                    ></span>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Месторасположение"
                    />
                  </div>
                </div>

                <div class="form-group col-xs-12 col-sm-6 col-md-4">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon"
                      ><i class="fa fa-users"></i
                    ></span>
                    <select class="form-control selectpicker">
                      <option>0 - 9</option>
                      <option selected>10 - 99</option>
                      <option>100 - 999</option>
                      <option>1,000 - 9,999</option>
                      <option>10,000 - 99,999</option>
                      <option>100,000 - 999,999</option>
                    </select>
                    <span class="input-group-addon"
                      >Количество сотрудников</span
                    >
                  </div>
                </div>

                <div class="form-group col-xs-12 col-sm-6 col-md-4">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon"
                      ><i class="fa fa-globe"></i
                    ></span>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Адрес сайта"
                    />
                  </div>
                </div>

                <div class="form-group col-xs-12 col-sm-6 col-md-4">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon"
                      ><i class="fa fa-birthday-cake"></i
                    ></span>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Год основания"
                    />
                  </div>
                </div>

                <div class="form-group col-xs-12 col-sm-6 col-md-4">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon"
                      ><i class="fa fa-phone"></i
                    ></span>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Номер телефона"
                    />
                  </div>
                </div>

                <div class="form-group col-xs-12 col-sm-6 col-md-4">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon"
                      ><i class="fa fa-envelope"></i
                    ></span>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Email"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="button-group">
            <div class="action-buttons">
              <div class="upload-button">
                <button class="btn btn-block btn-primary">
                  Выберите обложку
                </button>
                <input id="cover_img_file" type="file" />
              </div>
            </div>
          </div>
        </div>
      </header>
      <!-- END Page header -->

      <!-- Submit -->
      <section>
        <div class="container" v-if="is_authenticated">
          <header class="section-header">
            <span>Вы закончили?</span>
            <h2>Отправляйте</h2>
            <p>
              Пожалуйста, проверьте информацию о своей компании еще раз и
              нажмите кнопку ниже для доступа вашей компании к ресурсам сайта.
            </p>
          </header>

          <p class="text-center">
            <button class="btn btn-success btn-xl btn-round">
              Добавьте информацию о своей компании.
            </button>
          </p>
        </div>
      </section>
      <!-- END Main container -->
    </form>
    <div class="wrapper" v-if="!is_authenticated">
      <AuthError />
    </div>
  </div>
</template>

<script>
// import baseUrl from "../store/constants.js";
import { baseUrl, decode } from "../store/constants.js";

import Cookies from "universal-cookie";
import axios from "axios";
import AuthError from "@/components/Footer.vue";

export default {
  components: { AuthError },
  layout: "company",
  data: () => ({
    is_authenticated: true,
  }),
  mounted() {
    //   this.makeGETRequest(`${API_URL}/catalogData.json`);
    this.checkAuth();
  },
  methods: {
    // is_authenticated_f() {
    //   const cookies = new Cookies();
    //   if (cookies.get("token") !== "") {
    //     this.is_authenticated = true;
    //   }
    // },
    checkAuth() {
      axios
        .post(`${baseUrl()}/token/`, {
          username: "django",
          password: "django",
        })
        .then((response) => {
          const token = response.data;
          this.set_token(token.access);
          console.log(decode(token));
        })
        .catch((error) => console.log(error));
    },
    set_token(token) {
      const cookies = new Cookies();
      cookies.set("token", token, { path: "/" });
    },
  },
};
</script>

<style scoped>
.wrapper {
  width: 100%;
  position: relative;
  z-index: -1;
  margin-bottom: 70px;
}

.page-header {
  padding-bottom: 9px;
  margin: 40px 0 20px;
  border-bottom: 1px solid #eee;
}

.page-header {
  position: relative;
  z-index: 0;
  background-attachment: fixed;
  background-size: cover;
  background-repeat: no-repeat;
  background-color: rgba(41, 170, 254, 0.8);
  margin: 0;
  padding: 0;
  margin-bottom: 120px;
  padding-top: 100px;
  border: none;
}
.page-header.bg-repeat {
  background-repeat: repeat;
  background-size: auto;
}
.page-header.bg-img:before {
  position: absolute;
  content: "";
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: -1;
  background-color: rgba(0, 0, 0, 0.65);
}
.page-header.bg-alt {
  background-color: #fafafa;
}
.page-header.size-lg {
  padding-top: 200px;
}
.page-header.title-only {
  text-align: center;
  margin-bottom: 0;
}
.page-header.title-only h1 {
  display: inline-block;
  margin: 100px 0 150px;
  padding: 20px 40px;
  color: #fff;
  border: 1px solid #fff;
}
.page-header .container {
  position: relative;
  z-index: 1;
  background-color: #fff;
  padding: 30px 30px 20px;
  box-shadow: 0 5px 25px 0 rgba(0, 0, 0, 0.07);
  -webkit-transform: translateY(84px);
  transform: translateY(84px);
}
.page-header .container.no-shadow {
  border: 1px solid #eee;
  box-shadow: none;
}
.page-header .container.no-shadow h1 {
  color: #373a3c;
}
.page-header .container.page-name {
  background-color: transparent;
  padding-left: 15px;
  padding-right: 15px;
  box-shadow: none;
  -webkit-transform: none;
  transform: none;
  color: #fff;
  padding-top: 60px;
}
.page-header .header-detail .logo {
  float: left;
  width: 92px;
  margin-right: 30px;
}
.page-header .header-detail .hgroup {
  display: inline-block;
}
.page-header .header-detail h1 {
  font-size: 40px;
  margin-top: 0;
  margin-bottom: 8px;
}
.page-header .header-detail h3 {
  font-family: Open Sans, sans-serif;
  font-size: 20px;
  letter-spacing: 0;
  margin: 0;
}
.page-header .header-detail time {
  float: right;
  font-size: 13px;
  color: #96a2b2;
  line-height: 92px;
}
.page-header .header-detail hr {
  margin-top: 20px;
  margin-bottom: 20px;
}
.page-header .header-detail .hr-lg {
  margin-top: 40px;
  margin-bottom: 40px;
}
.page-header .button-group {
  background-color: #fafafa;
  margin: -20px -30px;
  margin-top: 20px;
  padding: 20px 30px;
}
.page-header .button-group:after {
  display: table;
  content: "";
  clear: both;
}
.page-header .button-group .social-icons {
  float: left;
}
.page-header .button-group .action-buttons {
  float: right;
  line-height: 12px;
}
.page-header .button-group .btn,
.page-header .button-group .upload-button {
  margin-left: 8px;
}

.btn-round.btn {
  border-radius: 22px;
}

.btn-xl {
  height: 34px;
  line-height: 34px;
  padding: 0 20px;
  font-size: 14px;
  margin: 20px 0 0 0;
}
</style>


