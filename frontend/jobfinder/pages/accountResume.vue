<!--<template>-->
<!--  <div class="main__wrapp">-->
<!--    <header class="header"></header>-->

<!--    <div class="container no-shadow">-->
<!--      <h1 class="text-center">Личный кабинет</h1>-->
<!--    </div>-->

<!--    <section class="content">-->
<!--      <div class="content-wrap">-->
<!--        <div class="item">-->
<!--          <img-->
<!--            src="~/assets/img/ava.png"-->
<!--            width="250"-->
<!--            height="250"-->
<!--            alt="avatar"-->
<!--          />-->
<!--        </div>-->
<!--        <div class="cont-text">-->
<!--          <h2>Данные о работнике:</h2>-->
<!--          <div v-if="worker">-->
<!--            <h4>Имя: {{ worker.first_name }}</h4>-->
<!--            <h4>Фамилия: {{ worker.last_name }}</h4>-->
<!--            <p>Дата рождения: {{ worker.birth_date }}</p>-->
<!--            <p>Телефон: {{ worker.phone }}</p>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </section>-->
<!--    <div class="tabs">-->
<!--      <ul class="breadcrumb">-->
<!--        <li-->
<!--          :class="{-->
<!--            'tab-item': true,-->
<!--            'tab-item_active': activeTab === 'myProfile',-->
<!--          }"-->
<!--          @click="changeActiveTab('myProfile')"-->
<!--        >-->
<!--          <nuxt-link to="/workerCard"> МОЙ ПРОФИЛЬ /</nuxt-link>-->
<!--        </li>-->

<!--        <li-->
<!--          :class="{-->
<!--            'tab-item': true,-->
<!--            'tab-item_active': activeTab === 'myResumes',-->
<!--          }"-->
<!--          @click="changeActiveTab('myResumes')"-->
<!--        >-->
<!--          <nuxt-link to="/accountResume"> МОИ РЕЗЮМЕ /</nuxt-link>-->
<!--          <div v-for="(item, id) in resumeList" :key="id">-->
<!--            <div>{{ item.position }}</div>-->
<!--            <nuxt-link class="btn btn-more" to="">Редактировать</nuxt-link>-->
<!--            <nuxt-link class="btn btn-more" to="">Удалить</nuxt-link>-->
<!--          </div>-->
<!--        </li>-->

<!--        <li-->
<!--          :class="{-->
<!--            'tab-item': true,-->
<!--            'tab-item_active': activeTab === 'myRequests',-->
<!--          }"-->
<!--          @click="changeActiveTab('myRequests')"-->
<!--        >-->
<!--          <nuxt-link to="/"> ОТКЛИКИ /</nuxt-link>-->
<!--        </li>-->

<!--        <li-->
<!--          :class="{-->
<!--            'tab-item': true,-->
<!--            'tab-item_active': activeTab === 'myInvites',-->
<!--          }"-->
<!--          @click="changeActiveTab('myInvites')"-->
<!--        >-->
<!--          <nuxt-link to="/"> ПРЕДЛОЖЕНИЯ /</nuxt-link>-->
<!--        </li>-->

<!--        <li-->
<!--          :class="{-->
<!--            'tab-item': true,-->
<!--            'tab-item_active': activeTab === 'myLetters',-->
<!--          }"-->
<!--          @click="changeActiveTab('myLetters')"-->
<!--        >-->
<!--          ПИСЬМА /-->
<!--        </li>-->
<!--      </ul>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { baseUrl, decode } from "../store/constants.js";-->
<!--import axios from "axios";-->
<!--import Cookies from "universal-cookie";-->

