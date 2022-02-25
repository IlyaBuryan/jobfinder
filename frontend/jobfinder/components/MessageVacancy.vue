<template>
  <div>
    <div class="content_vacancy" v-for="item in messagesData" :key="item.id">
      <div class="content-wrap-vacancy">
        <div class="cont-text-vacancy">
          <p v-if="item.response_status == ''">Ожидает вашего ответа</p>
          <p style="color: red" v-if="item.response_status == '1'">Отказано</p>
          <p style="color: green" v-if="item.response_status == '2'">
            Выслано приглашение
          </p>
          <h3>{{ item.vacancy.position }}</h3>
          <h4>Город: {{ item.vacancy.city }}</h4>
        </div>
        <br />
        <div>
          <h4>Имя: {{ item.resume.worker_info.first_name }}</h4>
          <h4>Фамилия: {{ item.resume.worker_info.last_name }}</h4>
          <h4>Почта: {{ item.user.email }}</h4>
          <h4>Телефон: {{ item.resume.worker_info.phone }}</h4>
          <h4>Образование: {{ item.resume.institution }}</h4>
          <h4>
            <em>откликнулся {{ item.vacancy.published_date }}</em>
          </h4>
          <h4>Должность в резюме: {{ item.resume.position }}</h4>
          <br />
        </div>
        <div>
          <button
            class="btn btn-danger btn-xl"
            @click="refuseResponseStatus(item)"
          >
            Отказать
          </button>
          <button
            class="btn btn-success btn-xl"
            @click="inviteResponseStatus(item)"
          >
            Пригласить
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Cookies from "universal-cookie";
import axios from "axios";
import { baseUrl } from "../store/constants.js";

export default {
  props: {
    messagesData: {
      type: Array,
      default: () => {},
    },
  },

  data: () => {
    return {
      user: "",
      resume: "",
      vacancy: "",
    };
  },

  mounted() {
    this.collectIds();
    this.markViewed();
  },

  methods: {
    collectIds() {
      this.messagesData.map((item) => {
        this.user = item.user.id;
        this.resume = item.resume.id;
        this.vacancy = item.vacancy.id;
      });
    },

    getIds(item) {
      let new_item = {
        ...item,
      };
      new_item.user = this.user;
      new_item.resume = this.resume;
      new_item.vacancy = this.vacancy;

      return new_item;
    },

    markViewed() {
      const cookies = new Cookies();
      let token = cookies.get("token");
      let headers = this.get_headers(token);
      this.messagesData.map((item) => {
        item.is_viewed = true;
        const newItem = this.getIds(item);
        axios.patch(`${baseUrl()}/message_to_vacancy/${newItem.id}/`, newItem, {
          headers,
        });
      });
    },

    refuseResponseStatus(item) {
      const cookies = new Cookies();
      let token = cookies.get("token");
      let headers = this.get_headers(token);
      item.response_status = 1;
      const newItem = this.getIds(item);
      axios.patch(`${baseUrl()}/message_to_vacancy/${newItem.id}/`, newItem, {
        headers,
      });
    },

    inviteResponseStatus(item) {
      const cookies = new Cookies();
      let token = cookies.get("token");
      let headers = this.get_headers(token);
      item.response_status = 2;
      const newItem = this.getIds(item);
      axios.patch(`${baseUrl()}/message_to_vacancy/${newItem.id}/`, newItem, {
        headers,
      });
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
  margin-left: 300px;
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.tab-item {
  color: blue;
}

.cont-text-vacancy {
  margin: 5px auto 5px;
  margin-left: 300px;
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
