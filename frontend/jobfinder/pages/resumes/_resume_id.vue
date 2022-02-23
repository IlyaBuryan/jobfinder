<template>
  <div class="resume_wrapp">
    <!-- Page header -->
    <header class="page-header">
      <div class="container">
        <div class="header-detail">
          <div class="header-detail__head">
            <!-- <img class="logo" :src="resume.img" alt=""> -->
            <div class="header-detail__head_main">
              <div class="hgroup">
                <h1>{{ resume.position }}</h1>
                <!-- <h3><a href="#">{{ resume.worker_info.first_name }} {{ resume.worker_info.last_name }}</a></h3> -->
              </div>
              <div class="header-detail__head_main-time">
                {{ resume.published_date }}
              </div>
            </div>
          </div>
          <hr />
          <p class="header-detail__head_main-descr">{{ resume.institution }}.</p>
          <div class="header-detail__footer">
            <ul class="header-detail__head_main-params">
              <li>
                <i class="fa fa-map-marker"></i>
                <span>{{ resume.courses }}</span>
              </li>

              <!-- <li>
                <i class="fa fa-briefcase"></i>
                <span>{{ resume.conditions }}</span>
              </li> -->

              <!-- <li>
                <i class="fa fa-money"></i>
                <span>{{ resume.salary }}</span>
              </li> -->
            </ul>
            <ul class="header-detail__head_main-params">
              <li>
                <i class="fa fa-clock-o"></i>
                <span>40h / week</span>
              </li>

              <li>
                <i class="fa fa-flask"></i>
                <span>2+ years experience</span>
              </li>

              <li>
                <i class="fa fa-certificate"></i>
                <a href="#">Высшее</a>
              </li>
            </ul>
          </div>

          <div class="button-group">
            <ul class="social-icons">
              <li class="title">Разместить на</li>
              <li>
                <a class="facebook" href="#"><i class="fa fa-facebook"></i></a>
              </li>
              <li>
                <a class="google-plus" href="#"
                  ><i class="fa fa-google-plus"></i
                ></a>
              </li>
              <li>
                <a class="twitter" href="#"><i class="fa fa-twitter"></i></a>
              </li>
              <li>
                <a class="linkedin" href="#"><i class="fa fa-linkedin"></i></a>
              </li>
            </ul>

            <div class="action-buttons">
              <a class="btn btn-success" href="#">Отправить предложение</a>
              <Message></Message>
            </div>
          </div>
        </div>
      </div>
    </header>
    <!-- END Page header -->

    <!-- Main container -->
    <main>
      <!-- Job detail -->
      <section class="resume-info">
        <div class="resume-info__container">
          <br />
          <h4>О себе</h4>
          <p>{{ resume.info }}</p>
          <!-- <ul>
            <li>Build next-generation web applications with a focus on the client side.</li>
            <li>Redesign UI's, implement new UI's, and pick up Java as necessary.</li>
            <li>Explore and design dynamic and compelling consumer experiences.</li>
            <li>Design and build scalable framework for web applications.</li>
          </ul> -->

          <br />
          <h4>Minimum qualifications</h4>
          <ul>
            <li>
              BA/BS degree in a technical field or equivalent practical
              experience.
            </li>
            <li>
              2 years of relevant work experience in software development.
            </li>
            <li>Programming experience in C, C++ or Java.</li>
            <li>Experience with AJAX, HTML and CSS.</li>
          </ul>

          <br />
          <h4>Preferred qualifications</h4>
          <ul>
            <li>Interest in user interface design.</li>
            <li>Web application development experience.</li>
            <li>Experience working on cross-browser platforms.</li>
            <li>
              Development experience designing object-oriented JavaScript.
            </li>
            <li>
              Experience with user interface frameworks such as XUL, Flex and
              XAML.
            </li>
            <li>Knowledge of user interface design.</li>
          </ul>
        </div>
      </section>
      <!-- END Job detail -->
    </main>
    <!-- END Main container -->
  </div>
</template>

<script>
import Message from "@/components/Message.vue";
import { baseUrl, decode } from "../../store/constants.js";
import axios from "axios";
import Cookies from "universal-cookie";
export default {
  components: { Message },
  data() {
    return {
      loading: false,
      resumeList: [],
      resume: {},
      worker: {},
      workerList: [],
      workerId: "",

    };
  },
  async mounted() {
    this.getCard();
  },

  methods: {
    getCard() {
      const cookies = new Cookies();
      let token = cookies.get("token");
      let userId = decode(token).user_id;
      let headers = this.get_headers(token);

      axios
        .get(`${baseUrl()}/resume/${this.$route.params.resume_id}`, {
          headers,
        })
        .then((response) => {
          this.resume = response.data;
          console.log(this.resume);
        })
        .catch((error) => console.log(error));

      axios
        .get(`${baseUrl()}/worker_card/`, { headers })
        .then((response) => {
          this.workerList = response.data;
          this.worker = this.workerList[0];
          console.log(this.workerList);
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
    getResume() {
      this.resumeId = this.$route.params.resume_id;
      this.resume = this.resumeList[this.resumeId - 1];
      console.log(this.resume);
      this.worker = this.workerList[0];
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
.resume_wrapp {
  width: 100%;
}
.page-header {
  display: flex;
  height: 700px;
  flex-direction: column;
  background: url("~/assets/img/bg-banner2.jpg") no-repeat top center;
  background-size: cover;
  align-items: center;
  justify-content: center;
}
.container {
  justify-content: center;
  max-width: 100%;
  margin-top: 100px;
  display: flex;
}
.header-detail {
  width: 80%;
  background-color: white;
  &__head {
    display: flex;
    padding-top: 10px;
    &_main {
      display: flex;
      justify-content: space-between;
      width: 75%;
      &-time {
        margin-right: 10px;
        display: flex;
        align-items: center;
      }
      &-descr {
        display: flex;
        padding: 10px;
      }
      &-params {
        display: flex;
        li {
          width: 30%;
        }
      }
    }
  }
}
.button-group {
  display: flex;
  padding: 20px;
  justify-content: space-between;
}
.logo {
  display: flex;
  padding: 0 10px;
  align-items: center;
  max-width: 300px;
  img {
    width: 240px;
  }
}
.resume-info {
  display: flex;
  justify-content: center;
  &__container {
    display: flex;
    flex-direction: column;
    padding: 50px;
    max-width: 90%;
  }
}
</style>
