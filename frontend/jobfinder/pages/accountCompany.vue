<template>
  <div class="main__wrapp">
    <header class="header"></header>

    <div class="container no-shadow">
      <h1 class="text-center">Личный кабинет</h1>
    </div>

    <section class="content">
      <div class="content-wrap">
        <div class="item">
          <img
            src="~/assets/img/ava_company.png"
            width="250"
            height="250"
            alt="avatar"
          />
        </div>
        <div class="cont-text" id="app">
          <h2>Данные о компании:</h2>
          <p>{{ company.name }}</p>
          <p>ИНН: {{ company.itn }}</p>
          <p>Отрасль: {{ company.category }}</p>
          <p>Детали: {{ company.company_details }}</p>
          <p>Описание: {{ company.description }}</p>
        </div>
      </div>
    </section>
    <div class="tabs">
      <ul class="breadcrumb">
        <nuxt-link :to="`/companyEdit?id=${company.id}`">
          <li
            :class="{
              'tab-item': true,
              'tab-item_active': activeTab === 'myProfile',
            }"
            @click="changeActiveTab('myProfile')"
          >
            РЕДАКТИРОВАНИЕ ПРОФИЛЯ /
          </li>
        </nuxt-link>
        <li
          :class="{
            'tab-item': true,
            'tab-item_active': activeTab === 'myVacancies',
          }"
          @click="changeActiveTab('myVacancies')"
        >
          МОИ ВАКАНСИИ /
        </li>
        <li
          :class="{
            'tab-item': true,
            'tab-item_active': activeTab === 'myRequests',
          }"
          @click="changeActiveTab('myRequests')"
        >
          ОТКЛИКИ /
        </li>
        <li
          :class="{
            'tab-item': true,
            'tab-item_active': activeTab === 'myInvites',
          }"
          @click="changeActiveTab('myInvites')"
        >
          ПРЕДЛОЖЕНИЯ /
        </li>
        <li
          :class="{
            'tab-item': true,
            'tab-item_active': activeTab === 'myLetters',
          }"
          @click="changeActiveTab('myLetters')"
        >
          ПИСЬМА /
        </li>
      </ul>
      <CompanyVacancies
        v-if="activeTab === 'myVacancies'"
        :vacancyData="vacancyList"
        :company="company"
      />
      <MessageVacancy
        v-if="activeTab === 'myRequests'"
        :vacancyData="vacancyList"
        :company="company"
      />
      <InvitesResume
        v-if="activeTab === 'myInvites'"
        :vacancyData="vacancyList"
        :company="company"
      />
    </div>
  </div>
</template>

<script>
import CompanyVacancies from "@/components/CompanyVacancies";
import { baseUrl, decode } from "../store/constants.js";
import axios from "axios";
import Cookies from "universal-cookie";

export default {
  components: { CompanyVacancies },
  data: () => {
    return {
      user: {},
      company: {},
      activeTab: "myVacancies",
      vacancyList: [],
    };
  },

  async mounted() {
    console.log("acc comm mounted");

    await this.userRole();
    this.getCard();
  },

  methods: {
    getCard() {
      const cookies = new Cookies();
      let token = cookies.get("token");
      let userId = decode(token).user_id;
      let headers = this.get_headers(token);

      axios
        .get(`${baseUrl()}/companyapp/${this.user.company}`, { headers })
        .then((response) => {
          this.company = response.data;
          console.log(response.data);
        })
        .catch((error) => console.log(error));

      axios
        .get(`${baseUrl()}/vacancyapp/`, { headers })
        .then((response) => {
          this.vacancyList = response.data;
        })
        .catch((error) => console.log(error));
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
    changeActiveTab(tab) {
      this.activeTab = tab;
      console.log(`i am ${this.activeTab}`);
    },
  },
};
</script>

<style scoped>
.main__wrapp {
  display: flex;
  max-width: 100%;
  flex-direction: column;
}

.page-header .container.no-shadow {
  border: 1px solid #eee;
  box-shadow: none;
  justify-content: space-between;
}

.page-header .container.no-shadow h1 {
  color: #373a3c;
}

.tabs {
  width: 100%;
  justify-content: space-between;
  align-items: center;
  min-height: 100vh;
  margin-top: 50px;
  margin-bottom: 50px;
}

.breadcrumb {
  width: 100%;
  justify-content: center;
  display: center;
}

.container right {
  display: justify;
  margin-left: 10px;
}

.header {
  display: flex;
  height: 200px;
  flex-direction: column;
  background: url("~/assets/img/bg-banner1.jpg") no-repeat bottom center;
  background-size: cover;
  align-items: center;
}

.head__container {
  max-width: 1800px;
  margin-top: 150px;
}

.content {
  background-color: #edeef0;
  font-size: 18px;
  font-style: normal;
  color: #333333;
  line-height: 1.4em;
  letter-spacing: 0em;
}

.content-wrap {
  margin-top: 40px;
  margin-left: 30px;
  display: flex;
  margin-bottom: 40px;
}

.tab-item {
  color: blue;
  &_active {
    color: white;
    background-color: blue;
  }
}

.cont-text {
  margin-left: 40px;
  margin-right: 10px;
}

.cont-text h2 {
  margin-bottom: 30px;
  font-size: 23px;
  font-style: normal;
  color: #333333;
  line-height: 1.4em;
  letter-spacing: 0em;
}
</style>
