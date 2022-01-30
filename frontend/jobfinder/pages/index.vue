<template>
  <div class="main__wrapp">
    <body class="nav-on-header">
      <!-- Site header -->
      <header
        class="site-header size-lg text-center"
        :style="`background: url(${require('~/assets/img/bg-banner1.jpg')}) no-repeat center`"
      >
        <div class="container main-window">
          <div class="col-xs-12">
            <br><br>
            <h2 class="main-window__header">Мы предлагаем <mark>1,259</mark> вакансии прямо сейчас!</h2>
            <h5 class="font-alt">Найди работу по душе уже через минуту</h5>
            <br /><br /><br />
          </div>

          <form class="header-job-search">
            <div class="input-keyword" prop="name">
              <input
              type="text"
                v-model="findForm.name"
                :placeholder="'Наименование должности'" class="form-control">
            </div>

            <div class="input-location" prop="city">
              <input type="text" class="form-control" :placeholder="'Город'">
            </div>

            <div class="btn-search">
              <button
                round
                :loading="loading"
                @click="onSubmit"
                class="btn btn-primary"
                type="submit">Найти работу
              </button>
              <button
                round
                :loading="loading"
                @click="onSearch"
                type="button"
                class="wsearch-btn"
              >
                {{ 'расширенный поиск' }}
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
              <span class="body-header__new">Свежее</span>
              <h2 class="body-header__head">Новейшие вакансии</h2>
            </header>

            <div class="body__container_vacancy">
              <!-- Job item -->
              <div class="vacancy-item" v-for="(item, id) in vacancyList" :key="id">
                <div class="vacancy-item__img"><img class="company-logo" :src="item.img" alt=""></div>
                <div class="vacancy-item__info">
                  <div class="vacancy-item__info_main">
                    <div class="vacancy-item__info_main-name">{{ item.title }}</div>
                    <div class="vacancy-item__info_main-city">{{ item.location}}</div>
                  </div>
                  <div class="vacancy-item__info_add">
                    <div class="vacancy-item__info_add-company">{{ item.company }}</div>
                    <div class="vacancy-item__info_add-worktime">{{ item.worktime }}</div>
                  </div>
                </div>
              </div>

              <!-- END Job item -->
            </div>

            <br /><br />
            <p class="text-center">
              <a class="btn btn-more" href="job-list.html"
                >Просмотреть все вакансии</a
              >
            </p>
          </div>
        </section>
        <!-- END Recent jobs -->

        <!-- Facts -->
        <section class="bg-img bg-repeat no-overlay section-sm">
          <div class="container">
            <div class="row">
              <div class="counter col-md-3 col-sm-6">
                <p><span data-from="0" data-to="6890"></span>+</p>
                <h6>Вакансии</h6>
              </div>

              <div class="counter col-md-3 col-sm-6">
                <p><span data-from="0" data-to="1200"></span>+</p>
                <h6>Клиентов</h6>
              </div>

              <div class="counter col-md-3 col-sm-6">
                <p><span data-from="0" data-to="36800"></span>+</p>
                <h6>Резюме</h6>
              </div>

              <div class="counter col-md-3 col-sm-6">
                <p><span data-from="0" data-to="15400"></span>+</p>
                <h6>Компаний</h6>
              </div>
            </div>
          </div>
        </section>
        <!-- END Facts -->

        <!-- How it works -->
        <section>
          <div class="text__container">
            <div class="text__container_left">
              <header class="text__container_left-title">
                <span class="text__container_left-title--text">Поиск работы</span>
                <div class="text__container_left-title--head">Как правильно искать работу</div>
              </header>

              <p class="story">
                Искать работу – тоже работа. Это инструкция из 5 пунктов для человека
                из любой индустрии и любого уровня, будь то первая работа после университета
                или руководящая должность высокоуровневого специалиста.
              </p>
              <p>
                1. Выбор индустрии
                Индустрия – почва, на которой вы будете расти следующее время. Это может быть
                диджитал, маркетинг, IT, финансы, продажи и т. д.
                Если у вас нет опыта, подумайте, в какой сфере было бы интересно развиваться,
                чем хотелось бы заниматься, чтобы работа приносила удовольствие.
              </p>
              <p>
                2. Выбор компании.
                Сайты для поиска работы – простой, но не эффективный способ. После изучения
                индустрии обратите внимание на компании, которые кажутся привлекательными,
                исходя из ваших ожиданий.

                -- Выберите 10 таких компаний.
                -- Найдите открытые вакансии в общем доступе.
                -- Оцените, какие требования ставит компания, и какие есть у вас.
                -- Подготовьте резюме, выделите ключевые навыки, которые соответствуют вакансии. Идеальных кандидатов с полным набором требований нет. Достаточно обладать несколькими важными. Не бойтесь рисковать!
              </p>
              <p>
                3. Представьте свою роль в компании.
                Приобретенная специальность не так важна. Всегда можно изменить
                профессиональную жизнь в лучшую сторону. Главное в карьере – это
                приобретенные навыки (hard skills) и личностные качества (soft skills).

                Если каждый день читать профильные статьи и смотреть лекции, посещать
                курсы и вебинары, то в какой-то момент вы начнете разбираться в сфере
                вашего изучения и сформируете экспертное мнение. После нужно закрепить
                это в практике, но начало положено.
              </p>

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
              <h2 class="category__container_header-head">Популярные категории</h2>
              <p class="category__container_header-note">Здесь самые популярные категории</p>
            </header>
          </div>
          <div class="category__block">
            <div class="category__item" v-for="(category, id) in categoryList" :key="id">
              <div class="category__item_img"><img class="category-img" :src="category.img"></div>
              <div class="category__item_title">{{ category.name }}</div>
              <div class="category__item_descr">{{ category.includes }}</div>
            </div>
          </div>
        </section>
        <!-- Newsletter -->
        <section class="subscribe"
        :style="`background: url(${require('~/assets/img/bg-facts.jpg')}) no-repeat center`">
          <div class="subscribe__container">
            <h2><strong class="subscribe__container_title">Подпишись</strong></h2>
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
      </main>
      <!-- END Main container -->

      <!-- Scripts -->
      <script src="assets/js/app.min.js"></script>
      <script src="assets/js/custom.js"></script>
    </body>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data () {
    return {
      findForm: {
        name: '',
        city: ''
      },
      // TODO: translate
      findRules: {
        name: [
          { required: true, message: 'название вакансии обязательно', trigger: 'blur' },
        ],
        city: [{ required: true, message: 'название города обязательно', trigger: 'blur' }]
      },
      loading: false,
      vacancyList: [
        {
          id: 1, title: 'Senior front-end developer', img: require('~/assets/img/logo-google.jpg'), company: 'Google', location: 'Москва', worktime: 'Full-Time', link: 'job-detail.html'
        },
        {
          id: 2, title: 'Software Engineer (Entry or Senior)', img: require('~/assets/img/logo-linkedin.png'), company: 'Linkedin', location: 'Казань', worktime: 'Part-Time' , link: 'job-detail.html'
        },
        {
          id: 3, title: 'Full Stack Web Developer', img: require('~/assets/img/logo-envato.png'), company: 'Envato', location: 'Новосибирск', worktime: 'Full-Time' , link: 'job-detail.html'
        },
        {
          id: 4, title: 'Web Applications Developer', img: require('~/assets/img/logo-facebook.png'), company: 'Facebook', location: 'Санкт-Петербург', worktime: 'Full-Time' , link: 'job-detail.html'
        },
        {
          id: 5, title: 'Sr. SQL Server Developer', img: require('~/assets/img/logo-microsoft.jpg'), company: 'Microsoft', location: 'Владивосток', worktime: 'Remote' , link: 'job-detail.html'
        },
      ],
      categoryList: [
        { id: 1, name: 'Технологии', img: require('~/assets/img/1.png'), includes: ' Designer, Developer, IT Service, Front-end developer, Project management'},
        { id: 2, name: 'Финансы', img: require('~/assets/img/2.png'), includes: ' Finance, Tax service, Payroll manager, Book keeper, Human resource'},
        { id: 3, name: 'Медицина', img: require('~/assets/img/3.png'), includes: 'Doctor, Nurse, Hospotal, Dental service, Massagist'},
        { id: 4, name: 'Производство продуктов', img: require('~/assets/img/4.png'), includes: 'Restaurant, Food service, Coffe shop, Cashier, Waitress'},
        { id: 5, name: 'Медиа', img: require('~/assets/img/5.png'), includes: 'Journalism, Newspaper, Reporter, Writer, Cameraman'},
        { id: 6, name: 'Государственная служба', img: require('~/assets/img/6.png'), includes: 'Federal, Law, Human resource, Manager, Biologist'},
      ]
    }
  },
  mounted() {
    this.getNewestVacancy()
  },
  methods: {
    onSubmit () {
      this.login()
    },
    login () {
      console.log( 'OK')
        // this.loading = true
        // const data = Object.assign({}, this.loginForm)
        // try {
        //   await this.axios.get('', { data })
        // } catch (e) {
        // }
        // this.loading = false
    },
    onSearch () {
      console.log('Уже ищу!!!')
    },
    async getNewestVacancy () {
      try {
        const response = await this.$axios.get('/api/v1/newestvacancy')
        this.vacancyList = response.data.data
        // eslint-disable-next-line no-console
        console.log(this.vacancyList)
      } catch (e) {
        this.$toast.error(e.response.data)
      }
    },
    async getCategory () {
      try {
        const response = await this.$axios.get('/api/v1/categories')
        this.categoryList = response.data.data
        // eslint-disable-next-line no-console
        console.log(this.categoryList)
      } catch (e) {
        this.$toast.error(e.response.data)
      }
    }
  }
}
</script>

