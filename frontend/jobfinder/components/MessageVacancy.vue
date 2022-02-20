<template>
  <div>
    <div
      class="content_vacancy"
      v-for="vacancy in vacancyData"
      :key="vacancy.id"
    >
      <div class="content-wrap-vacancy">
        <div class="cont-text-vacancy">
          <h3>{{ vacancy.position }}</h3>
        </div>
        <div>
           <h4>Данные работника: {{ vacancy.company_name }}</h4>
           <h4><em>откликнулся {{ vacancy.published_date }}</em></h4>
           <br/>
           <h4>Телефон: {{ vacancy.city }}</h4>
           <h4>Образование: </h4>
           <h4>Доп. информация: </h4>
        </div>
        <div>
        <button
            class="btn btn-success btn-xl"
            style="background-color: #32cd32; border-color: #32cd32"
          >
            Отправить ответ
          </button>
        </div>
      </div>
    </div>
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
      default: () => {},
    },
    company: {
      type: Object,
      default: () => {},
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
  &_active {
    color: white;
    background-color: blue;
  }
}

.cont-text-vacancy {
  margin:5px auto 5px;
  margin-left:300px;

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
