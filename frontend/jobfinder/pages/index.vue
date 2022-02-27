<template>
  <div class="main__wrapp">
    <body class="nav-on-header">
      <!-- Site header -->
      <header
        class="site-header"
        :style="`background: url(${require('~/assets/img/bg-banner1.jpg')}) no-repeat center`"
      >
        <div class="main-window">
          <div class="col-xs-12">
            <br /><br />
            <h2 class="main-window__header">
              Мы предлагаем <mark>1,259</mark> вакансии прямо сейчас!
            </h2>
            <h5 class="main-window__header-subtitle">
              Найди работу по душе уже через минуту
            </h5>
            <br /><br /><br />
          </div>

          <form class="header-job-search">
            <div class="input-keyword" prop="name">
              <input
                type="text"
                v-model="findForm.name"
                :placeholder="'Наименование должности'"
                class="form-control"
              />
            </div>

            <div class="input-location" prop="city">
              <input type="text" class="form-control" :placeholder="'Город'" />
            </div>

            <div class="btn-search">
              <button
                round
                :loading="loading"
                @click="onSubmit"
                class="btn btn-primary"
                type="submit"
              >
                Найти работу
              </button>
              <button
                round
                :loading="loading"
                @click="onSearch"
                type="button"
                class="wsearch-btn"
              >
                {{ "расширенный поиск" }}
              </button>
            </div>
          </form>
        </div>
      </header>
      <!-- END Site header -->

      <!-- Main container -->
      <main>
        <!-- Recent jobs -->
        <section class="body">
          <div class="body__container">
            <header class="body-header">
              <h3 class="body-header__head">Правила и описание портала</h3>
              <h5><b>Описание</b></h5>
              <div align="left" style="text-indent: 20px">
                <p>
                  Общество с ограниченной ответственностью «Топ Джоб»,именуемое
                  в дальнейшем «Исполнитель», предоставляет любому физическому
                  лицу, именуемому в дальнейшем «Работник», услуги по содействию
                  в трудоустройстве и иных видах занятости посредством
                  предоставления различных сервисов Сайтов Исполнителя.
                  Предоставляет любому физическому лицу или юридической
                  организации, именуемому в дальнейшем «Компания», услуги по
                  размещение вакансий, отправлений предложений на резюме,
                  посредством предоставления различных сервисов Сайтов
                  Исполнителя. Безусловным принятием (акцептом) условий
                  настоящей оферты считается регистрация на сайте или совершение
                  любых действий, направленных на какое-либо использование
                  Сайтов Исполнителя.
                </p>
              </div>
              <p align="left">
                Регистрация на Сайте — процедура создания аккаунта на Сайте и
                получения Работником или Компанией учетной информации.
                Регистрация производится на основании данных, добровольно и
                осознанно предоставляемых через регистрационные формы Сайта
              </p>
              <h5><b>Правила</b></h5>
              <div align="left" style="text-indent: 20px">
                <p>
                  <b>1.1</b> Исполнитель обязуется предоставить возможность
                  Работнику размещать Резюме на Сайте, искать вакансии,
                  опубликованные на Сайте и создавать на них отклики.
                </p>
                <p>
                  <b>1.2</b> Исполнитель обязуется предоставить возможность
                  Компании размещать Вакансии на Сайте, искать резюме,
                  опубликованные на Сайте и отправлять на них предложения.
                </p>
                <p>
                  <b>1.3</b> В соответствии с Федеральным законом от 27.07.2006
                  г. № 152-ФЗ «О персональных данных» Соискатель в целях,
                  указанных в п.2.3 настоящего Соглашения, выражает согласие
                  Исполнителю на осуществление со всеми персональными данными,
                  указанными Соискателем при регистрации на Сайте или в
                  последующем на Сайте, в том числе в соответствующем Резюме,
                  следующих действий: сбор, систематизация, накопление,
                  хранение, уточнение (обновление или изменение), использование,
                  предоставление, доступ, блокирование, уничтожение, поиск и
                  сбор информации.
                </p>
                <p>
                  <b>1.4</b> Используя Сайт, Пользователь обязуется не нарушать
                  или пытаться нарушать информационную безопасность Сайта, что
                  включает в себя.
                </p>
              </div>
            </header>
            <br /><br />
            <p class="text-center">
              <nuxt-link class="btn btn-more" to="/vacancies"
                >Просмотреть все вакансии</nuxt-link
              >
            </p>
            <p class="text-center"></p>
          </div>
        </section>
        <!-- END Recent jobs -->

        <!-- How it works -->
        <section>
          <div class="text__container">
            <div class="text__container_left">
              <header class="text__container_left-title">
                <div class="text__container_left-title--head">Новости</div>
              </header>

              <div class="content" v-for="item in newsList" :key="item.id">
                <h4>
                  <b>{{ item.title }}</b>
                </h4>
                <p>{{ item.text }}</p>
                <div align="right">
                  <em>{{ item.date_publish }}</em>
                </div>
                <br />
              </div>
              <br /><br />
              <a class="btn btn-primary" href="page-typography.html"
                >Подробнее</a
              >
            </div>

            <div class="text__container_right">
              <br />
              <img
                class="center-block"
                src="~/assets/img/Work_Life.jpg"
                alt="how fined job"
              />
            </div>
          </div>
        </section>
        <!-- END How it works -->

        <!-- Categories -->
        <section class="category__container">
          <div class="category__container_wrap">
            <header class="category__container_header">
              <span class="category__container_header-title">Категории</span>
              <h2 class="category__container_header-head">
                Популярные категории
              </h2>
              <p class="category__container_header-note">
                Здесь самые популярные категории
              </p>
            </header>
          </div>
          <div class="category__block">
            <div
              class="category__item"
              v-for="(category, id) in categoryList"
              :key="id"
            >
              <div class="category__item_img">
                <img class="category-img" :src="category.img" />
              </div>
              <div class="category__item_title">{{ category.name }}</div>
              <div class="category__item_descr">{{ category.includes }}</div>
            </div>
          </div>
        </section>
        <!-- Newsletter -->

        <section
          class="subscribe"
          :style="`background: url(${require('~/assets/img/bg-facts.jpg')}) no-repeat center`"
        >
          <div class="subscribe__container">
            <h2>
              <strong class="subscribe__container_title">Подпишись</strong>
            </h2>
            <h6 class="subscribe__container_note">
              Получай еженедельный топ новых вакансий на свой e-mail
            </h6>
            <br /><br />
            <form class="form-subscribe" action="#">
              <div class="input-group">
                <input
                  type="text"
                  class="form-control-input input-lg"
                  placeholder="Твой e-mail"
                />
                <span class="input-group-btn">
                  <button class="btn btn-success btn-lg" type="submit">
                    Подписаться
                  </button>
                </span>
              </div>
            </form>
          </div>
        </section>
        <!-- END Newsletter -->
        <section>
          <div class="partners">
            <h2>
              <strong class="category__container_header-head"
                >Наши партнеры</strong
              >
            </h2>
            <ul class="brands">
              <li class="brands__item">
                <a href="https://www.facebook.com/" target="_blank">
                  <img
                    src="/_nuxt/assets/img/logo-facebook.png"
                    alt="facebook"
                    title="Facebook"
                  />
                </a>
              </li>
              <li class="brands__item">
                <a href="https://www.linkedin.com/" target="_blank">
                  <img
                    src="/_nuxt/assets/img/logo-linkedin.png"
                    alt="linkedin"
                    title="LinkedIn"
                  />
                </a>
              </li>
              <li class="brands__item">
                <a href="https://elements.envato.com/" target="_blank">
                  <img
                    src="/_nuxt/assets/img/logo-envato.png"
                    alt="envato"
                    title="EnvatoElements"
                  />
                </a>
              </li>

              <li class="brands__item">
                <a href="https://www.microsoft.com/" target="_blank">
                  <img
                    src="/_nuxt/assets/img/logo-microsoft.jpg"
                    alt="microsoft"
                    title="Microsoft"
                  />
                </a>
              </li>
              <li class="brands__item">
                <a href="https://www.google.com/" target="_blank">
                  <img
                    src="/_nuxt/assets/img/logo-google.jpg"
                    alt="google"
                    title="Google"
                  />
                </a>
              </li>
            </ul>
            <br /><br />
          </div>
        </section>
      </main>
      <!-- END Main container -->

      <!-- Scripts -->
      <!-- <script src="assets/js/app.min.js"></script>
      <script src="assets/js/custom.js"></script> -->
    </body>
  </div>
