<template>
  <div class="main__wrapp">
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
  </div>
</template>

<script>
import SingleLink from "@/components/SingleLink";
import Cookies from "universal-cookie";
import {baseUrl, decode} from "@/store/constants";
import axios from "axios";
import WorkerResume from "@/pages/workerResume";

export default {
  props: {
    rezumeData: {
      type: Array,
      default: () => [],
      resumeList: []
    },
  },
};
// export default {
//   name: "WorkersResumes"
// }
</script>

<style scoped>

</style>
