<template>
  <div class="main__wrapp">
    <section class="news__list">
      <div class="news__container">
        <div class="news-item" v-for="item in newsList" :key="item.id">
          <div class="news-item__title">
            {{ item.title }}
          </div>
          <div class="news-item__text">
            {{ item.text }}
          </div>
          <div class="news-item__date">
            {{ item.date_publish }}
          </div>
          <!-- <div class="news-item__user">
            {{ item.user }}
          </div> -->
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { baseUrl, decode } from "../../store/constants.js";
import axios from "axios";
import Cookies from "universal-cookie";

export default {
  props: {
    newsList: {
      type: Array,
      default: () => [],
    }
  },
  data: () => {
    return {
    };
  },
}
