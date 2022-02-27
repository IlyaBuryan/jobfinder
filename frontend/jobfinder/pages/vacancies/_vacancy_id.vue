<template>
  <div class="vacancy_wrapp">
    <!-- Page header -->
    <header class="page-header">
      <div class="container">
        <div class="header-detail">
          <div class="header-detail__head">
            <!-- <img class="logo" :src="vacancy.img" alt=""> -->
            <div class="header-detail__head_main">
              <div class="hgroup">
                <h1>{{ vacancy.position }}</h1>
                <h3>
                  <a href="#">{{ company_name }}</a>
                </h3>
              </div>
              <div class="header-detail__head_main-time">
                {{ vacancy.published_date }}
              </div>
            </div>
          </div>
          <hr />
          <p class="header-detail__head_main-descr">{{ vacancy.duties }}.</p>
          <div class="header-detail__footer">
            <ul class="header-detail__head_main-params">
              <li>
                <i class="fa fa-map-marker"></i>
                <span>{{ vacancy.city }}</span>
              </li>

              <li>
                <i class="fa fa-briefcase"></i>
                <span>{{ vacancy.conditions }}</span>
              </li>

              <li>
                <i class="fa fa-money"></i>
                <span>{{ vacancy.salary }}</span>
              </li>
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
                  >Выберите резюме, которым хотите откликнуться</label
                >
                <select
                  v-model="resume"
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
                  Откликнуться
                </button>
              </p>
              <!-- <Message></Message> -->
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
          <h4>Position</h4>
          <p>{{ vacancy.position }}</p>

          <br />
          <h4>Conditions</h4>
          <p>{{ vacancy.conditions }}</p>

          <br />
          <h4>Duties</h4>
          <p>{{ vacancy.duties }}</p>

          <br />
          <h4>Responsibilities</h4>
          <p>{{ vacancy.requirements }}</p>

          <br />
          <h4>Salary</h4>
          <p>{{ vacancy.salary }}</p>

          <br />
          <h4>City</h4>
          <p>{{ vacancy.city }}</p>
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
      loading: false,
      vacancy: {},
      company_name: "",
      user: "",
      vacancy: "",
      resume: "",
      message: "",
      options: [],
    };
  },
  async mounted() {
    this.getCard();
  },

  methods: {
    async getCard() {
      const cookies = new Cookies();
      let token = cookies.get("token");
      this.user = decode(token).user_id;
      let headers = this.get_headers(token);

      await axios
        .get(`${baseUrl()}/vacancyapp/${this.$route.params.vacancy_id}`, {
          headers,
        })
        .then((response) => {
          this.vacancy = response.data;
          this.company = response.company_card;
          this.company_name = response.company_name;

          console.log(this.vacancy);
        })
        .catch((error) => console.log(error));

      await axios
        .get(`${baseUrl()}/resume/`, {
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
        vacancy: this.vacancy.id,
        resume: this.resume,
        message: this.message,
      };

      console.log(data);

      axios
        .post(`${baseUrl()}/message_to_vacancy/`, data, {
          headers,
        })
        .then((response) => {
          console.log(response.data);
          this.resume = "";
          this.$router.push("/accountWorker");
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
.vacancy_wrapp {
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

.button-group {
  display: flex;
  justify-content: center;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  align-content: center;
}
</style>
