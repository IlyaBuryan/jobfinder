<template>
  <!-- Navigation bar -->
  <nav class="navbar">
    <div class="header-wrap">
      <!-- Logo -->
      <div class="logo-wrapper">
        <NuxtLink class="logo" to="/">
          <img :src="`${require('/assets/img/logo.png')}`" alt="logo" />
        </NuxtLink>
      </div>
      <!-- END Logo -->

      <!-- Navigation menu -->
      <ul class="menu-wrapper">
        <li @mouseover="mouseOnMain = true" @mouseleave="mouseOnMain = false">
          <NuxtLink class="active" to="/">Главная</NuxtLink>
          <ul v-if="mouseOnMain" class="nav-menu__ul_el">
            <li>
              <NuxtLink to="/">Вариант 1</NuxtLink>
            </li>
            <li>
              <NuxtLink to="/">Вариант 2</NuxtLink>
            </li>
          </ul>
        </li>
        <li
          @mouseover="mouseOnVacancies = true"
          @mouseleave="mouseOnVacancies = false"
        >
          <NuxtLink to="/">Вакансии</NuxtLink>
          <ul v-if="mouseOnVacancies" class="nav-menu__ul_el">
            <li><NuxtLink to="/">Вариант 1</NuxtLink></li>
            <li><NuxtLink to="/">Вариант 2</NuxtLink></li>
            <li><NuxtLink to="/">Вариант 3</NuxtLink></li>
          </ul>
        </li>
        <li
          @mouseover="mouseOnResume = true"
          @mouseleave="mouseOnResume = false"
        >
          <NuxtLink to="/">Резюме</NuxtLink>
          <ul v-if="mouseOnResume" class="nav-menu__ul_el">
            <li><NuxtLink to="/">Вариант 1</NuxtLink></li>
            <li><NuxtLink to="/">Вариант 2</NuxtLink></li>
            <li><NuxtLink to="/">Вариант 3</NuxtLink></li>
          </ul>
        </li>
        <li
          @mouseover="mouseOnCompanies = true"
          @mouseleave="mouseOnCompanies = false"
        >
          <NuxtLink to="/">Компании</NuxtLink>
          <ul v-if="mouseOnCompanies" class="nav-menu__ul_el">
            <li><NuxtLink to="/companyCard">Заполнить карточку</NuxtLink></li>
            <li><NuxtLink to="/companyVacancy">Создать вакансию</NuxtLink></li>
          </ul>
        </li>
        <li @mouseover="mouseOnPages = true" @mouseleave="mouseOnPages = false">
          <NuxtLink to="/">Страницы</NuxtLink>
          <ul v-if="mouseOnPages" class="nav-menu__ul_el">
            <li><NuxtLink to="/">Вариант 1</NuxtLink></li>
            <li><NuxtLink to="/">Вариант 2</NuxtLink></li>
            <li><NuxtLink to="/">Вариант 3</NuxtLink></li>
          </ul>
        </li>
      </ul>
      <!-- END Navigation menu -->

      <!-- User account -->
      <div class="login-wrapper">
        <NuxtLink class="btn btn-primary" to="/login"> Авторизация </NuxtLink>
        <p class="or">или</p>
        <NuxtLink class="btn btn-outline-dark" to="/register">
          Регистрация
        </NuxtLink>
      </div>
      <!-- END User account -->
    </div>
  </nav>
  <!-- END Navigation bar -->
</template>

<script>
import SingleLink from "@/components/SingleLink.vue";
export default {
  components: { SingleLink },
  data: () => ({
    mouseOnMain: false,
    mouseOnVacancies: false,
    mouseOnResume: false,
    mouseOnCompanies: false,
    mouseOnPages: false,
  }),
};
</script>

<style scoped >
.navbar {
  width: 100%;
  background-color: transparent;
  position: absolute;
  top: 50px;
  display: flex;
  justify-content: center;
}

.header-wrap {
  display: flex;
  justify-content: space-between;
}

.logo-wrapper {
  align-items: center;
  justify-content: center;
}

.menu-wrapper {
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.menu-wrapper .nuxt-link-active {
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 1px;
  padding: 0 12px;
  line-height: 60px;
  color: #fff;
  transition: color 0.2s linear;
}

.menu-wrapper .nuxt-link-active:hover {
  color: #bbb;
  text-decoration: none;
}

.menu-wrapper .active {
  font-size: 18px;
  font-weight: bold;
}

.menu-wrapper > li {
  list-style: none;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 1px;
  padding: 0 12px;
  line-height: 60px;
  color: #bbb;
  padding: 0;
}

.menu-wrapper > li > ul {
  margin: 0;
  padding: 0 0 0 25px;
  width: 200px;
  list-style: none;
  display: flex;
  flex-direction: column;
  position: absolute;
  z-index: 100;
  background-color: #fff;
}

.menu-wrapper > li > ul > li > .nuxt-link-active,
.menu-wrapper > li > ul > li > a {
  font-family: Open Sans, sans-serif;
  text-transform: none;
  letter-spacing: 1px;
  line-height: 32px;
  padding-top: 3px;
  padding-bottom: 3px;
  white-space: nowrap;
  display: block;
  min-width: 150px;
  font-weight: 500;
  font-size: 13px;
  color: #7e8890;
  border-bottom: 1px solid #f8f9fa;
}

.menu-wrapper > li > ul:before {
  content: "";
  position: absolute;
  top: -4px;
  left: 30px;
  width: 0;
  height: 0;
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-bottom: 4px solid #fff;
}

.login-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
}
.or {
  margin: 0 30px;
}
</style>
