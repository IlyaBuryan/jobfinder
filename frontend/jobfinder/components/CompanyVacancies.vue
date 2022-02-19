<template>
  <div class="content_vacancy" v-for="vacancy in vacancyData" :key="vacancy.id>
    <div class="content-wrap">
      <div class="cont-text-vacancy">{{ vacancy.position }}</div>
    </div>
    <div class="button">
      <button class="btn btn-success btn-xl" style="background-color: #32CD32; border-color: #32CD32" href="#">Редактировать</button>
    </div>
      <div class="button">
      <button class="btn btn-success btn-xl" style="background-color: #E9967A; border-color: #E9967A" href="#">Удалить</button>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    vacancyData: {
      type: Object,
      default: () => {},
    },
    link: {
      type: String,
      default: () => "",
    },
  },
}
</script>

<style scoped>
.content_vacancy {
  background-color: #ddeeff;
  font-size: 18px;
  font-style: normal;
  color: #333333;
  line-height: 1.4em;
  letter-spacing: 0em;
  display:flex;
}

.content-wrap {
  display: flex;
  margin-bottom: 50px;
}

.tab-item {
  color:blue;
  &_active {
    color: white;
    background-color: blue;
  }
}

.cont-text-vacancy {
  margin-top:20px;
  margin-left: 40px;
  margin-right: 10px;
}
.button {
  margin-left: 10px;
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
