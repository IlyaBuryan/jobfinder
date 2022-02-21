<template>
  <div>
    <nuxt-link
      :to="`/resumes/${resume.id}`"
      class="content_resume"
      v-for="resume in resumeData"
      :key="resume.id"
      >
      <div class="content-wrap-resume">
        <div class="cont-text-resume">
          <h3>{{ resume.position }}</h3>
        </div>
      </div>
      <div class="button">
        <nuxt-link :to="`/resumeEdit?id=${resume.id}`">
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
          @click="deleteResume(resume.id, $event)"
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
    resumeData: {
      type: Array,
      default: () => [],
    },
    worker: {
      type: Object,
      default: () => {},
    },
  },

 methods: {
    deleteResume(id, event) {
      event.preventDefault();
      location.reload();
      const cookies = new Cookies();
      let token = cookies.get("token");
      let headers = this.get_headers(token);
      axios
        .delete(`${baseUrl()}/resume/${id}/`, { headers })
        .then((response) => {
          console.log("Резюме удалено");
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
.content_resume {
  background-color: #ddeeff;
  font-size: 18px;
  font-style: normal;
  color: #333333;
  line-height: 1.4em;
  letter-spacing: 0em;
  display: flex;
  margin-bottom: 10px;
}
.content-wrap-resume {
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
.cont-text-resume {
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
