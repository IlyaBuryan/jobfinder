<template>
  <div>
    <div class="content_vacancy" v-for="(vacancy, id) in vacancyData" :key="id">
      <div class="content-wrap-vacancy">
        <div class="cont-text-vacancy">
          <h3>{{ vacancy.position }}</h3>
        </div>
      </div>
      <div class="button">
        <button class="btn btn-success btn-xl" style="background-color: #32CD32; border-color: #32CD32" href="#">Редактировать</button>
      </div>
      <div class="button">
        <button class="btn btn-success btn-xl" style="background-color: #E9967A; border-color: #E9967A" href="#">Удалить</button>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    vacancyData: {
      type: Array,
      default: () => {},
    },
    company: {
      type: Object,
      default: () => {},
    }
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
  margin-bottom:10px;
}

.content-wrap-vacancy {
  margin-left:30px;
  display: flex;
  margin-bottom: 20px;
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
