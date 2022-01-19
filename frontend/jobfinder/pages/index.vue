<template>
  <div class="container">
    <body class="nav-on-header">

      <!-- Navigation bar -->
      <nav class="navbar">
        <div class="container">

          <!-- Logo -->
          <div class="pull-left">
            <a class="navbar-toggle" href="#" data-toggle="offcanvas"><i class="ti-menu"></i></a>

            <div class="logo-wrapper">
              <a class="logo" href="index.html"><img src="/assets/img/logo.png" alt="logo"></a>
              <a class="logo-alt" href="index.html"><img src="assets/img/logo-alt.png" alt="logo-alt"></a>
            </div>

          </div>
          <!-- END Logo -->

          <!-- Navigation menu -->
          <ul class="nav-menu">
            <li>
              <a class="nav-menu__ul active" href="index.html">Главная</a>
              <ul class="nav-menu__ul_el">
                <li><a class="active" href="index.html">Вариант 1</a></li>
                <li><a href="index-2.html">Вариант 2</a></li>
              </ul>
            </li>
            <li>
              <a class="nav-menu__ul" href="#">Вакансии</a>
              <ul class="nav-menu__ul_el">
                <li><a href="job-list-1.html">Вакансия - 1</a></li>
                <li><a href="job-list-2.html">Вакансия - 2</a></li>
                <li><a href="job-list-3.html">Вакансия - 3</a></li>
                <li><a href="job-detail.html">Инфо о вакансии</a></li>
                <li><a href="job-add.html">Добавить вакансию</a></li>
                <li><a href="job-manage.html">Редактировать вакансии</a></li>
              </ul>
            </li>
            <li>
              <a class="nav-menu__ul" href="#">Резюме</a>
              <ul class="nav-menu__ul_el">
                <li><a href="resume-list.html">Просмотреть резюме</a></li>
                <li><a href="resume-detail.html">Инфо о резюме</a></li>
                <li><a href="resume-add.html">Создать резюме</a></li>
                <li><a href="resume-manage.html">Редактировать резюме</a></li>
              </ul>
            </li>
            <li>
              <a class="nav-menu__ul" href="#">Компании</a>
              <ul class="nav-menu__ul_el">
                <li><a href="company-list.html">Просмотреть компании</a></li>
                <li><a href="company-detail.html">Инфо о компании</a></li>
                <li><a href="company-add.html">Создать компанию</a></li>
                <li><a href="company-manage.html">Редактировать компании</a></li>
              </ul>
            </li>
            <li>
              <a class="nav-menu__ul" href="#">Страницы</a>
              <ul class="nav-menu__ul_el">
                <li><a href="page-about.html">О нас</a></li>
                <li><a href="page-contact.html">Контакты</a></li>
                <li><a href="page-faq.html">FAQ</a></li>
                <li><a href="page-pricing.html">Наши цены</a></li>
                <li><a href="page-typography.html">Типографские услуги</a></li>
                <li><a href="page-ui-elements.html">UI элементы</a></li>
              </ul>
            </li>
          </ul>
          <!-- END Navigation menu -->

          <!-- User account -->
          <div class="pull-right user-login">
            <a class="btn btn-sm btn-primary" href="user-login.html">Авторизоваться</a> или <a
              href="user-register.html">Зарегистрироваться</a>
          </div>
          <!-- END User account -->

        </div>
      </nav>
      <!-- END Navigation bar -->


      <!-- Site header -->
      <header class="site-header size-lg text-center" :style="`background: url(${require('/assets/img/bg-banner1.jpg')}) no-repeat center`">
        <div class="container">
          <div class="col-xs-12">
            <br><br>
            <h2>Мы предлагаем <mark>1,259</mark> вакансии прямо сейчас!</h2>
            <h5 class="font-alt">Найди работу по душе уже через минуту</h5>
            <br><br><br>
            <form class="header-job-search">
              <div class="input-keyword">
                <input type="text" class="form-control" placeholder="Наименование должности, навыки или название компании">
              </div>

              <div class="input-location">
                <input type="text" class="form-control" placeholder="Город, область или почтовый индекс">
              </div>

              <div class="btn-search">
                <button class="btn btn-primary" type="submit">Найти работу</button>
                <a href="job-list.html">Расширенный поиск</a>
              </div>
            </form>
          </div>

        </div>
      </header>
      <!-- END Site header -->


      <!-- Main container -->
      <main>



        <!-- Recent jobs -->
        <section>
          <div class="container">
            <header class="section-header">
              <span>Свежее</span>
              <h2>Новейшие вакансии</h2>
            </header>

            <div class="row item-blocks-connected">

              <!-- Job item -->
              <div class="col-xs-12">
                <a class="item-block" href="job-detail.html">
                  <header>
                    <img src="assets/img/logo-google.jpg" alt="">
                    <div class="hgroup">
                      <h4>Senior front-end developer</h4>
                      <h5>Google</h5>
                    </div>
                    <div class="header-meta">
                      <span class="location">Menlo park, CA</span>
                      <span class="label label-success">Full-time</span>
                    </div>
                  </header>
                </a>
              </div>
              <!-- END Job item -->


              <!-- Job item -->
              <div class="col-xs-12">
                <a class="item-block" href="job-detail.html">
                  <header>
                    <img src="assets/img/logo-linkedin.png" alt="">
                    <div class="hgroup">
                      <h4>Software Engineer (Entry or Senior)</h4>
                      <h5>Linkedin</h5>
                    </div>
                    <div class="header-meta">
                      <span class="location">Livermore, CA</span>
                      <span class="label label-warning">Part-time</span>
                    </div>
                  </header>
                </a>
              </div>
              <!-- END Job item -->

              <!-- Job item -->
              <div class="col-xs-12">
                <a class="item-block" href="job-detail.html">
                  <header>
                    <img src="assets/img/logo-envato.png" alt="">
                    <div class="hgroup">
                      <h4>Full Stack Web Developer</h4>
                      <h5>Envato</h5>
                    </div>
                    <div class="header-meta">
                      <span class="location">San Francisco, CA</span>
                      <span class="label label-info">Freelance</span>
                    </div>
                  </header>
                </a>
              </div>
              <!-- END Job item -->

              <!-- Job item -->
              <div class="col-xs-12">
                <a class="item-block" href="job-detail.html">
                  <header>
                    <img src="assets/img/logo-facebook.png" alt="">
                    <div class="hgroup">
                      <h4>Web Applications Developer</h4>
                      <h5>Facebook</h5>
                    </div>
                    <div class="header-meta">
                      <span class="location">Lexington, MA</span>
                      <span class="label label-danger">Internship</span>
                    </div>
                  </header>
                </a>
              </div>
              <!-- END Job item -->

              <!-- Job item -->
              <div class="col-xs-12">
                <a class="item-block" href="job-detail.html">
                  <header>
                    <img src="assets/img/logo-microsoft.jpg" alt="">
                    <div class="hgroup">
                      <h4>Sr. SQL Server Developer</h4>
                      <h5>Microsoft</h5>
                    </div>
                    <div class="header-meta">
                      <span class="location">Palo Alto, CA</span>
                      <span class="label label-success">Remote</span>
                    </div>
                  </header>
                </a>
              </div>
              <!-- END Job item -->

            </div>

            <br><br>
            <p class="text-center"><a class="btn btn-info" href="job-list.html">Просмотреть все вакансии</a></p>
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

              <p class="lead">Pellentesque et pulvinar orci. Suspendisse sed euismod purus. Pellentesque nunc ex, ultrices
                eu enim non, consectetur interdum nisl. Nam congue interdum mauris, sed ultrices augue lacinia in. Praesent
                turpis purus, faucibus in tempor vel, dictum ac eros.</p>
              <p>Nulla quis felis et orci luctus semper sit amet id dui. Aenean ultricies lectus nunc, vel rhoncus odio
                sagittis eu. Sed at felis eu tortor mattis imperdiet et sed tortor. Nullam ac porttitor arcu. Vivamus
                tristique elit id tempor lacinia. Donec auctor at nibh eget tincidunt. Nulla facilisi. Nunc condimentum
                dictum mattis.</p>


              <br><br>
              <a class="btn btn-primary" href="page-typography.html">Подробнее</a>
            </div>

            <div class="col-sm-12 col-md-6 hidden-xs hidden-sm">
              <br>
              <img class="center-block" src="assets/img/how-it-works.png" alt="how it works">
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
                <p>Designer, Developer, IT Service, Front-end developer, Project management</p>
              </a>

              <a href="job-list-2.html">
                <i class="fa fa-line-chart"></i>
                <h6>Accounting</h6>
                <p>Finance, Tax service, Payroll manager, Book keeper, Human resource</p>
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
            <h6 class="font-alt">Получай еженедельный топ новых вакансий на свой e-mail</h6>
            <br><br>
            <form class="form-subscribe" action="#">
              <div class="input-group">
                <input type="text" class="form-control input-lg" placeholder="Твой e-mail">
                <span class="input-group-btn">
                  <button class="btn btn-success btn-lg" type="submit">Подписаться</button>
                </span>
              </div>
            </form>
          </div>
        </section>
        <!-- END Newsletter -->


      </main>
      <!-- END Main container -->


      <!-- Site footer -->
      <footer class="site-footer">

        <!-- Top section -->
        <div class="container">
          <div class="row">
            <div class="col-sm-12 col-md-6">
              <h6>О нас</h6>
              <p class="text-justify">Мы создаем передовые технологии на всех доступных платформах для того, чтобы
                работодатели могли быстро найти подходящего сотрудника, а соискатели — хорошую работу.</p>
            </div>

            <div class="col-xs-6 col-md-3">
              <h6>Наша компания</h6>
              <ul class="footer-links">
                <li><a href="page-about.html">О нас</a></li>
                <li><a href="page-typography.html">Как это работает</a></li>
                <li><a href="page-faq.html">FAQ</a></li>
                <li><a href="page-typography.html">Политика безопасности</a></li>
                <li><a href="page-contact.html">Наши контакты</a></li>
              </ul>
            </div>

            <div class="col-xs-6 col-md-3">
              <h6>Самые популярные вакансии</h6>
              <ul class="footer-links">
                <li><a href="job-list.html">Фронт-энд девелопер</a></li>
                <li><a href="job-list.html">Android девелопер</a></li>
                <li><a href="job-list.html">iOS девелопер</a></li>
                <li><a href="job-list.html">Full stack девелопер</a></li>
                <li><a href="job-list.html">Руководитель проекта</a></li>
              </ul>
            </div>
          </div>

          <hr>
        </div>
        <!-- END Top section -->

        <!-- Bottom section -->
        <div class="container">
          <div class="row">
            <div class="col-md-8 col-sm-6 col-xs-12">
              <p class="copyright-text">Copyrights &copy; 2022 Все права защищены <a
                  href="http://themeforest.net/user/shamsoft">Python Style Group</a>.</p>
            </div>

            <div class="col-md-4 col-sm-6 col-xs-12">
              <ul class="social-icons">
                <li><a class="facebook" href="#"><i class="fa fa-facebook"></i></a></li>
                <li><a class="twitter" href="#"><i class="fa fa-twitter"></i></a></li>
                <li><a class="dribbble" href="#"><i class="fa fa-dribbble"></i></a></li>
                <li><a class="linkedin" href="#"><i class="fa fa-linkedin"></i></a></li>
                <li><a class="instagram" href="#"><i class="fa fa-instagram"></i></a></li>
              </ul>
            </div>
          </div>
        </div>
        <!-- END Bottom section -->

      </footer>
      <!-- END Site footer -->


      <!-- Back to top button -->
      <a id="scroll-up" href="#"><i class="ti-angle-up"></i></a>
      <!-- END Back to top button -->

      <!-- Scripts -->
      <script src="assets/js/app.min.js"></script>
      <script src="assets/js/custom.js"></script>

    </body>
  </div>
</template>

<script>
export default {
  name: 'IndexPage'
}
</script>

<style lang="scss">
body {
  font-family: Open Sans,sans-serif;
  font-size: 16px;
  line-height: 28px;
  color: #7e8890;
}
.navbar {
  display: flex;
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
.site-header {
  display: flex;
}
</style>