<!--export default {-->
<!--  data: () => {-->
<!--    return {-->
<!--      user: {},-->
<!--      worker: {},-->
<!--      resumeList: [],-->
<!--      activeTab: "myProfile",-->
<!--      activeTab: "myResumes",-->
<!--    };-->
<!--  },-->

<!--  async mounted() {-->
<!--    console.log("acc comm mounted");-->

<!--    await this.userRole();-->
<!--    this.getCard();-->
<!--  },-->

<!--  methods: {-->
<!--    getCard() {-->
<!--      const cookies = new Cookies();-->
<!--      let token = cookies.get("token");-->
<!--      let userId = decode(token).user_id;-->
<!--      let headers = this.get_headers(token);-->

<!--      axios-->
<!--        .get(`${baseUrl()}/worker/${this.user.worker}`, { headers })-->
<!--        .then((response) => {-->
<!--          this.worker = response.data;-->
<!--        })-->
<!--        .catch((error) => console.log(error));-->

<!--      axios-->
<!--        .get(`${baseUrl()}/resume/`, { headers })-->
<!--        .then((response) => {-->
<!--          this.resumeList = response.data;-->
<!--        })-->
<!--        .catch((error) => console.log(error));-->
<!--    },-->

<!--    async userRole() {-->
<!--      const cookies = new Cookies();-->
<!--      let token = cookies.get("token");-->
<!--      let userId = decode(token).user_id;-->
<!--      let headers = this.get_headers(token);-->

<!--      await axios-->
<!--        .get(`${baseUrl()}/user/${userId}/`, { headers })-->
<!--        .then((response) => {-->
<!--          this.user = response.data;-->
<!--        })-->
<!--        .catch((error) => console.log(error));-->
<!--    },-->

<!--    get_headers(access) {-->
<!--      let headers = {-->
<!--        "Content-Type": "application/json",-->
<!--      };-->
<!--      headers["Authorization"] = "Bearer " + access;-->
<!--      return headers;-->
<!--    },-->

<!--    changeActiveTab(tab) {-->
<!--      this.activeTab = tab;-->
<!--      console.log(`i am ${this.activeTab}`);-->
<!--    },-->
<!--  },-->
<!--};-->
<!--</script>-->

<!--<style lang="scss" scoped>-->
<!--.main__wrapp {-->
<!--  display: flex;-->
<!--  max-width: 100%;-->
<!--  flex-direction: column;-->
<!--}-->
<!--.page-header .container.no-shadow {-->
<!--  border: 1px solid #eee;-->
<!--  box-shadow: none;-->
<!--  justify-content: space-between;-->
<!--}-->
<!--.page-header .container.no-shadow h1 {-->
<!--  color: #373a3c;-->
<!--}-->
<!--.tabs {-->
<!--  width: 100%;-->
<!--  justify-content: space-between;-->
<!--  align-items: center;-->
<!--  min-height: 100vh;-->
<!--  margin-top: 50px;-->
<!--  margin-bottom: 50px;-->
<!--}-->
<!--.breadcrumb {-->
<!--  width: 100%;-->
<!--  justify-content: center;-->
<!--  display: center;-->
<!--}-->
<!--.container right {-->
<!--  display: justify;-->
<!--  margin-left: 10px;-->
<!--}-->
<!--.header {-->
<!--  display: flex;-->
<!--  height: 200px;-->
<!--  flex-direction: column;-->
<!--  background: url("~/assets/img/bg-banner1.jpg") no-repeat bottom center;-->
<!--  background-size: cover;-->
<!--  align-items: center;-->
<!--}-->
<!--.head__container {-->
<!--  max-width: 1800px;-->
<!--  margin-top: 150px;-->
<!--}-->

<!--.content {-->
<!--  background-color: #edeef0;-->
<!--  font-size: 18px;-->
<!--  font-style: normal;-->
<!--  color: #333333;-->
<!--  line-height: 1.4em;-->
<!--  letter-spacing: 0em;-->
<!--}-->

<!--.content-wrap {-->
<!--  display: flex;-->
<!--  margin-bottom: 50px;-->
<!--}-->

<!--.tab-item {-->
<!--  color: blue;-->
<!--  &_active {-->
<!--    color: white;-->
<!--    background-color: blue;-->
<!--  }-->
<!--}-->

<!--.cont-text {-->
<!--  margin-left: 40px;-->
<!--  margin-right: 10px;-->
<!--}-->

<!--.cont-text h2 {-->
<!--  margin-bottom: 30px;-->
<!--  font-size: 23px;-->
<!--  font-style: normal;-->
<!--  color: #333333;-->
<!--  line-height: 1.4em;-->
<!--  letter-spacing: 0em;-->
<!--}-->
<!--</style>-->
