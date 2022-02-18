<template>
  <div class="main__wrapp">
    <h1>Этом мое резюме №1</h1>
            <!-- Job item -->
    <div class="vacancy-item" v-for="(item, id) in resumeData" :key="id">
      <nuxt-link :to="`/resumes/${item.id}`" style="textDecoration:none">
        <div class="vacancy-item__block">
          <div class="vacancy-item__info">
            <div class="vacancy-item__info_main">
              <div class="vacancy-item__info_main-name">{{ item.position }}</div>
              <div class="vacancy-item__info_main-name"><img src="~/assets/img/ava-5.png" width="150" height="150" alt="avatar"></div>
            </div>
              <div class="vacancy-item__info_descr">
              <div><b>Данные:</b> {{ worker.first_name }} {{ worker.last_name }}</div>
              <div><b>Телефон:</b> {{ worker.phone }}</div>
              </div>
            <br/>
            <div class="vacancy-item__info_descr" v-for="(experience, id) in item.experience" :key="id">
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
  </div>
</template>

<script>

export default {
  props: {
    resumeData: {
      type: Array,
      default: () => [],
      resumeList: []
    },
    worker: {
      type: Object,
      default: () => {},

    }
  },
};
// export default {
//   name: "WorkersResumes"
// }
</script>

<style scoped lang="scss">
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
  display: flex;
  margin-bottom: 50px;
}-->

.tab-item {
  color:blue;
  &_active {
    color: white;
    background-color: blue;
  }
}

.cont-text {margin-left: 40px;
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