<style lang="scss">
.main-window {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.site-header {
  display: flex;
  height: 700px;
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
  font-family: Arial,sans-serif;
  margin: 16px 0;
  line-height: 1.4;
  color: white;
  font-weight: 800;
}
.site-header mark {
  color: #29aafe;;
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
    font-family: Arial,sans-serif;
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
    font-family: Arial,sans-serif;
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
}
body {
  font-family: Arial,sans-serif;
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
  transition-duration: .2s;
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
        opacity: .85;
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
        font-family: Arial,sans-serif;
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
        font-family: Arial,sans-serif;
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
      font-family: Arial,sans-serif;
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
      font-family: Arial,sans-serif;
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
      font-family: Arial,sans-serif;
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
  transition-duration: .5s;
  &_img {
    width: 185px;
  }
  &_title {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 28px;
    font-family: Arial,sans-serif;
    color: #55595c;
    text-transform: capitalize;
    padding: 24px;
    line-height: 1.4;
    font-weight: 600;
    transition-property: color;
    transition-duration: .5s;
    &::after {
      content: "";
      width: 40px;
      height: 2px;
      background-color:  #96a2b2;
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
    transition-duration: .5s;
  }
}
.category__item:hover {
  background-color: #29aafe;
}
.category__item:hover .category__item_title{
  color: white;
}
.category__item:hover .category__item_title::after {
  content: "";
  background-color: white;
}
.category__item:hover .category__item_descr{
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
      font-family: Arial,sans-serif;
      color: white;
      text-transform: capitalize;
      margin: 16px 0;
      line-height: 1.4;
      font-weight: 800;
      text-shadow: -2px 2px 0 #55595c, 2px 2px 0 #55595c, 2px -2px 0 #55595c, -2px -2px 0 #55595c;
    }
    &_note {
      display: flex;
      padding: 24px;
      text-align: center;
      color: white;
      font-size: 30px;
      line-height: 30px;
      font-weight: 600;
      text-shadow: -2px 2px 0 #55595c, 2px 2px 0 #55595c, 2px -2px 0 #55595c, -2px -2px 0 #55595c;
    }
    .form-control-input {
      height: 48px;
      width: 80%;
    }
  }
}

</style>
