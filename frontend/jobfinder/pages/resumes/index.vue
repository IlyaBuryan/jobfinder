<template>
  <div class="main__wrapp">
    <!-- Page header -->
    <header class="header">
      <div class="head__container">
        <h1 class="text-center">Найти резюме</h1>
        <p class="lead text-center">Воспользуйтесь полями ниже для поиска подходящего резюме</p>
      </div>

      <div class="filter__container">
        <form action="#">

          <div class="filter__container_header">
            <div class="form-group col-xs-12 col-sm-4">
              <input type="text" class="form-control"
                placeholder="Ключевые слова: название должности">
            </div>

            <div class="form-group col-xs-12 col-sm-4">
              <input type="text" class="form-control" placeholder="Местоположение: город, область или почтовый индекс">
            </div>

            <div class="form-group col-xs-12 col-sm-4">
              <select class="form-control selectpicker" multiple>
                <option selected>Все категории</option>
                <option>Разработка</option>
                <option>Дизайн</option>
                <option>Работа с клиентами</option>
                <option>Финансы</option>
                <option>Здравоохранение</option>
                <option>Продажи</option>
                <option>Строительство</option>
                <option>Маркетинг</option>
                <option>Информационные технологии</option>
                <option>Другое</option>
              </select>
            </div>
          </div>
          <div class="filter__container_footer">

            <div class="form-group col-xs-12 col-sm-4">
              <h6>Режим работы</h6>
              <div class="checkall-group">
                <div class="checkbox">
                  <input type="checkbox" id="contract1" name="contract" checked>
                  <label for="contract1">Любой</label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="contract2" name="contract">
                  <label for="contract2">Полная занятость <small>(354)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="contract3" name="contract">
                  <label for="contract3">Частичная занятость <small>(284)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="contract4" name="contract">
                  <label for="contract4">Стажировка <small>(169)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="contract5" name="contract">
                  <label for="contract5">Фриланс <small>(480)</small></label>
                </div>
              </div>
            </div>


            <div class="form-group col-xs-12 col-sm-4">
              <h6>Оплата в час</h6>
              <div class="checkall-group">
                <div class="checkbox">
                  <input type="checkbox" id="rate1" name="rate" checked>
                  <label for="rate1">Любая</label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="rate2" name="rate">
                  <label for="rate2">$0 - $50 <small>(364)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="rate3" name="rate">
                  <label for="rate3">$50 - $100 <small>(684)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="rate4" name="rate">
                  <label for="rate4">$100 - $200 <small>(195)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="rate5" name="rate">
                  <label for="rate5">$200+ <small>(39)</small></label>
                </div>
              </div>
            </div>


            <div class="form-group col-xs-12 col-sm-4">
              <h6>Ученая степень</h6>
              <div class="checkall-group">
                <div class="checkbox">
                  <input type="checkbox" id="degree1" name="degree" checked>
                  <label for="degree1">Все</label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="degree2" name="degree">
                  <label for="degree2">Ассистент <small>(216)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="degree3" name="degree">
                  <label for="degree3">Бакалавр <small>(569)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="degree4" name="degree">
                  <label for="degree4">Магистр <small>(439)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="degree5" name="degree">
                  <label for="degree5">Докторская степень <small>(84)</small></label>
                </div>
              </div>
            </div>

          </div>

          <div class="button-group">
            <div class="action-buttons">
              <button class="btn btn-primary">Применить фильтр</button>
            </div>
          </div>

        </form>

      </div>

    </header>
    <!-- END Page header -->


    <!-- Main container -->
    <main class="vacancy">
      <section class="vacancy__list">
        <div class="vacancy__container">
          <div class="vacancy__container_head">
            <div class="vacancy__container_head-title">
              <br>
              <h5>Мы нашли <strong>357</strong> совпадений, вы смотрите от <i>10</i> до <i>20</i></h5>
            </div>
          </div>
          <!-- Job item -->

          <div class="vacancy-item" v-for="(item, id) in resumeList" :key="id">
            <nuxt-link :to="`/resumes/${item.id}`" style="textDecoration:none">
              <div class="vacancy-item__block">
                <div class="vacancy-item__info">
                  <div class="vacancy-item__info_main">
                    <div class="vacancy-item__info_main-name">{{ item.position }}</div>
                    <div class="vacancy-item__info_main-name"><img src="~/assets/img/ava-5.png" width="150" height="150" alt="avatar"></div>
                  </div>
                   <div class="vacancy-item__info_descr" v-for="worker in workerList" :key="worker.id" >
                    <div><b>Данные:</b> {{ worker.first_name }} {{ worker.last_name }}</div>
                    <div><b>Телефон:</b> {{ worker.phone }}</div>
                   </div>
                  <br/>
                  <div class="vacancy-item__info_descr" v-for="experience in experienceList" :key="experience.id" >
                    <div><b>Место работы:</b> {{ experience.organization }}</div>
                    <div><b>Должность:</b> {{ experience.position }}</div>
                  <br/>
                  </div>
                  <div class="vacancy-item__info_footer">
                    <div class="vacancy-item__info_footer-city"><b>О себе:</b> {{ item.info }}</div>
                  </div>
                </div>
              </div>
            </nuxt-link>
          </div>
          <!-- END Job item first-->

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
import {baseUrl, decode} from "../../store/constants.js";
import axios from "axios";
import Cookies from "universal-cookie";

export default {
  data: () => {
    return {
      user: {},
      resumeList: [],
      workerList: [],
      experienceList: []
    }
  },


  async mounted() {
    console.log('acc comm mounted');

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
        .get(`${baseUrl()}/resume/`, {headers})
        .then((response) => {
          this.resumeList = response.data;
        })
        .catch((error) => console.log(error));

      axios
        .get(`${baseUrl()}/worker_card/`, {headers})
        .then((response) => {
          this.workerList = response.data;
        })
        .catch((error) => console.log(error));

      axios
        .get(`${baseUrl()}/work_experience/`, {headers})
        .then((response) => {
          this.experienceList = response.data;
        })
        .catch((error) => console.log(error));
      },

    async userRole() {
      const cookies = new Cookies();
      let token = cookies.get("token");
      let userId = decode(token).user_id;
      let headers = this.get_headers(token);

      await axios
        .get(`${baseUrl()}/user/${userId}/`, {headers})
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
  }
}
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
  background: url('~/assets/img/bg-banner2.jpg') no-repeat bottom center;
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
.vacancy {
  flex-direction: column;
  justify-content: flex-start;
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
.vacancy-item {
  &__block {
    display: flex;
    cursor: pointer;
    width: 100%;
    justify-content: flex-start;
    margin: 30px 0;
    transition-property: border;
    transition-duration: .2s;
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
      justify-content: flex-start;
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
        opacity: .85;
        background-color: #5cb85c;
      }
    }
    &_footer {
      display: flex;
      justify-content: flex-start;
      max-width: 50%;
    }
  }
}
</style>
