<template>
  <div class="wrapper">
    <form class="form-data">
      <header class="page-header">
        <div class="container page-name">
          <h1 class="text-center">Добавьте информацию о себе</h1>
          <p class="lead text-center">Расскажите больше о себе.</p>
        </div>

        <div class="container" v-if="permission == 'yes'">
          <p v-if="error[0]" class="alert alert-danger" role="alert">
            {{ error.join(", ") }}
          </p>

          <form class="form_container">
            <!-- Fields -->
            <div class="form-group">
              <label for="nameComp">Имя</label>
              <input
                type="text"
                id="nameComp"
                placeholder="Имя"
                class="form-control"
                v-model="worker.first_name"
              />
            </div>
            <div class="form-group">
              <label for="nameComp">Фамилия</label>
              <input
                type="text"
                id="nameComp"
                placeholder="Фамилия"
                class="form-control"
                v-model="worker.last_name"
              />
            </div>
            <div class="form-group">
              <label for="phoneComp">Номер телефона</label>
              <input
                type="tel"
                id="phoneComp"
                placeholder="89991231213"
                class="form-control"
                v-model="worker.phone"
              />
            </div>
            <div class="form-group">
              <label for="dateComp">Дата рождения</label>
              <input
                type="date"
                id="dateComp"
                placeholder="Дата рождения"
                class="form-control"
                v-model="worker.birth_date"
              />
            </div>
            <!-- END Fields -->

            <!-- Submit -->
            <section>
              <div v-if="permission">
                <header class="section-header">
                  <span>Вы закончили?</span>
                  <h2>Отправляйте</h2>
                  <p>
                    Пожалуйста, проверьте информацию о себе еще раз и нажмите
                    кнопку ниже для доступа к ресурсам сайта.
                  </p>
                </header>

                <p class="text-center">
                  <button
                    class="btn btn-success btn-xl btn-round"
                    v-on:click="sendCreateReq"
                  >
                    Добавьте информацию о себе.
                  </button>
                </p>
              </div>
            </section>
            <!-- END Submit -->
          </form>
        </div>
      </header>
    </form>

    <div class="wrapper" v-if="permission == 'no'">
      <AuthError />
    </div>

    <div class="wrapper" v-if="permission == 'pending'">
      <h4 class="loading_page">Страница загружается</h4>
    </div>
  </div>
</template>

<script>
import { baseUrl, decode } from "../store/constants.js";

import Cookies from "universal-cookie";
import axios from "axios";
import AuthError from "@/components/AuthError.vue";

export default {
  components: { AuthError },
  layout: "company",

  data: () => ({
    permission: "pending",
    user: {},
    worker: {
      first_name: "",
      last_name: "",
      phone: "",
      birth_date: "",
    },
    error: [],
  }),

  async mounted() {
    await this.userRole();
    this.checkPermission();
  },

  methods: {
    checkPermission() {
      const cookies = new Cookies();
      let token = cookies.get("token");
      if (token !== "" && this.user.role === 2) {
        this.permission = "yes";
      } else {
        this.permission = "no";
      }
    },

    checkForm() {
      let pattern = /[0-9]{11}/;
      if (this.worker.phone.search(pattern) == -1) {
        this.error.push("Неправильный телефон");
      }
    },

    async userRole() {
      const cookies = new Cookies();
      let token = cookies.get("token");
      let userId = decode(token).user_id;
      let headers = this.get_headers(token);

      await axios
        .get(`${baseUrl()}/user/${userId}/`, { headers })
        .then((response) => {
          this.user = response.data;
        })
        .catch((error) => console.log(error));
    },

    get_headers(access) {
      let headers = {
        "Content-Type": "application/json",
      };
      headers["Authorization"] = "Bearer " + access;
      return headers;
    },

    sendCreateReq(event) {
      event.preventDefault();
      this.worker.user = this.user.id;
      this.error = [];
      this.checkForm();

      const cookies = new Cookies();
      let token = cookies.get("token");
      let headers = this.get_headers(token);

      axios
        .post(`${baseUrl()}/worker/`, this.worker, {
          headers,
        })
        .then((response) => {
          console.log(response.data);
          this.worker = response.data
          this.$router.push("/accountWorker");
        })
        .catch(() =>
          this.error.push("Ошибка при отправке формы, проверьте ввод!")
        );
    },
  },
};
</script>

<style scoped>
.wrapper {
  width: 100%;
  position: relative;
  z-index: 10;
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

.loading_page {
  text-align: center;
}
</style>


