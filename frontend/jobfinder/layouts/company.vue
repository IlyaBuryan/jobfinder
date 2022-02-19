<template>
  <div>
    <Header :userData="user" />
    <div class="main-container">
      <nuxt />
    </div>
    <Footer />
  </div>
</template>

<script>
import { baseUrl, decode } from "../store/constants.js";
import Cookies from "universal-cookie";
import axios from "axios";
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: { Header, Footer },
  data() {
    return {
      user: { username: "" },
    };
  },
  mounted() {
    this.getUser();
  },
  methods: {
    async getUser() {
      const cookies = new Cookies();
      let token = cookies.get("token");
      if (token !== "") {
        let userId = decode(token).user_id;
        let headers = this.get_headers(token);

        await axios
          .get(`${baseUrl()}/user/${userId}/`, { headers })
          .then((response) => {
            this.user = response.data;
            console.log(this.user);
            this.checkLink();
          })
          .catch((error) => console.log(error));
      }
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

<style scoped lang="scss">
.main-container {
  width: 100%;
  display: flex;
  justify-content: center;
}

.navbar {
  z-index: 11;
}
</style>
