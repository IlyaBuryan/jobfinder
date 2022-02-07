<template>
  <div>
    <!-- Site footer -->
    <footer class="site-footer">
      <!-- Top section -->
      <div class="container">
        <div class="row">
          <div class="col-sm-12 col-md-6">
            <h6>О нас</h6>
            <p class="text-justify">
              Мы создаем передовые технологии на всех доступных платформах для
              того, чтобы работодатели могли быстро найти подходящего
              сотрудника, а соискатели — хорошую работу.
            </p>
          </div>

          <div class="col-xs-6 col-md-3">
            <h6>Наша компания</h6>
            <ul class="footer-links">
              <div v-for="item in OurCompany" :key="item.id">
                <li><SingleLink :job="item" /></li>
              </div>
            </ul>
          </div>

          <div class="col-xs-6 col-md-3">
            <h6>Самые популярные вакансии</h6>
            <ul class="footer-links">
              <div v-for="item in topVacancies" :key="item.id">
                <li><SingleLink :job="item" /></li>
              </div>
            </ul>
          </div>
        </div>

        <hr />
      </div>
      <!-- END Top section -->

      <!-- Bottom section -->
      <div class="container">
        <div class="row">
          <div class="col-md-8 col-sm-6 col-xs-12">
            <p class="copyright-text">
              Copyrights &copy; {{ new Date().getFullYear() }} Все права защищены
              <a href="http://themeforest.net/user/shamsoft"
                >"Python's Style Group"</a
              >.
            </p>
          </div>

          <div class="col-md-4 col-sm-6 col-xs-12">
            <ul class="social-icons">
              <li>
                <a class="facebook" href="#">
                  <i class="fa fa-facebook"></i>
                </a>
              </li>
              <li>
                <a class="twitter" href="#">
                  <i class="fa fa-twitter"></i>
                </a>
              </li>
              <li>
                <a class="linkedin" href="#">
                  <i class="fa fa-linkedin"></i>
                </a>
              </li>
              <li>
                <a class="instagram" href="#">
                  <i class="fa fa-instagram"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <!-- END Bottom section -->
    </footer>
    <!-- END Site footer -->

    <!-- Back to top button -->
    <a id="scroll-up" href="#"><i class="ti-angle-up"></i></a>
    <!-- END Back to top button -->
  </div>
</template>

<script>
import SingleLink from "@/components/SingleLink.vue";
export default {
  components: { SingleLink },
  data: () => ({
    topVacancies: [
      { id: 1, text: "Фронт-энд девелопер", link: "/" },
      { id: 2, text: "Android девелопер", link: "/" },
      { id: 3, text: "iOS девелопер", link: "/" },
      { id: 4, text: "Full stack девелопер", link: "/" },
      { id: 5, text: "Руководитель проекта", link: "/" },
    ],
    OurCompany: [
      { id: 1, text: "О нас", link: "/" },
      { id: 2, text: "Как это работает", link: "/" },
      { id: 3, text: "FAQ", link: "/" },
      { id: 4, text: "Политика безопасности", link: "/" },
      { id: 5, text: "Наши контакты", link: "/" },
    ],
  }),
};
</script>

<style>
.text-justify {
  text-align: justify;
}
.site-footer {
  background-color: #26272b;
  padding: 45px 0 20px;
  font-size: 14px;
  line-height: 24px;
  color: #bbb;
}
.site-footer hr {
  border-top-color: #bbb;
  opacity: 0.1;
}
.site-footer hr.small {
  margin: 20px 0;
}
.site-footer h6 {
  color: #fff;
  font-size: 15px;
  text-transform: uppercase;
  margin-top: 0;
  letter-spacing: 2px;
}
.site-footer a {
  position: relative;
  color: #bbb;
}
.site-footer a:after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  height: 2px;
  bottom: -2px;
  border-bottom: 1px solid #bbb;
}
.site-footer a:hover {
  color: #fff;
}
.site-footer .social-icons {
  text-align: right;
}
.site-footer .social-icons a {
  width: 40px;
  height: 40px;
  line-height: 40px;
  margin-left: 6px;
  margin-right: 0;
  border-radius: 100%;
  background-color: #33353d;
}
.site-footer .social-icons a:after {
  display: none;
}
.copyright-text {
  margin: 0;
}
.social-icons {
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}
.social-icons li {
  display: inline-block;
  margin-bottom: 4px;
}
.social-icons li.title {
  margin-right: 15px;
  text-transform: uppercase;
  color: #96a2b2;
  font-weight: 700;
  font-size: 13px;
}
.social-icons a {
  background-color: #eceeef;
  color: #818a91;
  font-size: 16px;
  display: inline-block;
  line-height: 44px;
  width: 44px;
  height: 44px;
  text-align: center;
  margin-right: 8px;
  border-radius: 100%;
  transition: all 0.2s linear;
}
.social-icons a:active,
.social-icons a:focus,
.social-icons a:hover {
  color: #fff;
  background-color: #29aafe;
}
.social-icons.size-sm a {
  line-height: 34px;
  height: 34px;
  width: 34px;
  font-size: 14px;
}
.social-icons a.facebook:hover {
  background-color: #3b5998;
}
.social-icons a.twitter:hover {
  background-color: #00aced;
}
.social-icons a.linkedin:hover {
  background-color: #007bb6;
}
.social-icons a.instagram:hover {
  background-color: #517fa4;
}
.footer-links {
  padding-left: 0;
  list-style: none;
}
.footer-links li {
  display: block;
}
.footer-links a {
  color: #bbb;
}
.footer-links a:active,
.footer-links a:focus,
.footer-links a:hover {
  color: #fff;
}
.footer-links a:after {
  display: none;
}
.footer-links.inline li {
  display: inline-block;
}
</style>
