<template>
  <div class="main__wrapp">
    <body class="nav-on-header">
      <!-- Site header -->
      <header
        class="site-header size-lg text-center"
        :style="`background: url(${require('/assets/img/bg-banner1.jpg')}) no-repeat center`"
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
              <a class="btn btn-info" href="job-list.html"
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
          <div class="container">
            <div class="col-sm-12 col-md-6">
              <header class="section-header text-left">
                <span>Технология работы</span>
                <h2>Как это устроено</h2>
              </header>

              <p class="lead">
                Pellentesque et pulvinar orci. Suspendisse sed euismod purus.
                Pellentesque nunc ex, ultrices eu enim non, consectetur interdum
                nisl. Nam congue interdum mauris, sed ultrices augue lacinia in.
                Praesent turpis purus, faucibus in tempor vel, dictum ac eros.
              </p>
              <p>
                Nulla quis felis et orci luctus semper sit amet id dui. Aenean
                ultricies lectus nunc, vel rhoncus odio sagittis eu. Sed at
                felis eu tortor mattis imperdiet et sed tortor. Nullam ac
                porttitor arcu. Vivamus tristique elit id tempor lacinia. Donec
                auctor at nibh eget tincidunt. Nulla facilisi. Nunc condimentum
                dictum mattis.
              </p>

              <br /><br />
              <a class="btn btn-primary" href="page-typography.html"
                >Подробнее</a
              >
            </div>

            <div class="col-sm-12 col-md-6 hidden-xs hidden-sm">
              <br />
              <img
                class="center-block"
                src="assets/img/how-it-works.png"
                alt="how it works"
              />
            </div>
          </div>
        </section>
        <!-- END How it works -->

        <!-- Categories -->
        <section class="bg-alt">
          <div class="container">
            <header class="section-header">
              <span>Категории</span>
              <h2>Популярные категории</h2>
              <p>Здесь самые популярные категории</p>
            </header>

            <div class="category-grid">
              <a href="job-list-1.html">
                <i class="fa fa-laptop"></i>
                <h6>Technology</h6>
                <p>
                  Designer, Developer, IT Service, Front-end developer, Project
                  management
                </p>
              </a>

              <a href="job-list-2.html">
                <i class="fa fa-line-chart"></i>
                <h6>Accounting</h6>
                <p>
                  Finance, Tax service, Payroll manager, Book keeper, Human
                  resource
                </p>
              </a>

              <a href="job-list-3.html">
                <i class="fa fa-medkit"></i>
                <h6>Medical</h6>
                <p>Doctor, Nurse, Hospotal, Dental service, Massagist</p>
              </a>

              <a href="job-list-1.html">
                <i class="fa fa-cutlery"></i>
                <h6>Food</h6>
                <p>Restaurant, Food service, Coffe shop, Cashier, Waitress</p>
              </a>

              <a href="job-list-2.html">
                <i class="fa fa-newspaper-o"></i>
                <h6>Media</h6>
                <p>Journalism, Newspaper, Reporter, Writer, Cameraman</p>
              </a>

              <a href="job-list-3.html">
                <i class="fa fa-institution"></i>
                <h6>Government</h6>
                <p>Federal, Law, Human resource, Manager, Biologist</p>
              </a>
            </div>
          </div>
        </section>
        <!-- END Categories -->

        <!-- Newsletter -->
        <section class="bg-img text-center">
          <div class="container">
            <h2><strong>Подпишись</strong></h2>
            <h6 class="font-alt">
              Получай еженедельный топ новых вакансий на свой e-mail
            </h6>
            <br /><br />
            <form class="form-subscribe" action="#">
              <div class="input-group">
                <input
                  type="text"
                  class="form-control input-lg"
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
          id: 1, title: 'Senior front-end developer', img: require('../assets/img/logo-google.jpg'), company: 'Google', location: 'Москва', worktime: 'Full-Time', link: 'job-detail.html'
        },
        {
          id: 2, title: 'Software Engineer (Entry or Senior)', img: require('../assets/img/logo-linkedin.png'), company: 'Linkedin', location: 'Казань', worktime: 'Part-Time' , link: 'job-detail.html'
        },
        {
          id: 3, title: 'Full Stack Web Developer', img: require('../assets/img/logo-envato.png'), company: 'Envato', location: 'Новосибирск', worktime: 'Full-Time' , link: 'job-detail.html'
        },
        {
          id: 4, title: 'Web Applications Developer', img: require('../assets/img/logo-facebook.png'), company: 'Facebook', location: 'Санкт-Петербург', worktime: 'Full-Time' , link: 'job-detail.html'
        },
        {
          id: 5, title: 'Sr. SQL Server Developer', img: require('../assets/img/logo-microsoft.jpg'), company: 'Microsoft', location: 'Владивосток', worktime: 'Remote' , link: 'job-detail.html'
        },
      ]
    }
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
    }
  }
}
</script>

<style lang="scss">
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
  &::after {
    border: 1px solid #29aafe;
  }
  &__img {
    display: flex;
    padding: 0 30px;
  }
  &__info {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
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
</style>
