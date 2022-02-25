<template>
  <div class="form-group">
    <label for="message">Сопроводительное письмо</label>
      <textarea
        type="text"
        id="message"
        placeholder="Напишите письмо"
        class="form-control"
      />
      <button class="btn btn-success btn-xl">Отправить</button>
  </div>
</template>

<style scoped>
.form-group {
  width:500px;

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
