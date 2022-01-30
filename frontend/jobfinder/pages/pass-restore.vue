<template>
  <body class="login-page">
    <main>
      <div class="login-block">
        <img class="logo-form" src="/_nuxt/assets/img/logo.png" alt="" />
        <h1>Сбросить пароль</h1>

        <form action="#">
          <div class="form-group">
            <div class="input-group">
              <span class="input-group-addon"><i class="ti-email"></i></span>
              <input type="text" class="form-control" placeholder="Email" />
            </div>
          </div>

          <button class="btn btn-primary btn-block" type="submit">
            Запрос ссылки для сброса пароля
          </button>
        </form>
      </div>

      <div class="login-links">
        <p class="text-center">
          <nuxt-link to="/login">Авторизация</nuxt-link>
        </p>
      </div>
    </main>
  </body>
</template>  

<script>
export default {
  layout: "login_reg",
};
</script>

<style scoped lang="scss">
.login-page main {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  width: 100%;
  max-width: 460px;
}
.logo-form {
  width: 360px;
}
.login-block {
  background-color: #fff;
  padding: 60px;
  box-shadow: 0 3px 50px 0 rgb(0 0 0 / 10%);
  text-align: center;
  border-radius: 5px;
}
*,
:after,
:before {
  box-sizing: border-box;
}
.login-block h1 {
  font-family: Open Sans, sans-serif;
  font-size: 22px;
  color: #96a2b2;
  margin-bottom: 60px;
  margin-top: 40px;
}
.login-links {
  padding: 15px 5px 0;
  font-size: 13px;
  color: #96a2b2;
}
.text-center {
  text-align: center;
}
.btn-primary {
  background-color: #29aafe;
  border-color: #29aafe !important;
}
.btn {
  height: 44px;
  line-height: 44px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-radius: 3px;
  padding: 0 30px;
  color: #fff;
  transition: 0.2s linear;
}
.login-block .form-control {
  background-color: transparent;
  border: none;
}
.login-block .input-group-addon {
  color: #29aafe;
  font-size: 19px;
  opacity: 0.5;
  background-color: transparent;
  border: none;
  padding: 6px 12px;
}
[class*=" ti-"],
[class^="ti-"] {
  font-family: themify;
  font-style: normal;
}
.ti-email:before {
  content: "\2709";
}
</style>