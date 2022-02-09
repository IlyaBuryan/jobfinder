<template>
  <div class="main__wrapp">
    <!-- Page header -->
    <header class="header">
     </header>
      <div class="container no-shadow">
        <h1 class="text-center">Личный кабинет</h1>
      </div>
    <div class="row">

      <div class="col-1-3">
        <img class="avatar" src="~/assets/img/ava.png" width="250" height="250" alt="avatar"/>
      </div>

      <div class="col-2-3">
        <h2>{{ worker.first_name }} {{ worker.last_name }}</h2>
        <p>{{ worker.phone }}</p>
        <p>Данные о работнике</p>
      </div>
    </div>
      <div class="tabs">
        <ul class="breadcrumb">
          <li class="breadcrumb-item"><a href="#">МОИ РЕЗЮМЕ</a></li>
          <li class="breadcrumb-item"><a href="#">ОТКЛИКИ</a></li>
          <li class="breadcrumb-item"><a href="#">ПРЕДЛОЖЕНИЯ</a></li>
          <li class="breadcrumb-item"><a href="#">ПИСЬМА</a></li>
        </ul>
      </div>

  </div>
</template>

<script>
  import { baseUrl, decode } from "../store/constants.js";
  export default {
    head() {
      },
    async asyncData({ $axios, params }) {
      try {
        let worker = await
        $axios.$get('${baseUrl()}/worker/${workerId}/');
        return { worker };
      } catch (e) {
        return { worker: [] };
      }
    },
    data () {
      return {
        worker: {
          first_name: "",
          last_name: "",
          phone: ""
        }
      };
    }
  };
</script>



<style scoped>

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
  margin-top:50px;
  margin-bottom:50px;
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
  background: url('~/assets/img/bg-banner1.jpg') no-repeat bottom center;
  background-size: cover;
  align-items: center;
}
.head__container {
  max-width: 1800px;
  margin-top: 150px;
}

.col-1-3 {
  width: 33.3333333333%;
  float: left;
  margin-left:10px;
}

.col-2-3 {
  width: 66.6666666667%;
  float: left;
}

</style>
