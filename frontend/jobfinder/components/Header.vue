<template>
 <!-- Navigation bar -->
      <nav class="navbar" :style="`background: url(${require('/assets/img/bg-banner1.jpg')}) no-repeat center`">
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
</template>

