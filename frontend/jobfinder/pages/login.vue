<template>
  <body class="login-page">
    <main>
      <div class="login-block">
        <img class="logo-form" src="/_nuxt/assets/img/logo.png" alt="" />
        <h1>Авторизация</h1>

        <form action="#">
          <div class="form-group">
            <div class="input-group">
              <span class="input-group-addon"><i class="ti-email"></i></span>
              <input type="text" class="form-control" placeholder="Email" />
            </div>
          </div>

          <hr class="hr-xs" />

          <div class="form-group">
            <div class="input-group">
              <span class="input-group-addon"><i class="ti-unlock"></i></span>
              <input
                type="password"
                class="form-control"
                placeholder="Password"
              />
            </div>
          </div>

          <button class="btn btn-primary btn-block" type="submit">
            Авторизоваться
          </button>

          <div class="login-footer">
            <h6>или залогиниться через</h6>
            <ul class="social-icons">
              <li>
                <a class="facebook" href="#"><i class="fa fa-facebook"></i></a>
              </li>
              <li>
                <a class="twitter" href="#"><i class="fa fa-twitter"></i></a>
              </li>
              <li>
                <a class="linkedin" href="#"><i class="fa fa-linkedin"></i></a>
              </li>
            </ul>
          </div>
        </form>
      </div>
    </main>
  </body>
</template>

<script>
export default {
  layout: "login_reg",
};
</script>

<style lang="scss">
.logo-form {
  width: 360px;
}
h1 {
  display: block;
  font-size: 2em;
  margin-block-start: 0.67em;
  margin-block-end: 0.67em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  font-weight: bold;
}
.login-page {
  background-color: #e5e7ed;
}
.login-block {
  background-color: #fff;
  padding: 60px;
  box-shadow: 0 3px 50px 0 rgba(0, 0, 0, 0.1);
  text-align: center;
  border-radius: 5px;
  position: absolute;
  top: 50%;
  left: 50%;
  margin: -240px -285px;
}
.login-block .form-group {
  margin-top: 15px;
  margin-bottom: 15px;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group-addon {
  width: auto;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.login-block .hr-xs {
  margin-top: 5px;
  margin-bottom: 5px;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.login-footer {
  margin-top: 60px;
  opacity: 0.5;
  transition: opacity 0.3s ease-in-out;
}
.login-footer:hover {
  opacity: 1;
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
.social-icons {
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}
.social-icons li {
  display: inline-block;
  margin-bottom: 4px;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-linkedin:before {
  content: "\f0e1";
}
a,
a:focus,
a:hover {
  color: #29aafe;
  text-decoration: none;
  transition: color 0.3s linear;
  outline: 0;
}
a {
  color: #337ab7;
  text-decoration: none;
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
ol,
ul {
  line-height: 28px;
}
.login-links {
  padding: 15px 5px 0;
  font-size: 13px;
  color: #96a2b2;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
</style>
