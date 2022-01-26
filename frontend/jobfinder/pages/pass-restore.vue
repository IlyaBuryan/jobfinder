<template>
  <body>
    <div class="overlay">
      <form>
        <div class="con">
          <img class="logo-form" src="/_nuxt/assets/img/logo.png" alt="" />
          <header class="head-form">
            <h2>Сбросить пароль</h2>
          </header>
          <br />
          <div class="field-set">
            <span class="input-item">
              <i class="fa fa-user-circle"></i>
            </span>

            <input
              class="form-input"
              id="txt-input"
              type="text"
              placeholder="Email"
              required
            />
            <br />
            <span class="input-item">
              <i class="fa fa-key"></i>
            </span>

            <input
              class="form-input"
              type="password"
              placeholder="Password"
              id="pwd"
              name="password"
              required
            />

            <span>
              <i
                class="fa fa-eye"
                aria-hidden="true"
                type="button"
                id="eye"
              ></i>
            </span>

            <br />

            <button class="log-in">Авторизация</button>
          </div>

          <div class="other">
            <button class="btn submits frgt-pass">Забыли пароль</button>

            <button class="btn submits sign-up">
              Зарегистрироваться
              <i class="fa fa-user-plus" aria-hidden="true"></i>
            </button>
          </div>
        </div>
      </form>
    </div>
  </body>
</template>  

<script>
export default {
  layout: "login_auth",
};
</script>

<style lang="css">
.logo-form {
  width: 360px;
}
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
/* End Global rules */

/* Start body rules */
body {
  /* background-image: linear-gradient(-225deg, #e3fdf5 0%, #ffe6fa 100%);
  background-image: linear-gradient(to top, #a8edea 0%, #fed6e3 100%); */
  background-attachment: fixed;
  background-repeat: no-repeat;

  font-family: "Vibur", cursive;
  /*   the main font */
  font-family: "Abel", sans-serif;
  opacity: 0.95;
  /* background-image: linear-gradient(to top, #d9afd9 0%, #97d9e1 100%); */
}
form {
  width: 450px;
  min-height: 500px;
  height: auto;
  border-radius: 5px;
  margin: 2% auto;
  box-shadow: 0 9px 50px hsla(20, 67%, 75%, 0.31);
  padding: 2%;
  background-image: linear-gradient(-225deg, #e3fdf5 50%, #ffe6fa 50%);
}
form .con {
  display: -webkit-flex;
  display: flex;

  -webkit-justify-content: space-around;
  justify-content: space-around;

  -webkit-flex-wrap: wrap;
  flex-wrap: wrap;

  margin: 0 auto;
}

/* the header form form */
header {
  margin: 2% auto 10% auto;
  text-align: center;
}
/* Login title form form */
header h2 {
  font-size: 22px;
  font-family: Gill Sans, sans-serif;
  color: #3e403f;
}
/*  A welcome message or an explanation of the login form */
header p {
  letter-spacing: 0.05em;
}
.input-item {
  background: #fff;
  color: #333;
  padding: 14.5px 0px 15px 9px;
  border-radius: 5px 0px 0px 5px;
}
#eye {
  background: #fff;
  color: #333;

  margin: 5.9px 0 0 0;
  margin-left: -20px;
  padding: 15px 9px 19px 0px;
  border-radius: 0px 5px 5px 0px;

  float: right;
  position: relative;
  right: 1%;
  top: -0.2%;
  z-index: 5;
  cursor: pointer;
}
/* inputs form  */
input[class="form-input"] {
  width: 240px;
  height: 50px;

  margin-top: 2%;
  padding: 15px;

  font-size: 16px;
  font-family: "Abel", sans-serif;
  color: #5e6472;

  outline: none;
  border: none;

  border-radius: 0px 5px 5px 0px;
  transition: 0.2s linear;
}
input[id="txt-input"] {
  width: 250px;
}
/* focus  */
input:focus {
  transform: translateX(-2px);
  border-radius: 5px;
}

button {
  display: inline-block;
  color: #252537;

  width: 280px;
  height: 50px;

  padding: 0 20px;
  background: #fff;
  border-radius: 5px;

  outline: none;
  border: none;

  cursor: pointer;
  text-align: center;
  transition: all 0.2s linear;

  margin: 7% auto;
  letter-spacing: 0.05em;
}
/* Submits */
.submits {
  width: 48%;
  display: inline-block;
  float: left;
  margin-left: 2%;
}
.frgt-pass {
  background: transparent;
}

.sign-up {
  background: #b8f2e6;
}

/* buttons hover */
button:hover {
  transform: translatey(3px);
  box-shadow: none;
}

/* buttons hover Animation */
button:hover {
  animation: ani9 0.4s ease-in-out infinite alternate;
}
@keyframes ani9 {
  0% {
    transform: translateY(3px);
  }
  100% {
    transform: translateY(5px);
  }
}
</style>