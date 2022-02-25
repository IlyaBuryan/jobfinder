<template>
  <div>
    <nuxt-link
      :to="`/vacancies/${vacancy.id}`"
      class="content_vacancy"
      v-for="vacancy in vacancyData"
      :key="vacancy.id"
    >
      <div class="content-wrap-vacancy">
        <div class="cont-text-vacancy">
          <h3>{{ vacancy.position }}</h3>
        </div>
      </div>
      <div class="button">
        <nuxt-link :to="`/vacancyEdit?id=${vacancy.id}`">
          <button
            class="btn btn-success btn-xl"
            style="background-color: #32cd32; border-color: #32cd32"
          >
            Редактировать
          </button>
        </nuxt-link>
      </div>
      <div class="button">
        <button
          class="btn btn-success btn-xl"
          style="background-color: #e9967a; border-color: #e9967a"
          @click="deleteVacancy(vacancy.id, $event)"
        >
          Удалить
        </button>
      </div>
    </nuxt-link>
  </div>
</template>

<script>
import { baseUrl } from "../store/constants.js";
import Cookies from "universal-cookie";
import axios from "axios";

export default {
  props: {
    vacancyData: {
      type: Array,
      default: () => [],
    },
    user: {
      type: Object,
      default: () => {},
    },
  },

  methods: {
    deleteVacancy(id, event) {
      event.preventDefault();
      location.reload();
      const cookies = new Cookies();
      let token = cookies.get("token");
      let headers = this.get_headers(token);
      axios
        .delete(`${baseUrl()}/vacancyapp/${id}/`, { headers })
        .then((response) => {
          console.log("Ваканси удалена");
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
  },
};
</script>

<style scoped>
.content_vacancy {
  background-color: #ddeeff;
  font-size: 18px;
  font-style: normal;
  color: #333333;
  line-height: 1.4em;
  letter-spacing: 0em;
  display: flex;
  margin-bottom: 10px;
}

.content-wrap-vacancy {
  margin-left: 200px;
  display: flex;
  margin-bottom: 20px;
}

.tab-item {
  color: blue;
  &_active {
    color: white;
    background-color: blue;
  }
}

.cont-text-vacancy {
  margin-top: 20px;
  margin-left: 40px;
  margin-right: 10px;
}
.button {
  margin-left: 10px;
}
.button:hover * {
  color: #333333;
}

.cont-text h2 {
  margin-bottom: 30px;
  font-size: 23px;
  font-style: normal;
  color: #333333;
  line-height: 1.4em;
  letter-spacing: 0em;
}
.btn-xl {
  height: 34px;
  line-height: 34px;
  padding: 0 20px;
  font-size: 14px;
  margin: 20px 0 0 0;
  text-align: right;
}
</style>
