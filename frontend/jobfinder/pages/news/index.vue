<template>
  <div class="main__wrapp">
    <!-- Page header -->
    <header class="header">
      <div class="head__container">
        <h1 class="text-center">Новости</h1>
      </div>
    </header>
    <!-- END Page header -->

    <!-- Main container -->
    <main class="news">
      <section class="news__list">
        <div class="news__container">
          <!-- <div class="news__container_head">
            <div class="news__container_head-title">
              <br />
            </div>
          </div> -->
          <!-- News item -->

          <div class="news-item" v-for="item in newsList" :key="item.id">
            <nuxt-link
              :to="`/news/${item.id}`"
              style="textdecoration: none"
            >
              <div class="news-item__block">
                <div class="news-item__info">
                  <div class="news-item__info_main">
                    <div class="news-item__info_main-name">
                      {{ item.position }}
                    </div>
                    <div class="news-item__info_main-name">
                      {{ item.salary }}
                    </div>
                  </div>
                  <br />
                  <div class="news-item__info_descr">
                    <img src="~/assets/img/office_icon.png" alt="icon" />
                    {{ item.company_name }}
                  </div>
                  <div class="news-item__info_footer">
                    <div class="news-item__info_footer-city">
                      {{ item.city }}
                    </div>
                  </div>
                  <br />
                  <div class="content">
                    <div><b>Заголовок:</b> {{ item.title }}</div>
                    <div><b>Текст:</b> {{ item.text }}</div>
                    <br />
                    <div>{{ item.date_publish }}</div>
                  </div>
                </div>
              </div>
            </nuxt-link>
          </div>
          <!-- END News item first-->

          <!-- Page navigation -->
          <nav class="text-center">
            <ul class="pagination">
              <li>
                <a href="#" aria-label="Previous">
                  <i class="ti-angle-left"></i>
                </a>
              </li>
              <li><a href="#">1</a></li>
              <li class="active"><a href="#">2</a></li>
              <li><a href="#">3</a></li>
              <li><a href="#">4</a></li>
              <li>
                <a href="#" aria-label="Next">
                  <i class="ti-angle-right"></i>
                </a>
              </li>
            </ul>
          </nav>
          <!-- END Page navigation -->
        </div>
      </section>
    </main>
    <!-- END Main container -->
  </div>
</template>

<script>
import { baseUrl, decode } from "../../store/constants.js";
import axios from "axios";
import Cookies from "universal-cookie";

export default {
  data: () => {
    return {
      newsList: [],
    };
  },

  mounted() {
    this.getCard();
  },

  methods: {
    async getCard() {
      const cookies = new Cookies();
      let token = cookies.get("token");
      let headers = this.get_headers(token);

      await axios
        .get(`${baseUrl()}/news/`, { headers })
        .then((response) => {
          this.newsList = response.data;
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

<style lang="scss">
.main__wrapp {
  display: flex;
  max-width: 100%;
  flex-direction: column;
}
.header {
  display: flex;
  height: 700px;
  flex-direction: column;
  background: url("~/assets/img/bg-banner2.jpg") no-repeat bottom center;
  background-size: cover;
  align-items: center;
}
.head__container {
  max-width: 1800px;
  margin-top: 150px;
}
.filter__container {
  display: flex;
  flex-direction: column;
  width: 90%;
  &_header {
    display: flex;
  }
  &_footer {
    display: flex;
  }
}
.content {
  text-align: left;
}
.news {
  justify-content: flex-start;
  display: flex;
  flex-direction: column;
  max-width: 1800px;
  min-width: 800px;
  align-self: center;
  &__list {
    display: flex;
    flex-direction: column;
  }
  &__container {
    &_head {
      display: flex;
      justify-content: flex-start;
      &-title {
        display: flex;
        justify-content: flex-start;
      }
    }
  }
}
.news-item {
  &__block {
    display: flex;
    cursor: pointer;
    width: 100%;
    justify-content: flex-start;
    margin: 30px 0;
    transition-property: border;
    transition-duration: 0.2s;
    flex-grow: 1;
    // &:hover {
    //   border: 1px solid #29aafe;
    // }
  }

  // &__img {
  //  display: flex;
  //  padding: 0 30px;
  //  align-items: center;
  //  max-width: 300px;
  //  img {
  //    width: 240px;
  //  }
  //}
  &__info {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    width: 100%;
    padding: 0 30px;
    color: dimgray;
    &_main {
      display: flex;
      justify-content: space-between;
      &-name {
        font-size: 36px;
        line-height: 40px;
        color: #55595c;
        font-family: Arial, sans-serif;
        font-weight: 400;
      }
      &-city {
        color: #96a2b2;
        line-height: 35px;
        font-size: 30px;
      }
    }
    &_add {
      display: flex;
      justify-content: space-between;
      &-company {
        font-size: 36px;
        line-height: 40px;
        color: #55595c;
      }
      &-worktime {
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 30px;
        color: white;
        font-weight: 400;
        border-radius: 0;
        padding: 4px 6px;
        margin-top: 6px;
        margin-left: 16px;
        opacity: 0.85;
        background-color: #5cb85c;
      }
    }
    &_footer {
      display: flex;
      justify-content: space-between;
      max-width: 50%;
    }
  }
}
</style>
