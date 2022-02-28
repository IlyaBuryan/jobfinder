<template>
  <div class="resume_wrapp">
    <!-- Page header -->
    <header class="page-header">
      <div class="container">
        <div class="header-detail">
          <div class="header-detail__head">
            <!-- <img class="logo" :src="resume.img" alt=""> -->
            <div class="header-detail__head_main">
              <div class="hgroup">
                <h1>{{ resume.position }}</h1>
                <!-- <h3><a href="#">{{ resume.worker_info.first_name }} {{ resume.worker_info.last_name }}</a></h3> -->
              </div>
              <div class="header-detail__head_main-time">
                {{ resume.published_date }}
              </div>
            </div>
          </div>
          <hr />
          <p class="header-detail__head_main-descr">
            {{ resume.institution }}.
          </p>
          <div class="header-detail__footer">
            <ul class="header-detail__head_main-params">
              <li>
                <i class="fa fa-map-marker"></i>
                <span>{{ resume.courses }}</span>
              </li>

              <!-- <li>
                <i class="fa fa-briefcase"></i>
                <span>{{ resume.conditions }}</span>
              </li> -->

              <!-- <li>
                <i class="fa fa-money"></i>
                <span>{{ resume.salary }}</span>
              </li> -->
            </ul>
            <ul class="header-detail__head_main-params">
              <li>
                <i class="fa fa-clock-o"></i>
                <span>40h / week</span>
              </li>

              <li>
                <i class="fa fa-flask"></i>
                <span>2+ years experience</span>
              </li>

              <li>
                <i class="fa fa-certificate"></i>
                <a href="#">Высшее</a>
              </li>
            </ul>
          </div>

          <div class="button-group">
            <div class="action-buttons">
              <div class="form-group">
                <label for="catComp"
                  >Выберите вакансию, на которую хотите пригласить
                  человека</label
                >
                <select
                  v-model="vacancy"
                  class="form-control"
                  aria-label="Default select example"
                >
                  <option disabled value="">Выберите один из вариантов</option>
                  <option
                    v-for="option in options"
                    :key="option.id"
                    v-bind:value="option.id"
                  >
                    {{ option.id }} - {{ option.position }}
                  </option>
                </select>
              </div>
              <div class="form-group">
                <label for="message">Сопроводительное письмо</label>
                <textarea
                  type="text"
                  id="message"
                  placeholder="Напишите письмо"
                  class="form-control"
                  v-model="message"
                />
              </div>
              <p class="text-center">
                <button
                  class="btn btn-success btn-xl btn-round"
                  v-on:click="sendCreateReq"
                >
                  Отправить приглашение
                </button>
              </p>
            </div>
          </div>
        </div>
      </div>
    </header>
    <!-- END Page header -->

    <!-- Main container -->
    <main>
      <!-- Job detail -->
      <section class="vacancy-info">
        <div class="vacancy-info__container">
          <br />
          <h4>Позиция</h4>
          <span>{{ resume.position }}</span>

          <div
            class="vacancy-item"
            v-for="(item, id) in resume.experience"
            :key="id"
          >
            <p>Организация {{ item.organization }}</p>
            <p>Позиция {{ item.position }}</p>
            <p>Функции {{ item.functions }}</p>
            <p>Начало {{ item.start }}</p>
            <p>Окончание {{ item.end }}</p>
          </div>

          <h4>Образование</h4>
          <span>{{ resume.institution }}</span>

          <br />
          <h4>Имя</h4>
          <span>{{ resume.worker_info.first_name }}</span>

          <br />
          <h4>Фамилия</h4>
          <span>{{ resume.worker_info.last_name }}</span>

          <br />
          <h4>Телефон</h4>
          <span>{{ resume.worker_info.phone }}</span>
        </div>
      </section>
      <!-- END Job detail -->
    </main>
    <!-- END Main container -->
  </div>
</template>

<script>
import Message from "@/components/Message.vue";
import { baseUrl, decode } from "../../store/constants.js";
import axios from "axios";
import Cookies from "universal-cookie";

export default {
  components: { Message },
  data() {
    return {
      resume: {
        worker_info: {
          first_name: "",
          last_name: "",
          phone: "",
        },
        position: "",
        experience: [],
        institution: "",
      },

      user: "",
      vacancy: "",
      message: "",
      options: [],
    };
  },
  async mounted() {
    await this.getCard();
  },

  methods: {
    getCard() {
      const cookies = new Cookies();
      let token = cookies.get("token");
      this.user = decode(token).user_id;
      let headers = this.get_headers(token);

      axios
        .get(`${baseUrl()}/resume/${this.$route.params.resume_id}/`, {
          headers,
        })
        .then((response) => {
          this.resume = response.data;
          console.log("------------------------------");
          console.log(response.data);
          console.log(this.resume);
        })
        .catch((error) => console.log(error));

      axios
        .get(`${baseUrl()}/my_vacancies/`, {
          headers,
        })
        .then((response) => {
          this.options = response.data;
          console.log(this.options);
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
      const cookies = new Cookies();
      let token = cookies.get("token");
      let headers = this.get_headers(token);

      const data = {
        user: this.user,
        vacancy: this.vacancy,
        resume: this.resume.id,
        message: this.message,
      };

      console.log(data);

      axios
        .post(`${baseUrl()}/message_on_resume/`, data, {
          headers,
        })
        .then((response) => {
          console.log(response.data);
          this.resume = "";
          this.$router.push("/accountCompany");
        })
        .catch(() => (this.error = true));
    },
  },
};
</script>

<style lang="scss">
.main__wrapp {
  display: flex;
  max-width: 100%;
  flex-direction: column;
}
.resume_wrapp {
  width: 100%;
}
.page-header {
  display: flex;
  height: 700px;
  flex-direction: column;
  background: url("~/assets/img/bg-banner2.jpg") no-repeat top center;
  background-size: cover;
  align-items: center;
  justify-content: center;
}
.container {
  justify-content: center;
  max-width: 100%;
  margin-top: 100px;
  display: flex;
}
.vacancy-info {
  display: flex;
  justify-content: center;
  &__container {
    display: flex;
    flex-direction: column;
    padding: 50px;
    max-width: 90%;
  }
}
.header-detail {
  width: 80%;
  background-color: white;
  &__head {
    display: flex;
    padding-top: 10px;
    &_main {
      display: flex;
      justify-content: space-between;
      width: 75%;
      &-time {
        margin-right: 10px;
        display: flex;
        align-items: center;
      }
      &-descr {
        display: flex;
        padding: 10px;
      }
      &-params {
        display: flex;
        li {
          width: 30%;
        }
      }
    }
  }
}
.button-group {
  display: flex;
  padding: 20px;
  justify-content: space-between;
}
.logo {
  display: flex;
  padding: 0 10px;
  align-items: center;
  max-width: 300px;
  img {
    width: 240px;
  }
}
.resume-info {
  display: flex;
  justify-content: center;
  &__container {
    display: flex;
    flex-direction: column;
    padding: 50px;
    max-width: 90%;
  }
}

.button-group {
  display: flex;
  justify-content: center;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  align-content: center;
}
.vacancy-item {
  display: flex;
  flex-direction: column;
}
</style>