</template>

<script>
import { baseUrl, decode } from "../store/constants.js";
import axios from "axios";

export default {
  name: "IndexPage",
  data() {
    return {
      newsList: [],
      findForm: {
        name: "",
        city: "",
      },
      // TODO: translate
      findRules: {
        name: [
          {
            required: true,
            message: "название вакансии обязательно",
            trigger: "blur",
          },
        ],
        city: [
          {
            required: true,
            message: "название города обязательно",
            trigger: "blur",
          },
        ],
      },
      loading: false,
      vacancyList: [
        {
          id: 1,
          title: "Senior front-end developer",
          img: require("~/assets/img/logo-google.jpg"),
          company: "Google",
          location: "Москва",
          worktime: "Full-Time",
          link: "job-detail.html",
        },
        {
          id: 2,
          title: "Software Engineer (Entry or Senior)",
          img: require("~/assets/img/logo-linkedin.png"),
          company: "Linkedin",
          location: "Казань",
          worktime: "Part-Time",
          link: "job-detail.html",
        },
        {
          id: 3,
          title: "Full Stack Web Developer",
          img: require("~/assets/img/logo-envato.png"),
          company: "Envato",
          location: "Новосибирск",
          worktime: "Full-Time",
          link: "job-detail.html",
        },
        {
          id: 4,
          title: "Web Applications Developer",
          img: require("~/assets/img/logo-facebook.png"),
          company: "Facebook",
          location: "Санкт-Петербург",
          worktime: "Full-Time",
          link: "job-detail.html",
        },
        {
          id: 5,
          title: "Sr. SQL Server Developer",
          img: require("~/assets/img/logo-microsoft.jpg"),
          company: "Microsoft",
          location: "Владивосток",
          worktime: "Remote",
          link: "job-detail.html",
        },
      ],
      categoryList: [
        {
          id: 1,
          name: "Технологии",
          img: require("~/assets/img/1.png"),
          includes:
            " Designer, Developer, IT Service, Front-end developer, Project management",
        },
        {
          id: 2,
          name: "Финансы",
          img: require("~/assets/img/2.png"),
          includes:
            " Finance, Tax service, Payroll manager, Book keeper, Human resource",
        },
        {
          id: 3,
          name: "Медицина",
          img: require("~/assets/img/3.png"),
          includes: "Doctor, Nurse, Hospotal, Dental service, Massagist",
        },
        {
          id: 4,
          name: "Производство продуктов",
          img: require("~/assets/img/4.png"),
          includes: "Restaurant, Food service, Coffe shop, Cashier, Waitress",
        },
        {
          id: 5,
          name: "Медиа",
          img: require("~/assets/img/5.png"),
          includes: "Journalism, Newspaper, Reporter, Writer, Cameraman",
        },
        {
          id: 6,
          name: "Государственная служба",
          img: require("~/assets/img/6.png"),
          includes: "Federal, Law, Human resource, Manager, Biologist",
        },
      ],
    };
  },

  mounted() {
    this.getNews();
  },

  methods: {
    onSubmit() {
      this.login();
    },
    login() {
      console.log("OK");
      // this.loading = true
      // const data = Object.assign({}, this.loginForm)
      // try {
      //   await this.axios.get('', { data })
      // } catch (e) {
      // }
      // this.loading = false
    },
    onSearch() {
      console.log("Уже ищу!!!");
    },
    async getNewestVacancy() {
      try {
        const response = await this.$axios.get("/api/v1/newestvacancy");
        this.vacancyList = response.data.data;
        // eslint-disable-next-line no-console
        console.log(this.vacancyList);
      } catch (e) {
        this.$toast.error(e.response.data);
      }
    },
    async getCategory() {
      try {
        const response = await this.$axios.get("/api/v1/categories");
        this.categoryList = response.data.data;
        // eslint-disable-next-line no-console
        console.log(this.categoryList);
      } catch (e) {
        this.$toast.error(e.response.data);
      }
    },

    async getNews() {
      await axios
        .get(`${baseUrl()}/news/`)
        .then((response) => {
          this.newsList = response.data;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style lang="scss">
li {
  list-style-type: none;
}
.brands__item a {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.brands {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.brands__item {
  flex: 0 0 50%;
}

@media (min-width: 1100px) {
  .brands__item {
    flex: 0 0 20%;
  }
}
.main-window {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.site-header {
  display: flex;
  height: 700px;
  justify-content: center;
}
.header-job-search {
  display: flex;
  justify-content: center;
}
.wsearch-btn {
  height: 100%;
  border: none;
}
.main__wrapp {
  width: 100%;
}
.main-window__header {
  font-size: 46px;
  font-family: Arial, sans-serif;
  margin: 16px 0;
  line-height: 1.4;
  color: white;
  font-weight: 800;
  &-subtitle {
    text-align: center;
  }
}
.site-header mark {
  color: #29aafe;
  background-color: transparent;
  font-weight: 700;
}
.body-header {
  padding-top: 80px;
  display: flex;
  flex-direction: column;
  align-items: center;
  &__new {
    color: #84878a;
    font-family: Arial, sans-serif;
    font-size: 20px;
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  &__head {
    padding: 48px 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 46px;
    font-family: Arial, sans-serif;
    color: #55595c;
    margin: 16px 0;
    line-height: 1.4;
    font-weight: 800;
    &::after {
      content: "";
      width: 60px;
      height: 2px;
      background-color: #29aafe;
      margin-top: 50px;
    }
  }
}
body {
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 28px;
  color: #7e8890;
}
.body {
  &__container {
    display: flex;
    flex-direction: column;
    align-items: center;
    &_vacancy {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 90%;
    }
  }
}
.vacancy-item {
  display: flex;
  cursor: pointer;
  width: 100%;
  justify-content: space-around;
  margin: 30px 0;
  transition-property: border;
  transition-duration: 0.2s;
  &:hover {
    border: 1px solid #29aafe;
  }
  &__img {
    display: flex;
    padding: 0 30px;
  }
  &__info {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    width: 100%;
    padding: 0 30px;
    &_main {
      display: flex;
      justify-content: space-between;
      &-name {
        font-size: 36px;
        line-height: 40px;
        color: #55595c;
        font-family: Arial, sans-serif;
        font-weight: 400;
      }
      &-city {
        color: #96a2b2;
        line-height: 35px;
        font-size: 30px;
      }
    }
    &_add {
      display: flex;
      justify-content: space-between;
      &-company {
        font-size: 30px;
        color: #96a2b2;
      }
      &-worktime {
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 30px;
        color: white;
        font-weight: 400;
        border-radius: 0;
        padding: 4px 6px;
        margin-top: 6px;
        margin-left: 16px;
        opacity: 0.85;
        background-color: #5cb85c;
      }
    }
  }
}
.header-meta {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}
.nav-menu {
  margin: 0;
  padding: 0;
  display: flex;
  text-align: center;
  list-style-type: none;
  width: 65%;
  justify-content: space-between;
  align-items: center;
  &__ul {
    &_el {
      display: none;
    }
  }
}
.btn-more {
  width: 250px;
  height: 50px;
  color: #fff;
  background-color: #5bb7ed;
  border-color: #5bb7ed;
  align-items: center;
  display: flex;
  justify-content: center;
}
.text__container {
  display: flex;
  justify-content: space-around;
  &_left {
    width: 40%;
    &-title {
      display: flex;
      flex-direction: column;
      &--text {
        color: #84878a;
        font-family: Arial, sans-serif;
        font-size: 20px;
        letter-spacing: 2px;
        text-transform: uppercase;
      }
      &--head {
        padding: 48px 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        font-size: 46px;
        font-family: Arial, sans-serif;
        color: #55595c;
        text-transform: capitalize;
        margin: 16px 0;
        line-height: 1.4;
        font-weight: 800;
      }
    }
  }
}
.category__container {
  display: flex;
  flex-direction: column;
  align-items: center;
  &_header {
    display: flex;
    flex-direction: column;
    align-items: center;
    &-title {
      color: #84878a;
      font-family: Arial, sans-serif;
      font-size: 20px;
      letter-spacing: 2px;
      text-transform: uppercase;
    }
    &-head {
      padding: 48px 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      font-size: 46px;
      font-family: Arial, sans-serif;
      color: #55595c;
      text-transform: capitalize;
      margin: 16px 0;
      line-height: 1.4;
      font-weight: 800;
      &::after {
        content: "";
        width: 60px;
        height: 2px;
        background-color: #29aafe;
        margin-top: 50px;
      }
    }
    &-note {
      color: #84878a;
      font-family: Arial, sans-serif;
      font-size: 20px;
      letter-spacing: 2px;
      text-transform: uppercase;
    }
  }
}
.category__block {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  padding: 30px;
  justify-content: space-around;
}
.category__item {
  display: flex;
  flex-direction: column;
  width: 30%;
  align-items: center;
  padding: 30px;
  transition-property: background-color;
  transition-duration: 0.5s;
  &_img {
    width: 185px;
  }
  &_title {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 28px;
    font-family: Arial, sans-serif;
    color: #55595c;
    text-transform: capitalize;
    padding: 24px;
    line-height: 1.4;
    font-weight: 600;
    transition-property: color;
    transition-duration: 0.5s;
    &::after {
      content: "";
      width: 40px;
      height: 2px;
      background-color: #96a2b2;
      margin-top: 50px;
    }
  }
  &_descr {
    display: flex;
    padding: 24px;
    text-align: center;
    color: #96a2b2;
    font-size: 20px;
    line-height: 30px;
    transition-property: color;
    transition-duration: 0.5s;
  }
}
.category__item:hover {
  background-color: #29aafe;
}
.category__item:hover .category__item_title {
  color: white;
}
.category__item:hover .category__item_title::after {
  content: "";
  background-color: white;
}
.category__item:hover .category__item_descr {
  color: white;
}
.subscribe {
  display: flex;
  justify-content: center;
  &__container {
    display: flex;
    height: 600px;
    justify-content: center;
    flex-direction: column;
    width: 50%;
    &_title {
      padding: 48px 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      font-size: 46px;
      font-family: Arial, sans-serif;
      color: white;
      text-transform: capitalize;
      margin: 16px 0;
      line-height: 1.4;
      font-weight: 800;
      text-shadow: -2px 2px 0 #55595c, 2px 2px 0 #55595c, 2px -2px 0 #55595c,
        -2px -2px 0 #55595c;
    }
    &_note {
      display: flex;
      padding: 24px;
      text-align: center;
      color: white;
      font-size: 30px;
      line-height: 30px;
      font-weight: 600;
      text-shadow: -2px 2px 0 #55595c, 2px 2px 0 #55595c, 2px -2px 0 #55595c,
        -2px -2px 0 #55595c;
    }
    .form-control-input {
      height: 48px;
      width: 80%;
    }
  }
}
</style>
