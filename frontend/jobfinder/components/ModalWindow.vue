<template>
  <div>
    <div class="modal">
      <div>
        <!-- Fields -->

        <div class="form-group">
          <label for="organizationComp">Организация</label>
          <input
            type="text"
            id="organizationComp"
            placeholder="Организация"
            class="form-control"
            v-model="experience.organization"
          />
        </div>

        <div class="form-group">
          <label for="startComp">Начало работы</label>
          <input
            type="date"
            id="startComp"
            placeholder="Начало работы"
            class="form-control"
            v-model="experience.start"
          />
        </div>

        <div class="form-group">
          <label for="endComp">Окончание работы</label>
          <input
            type="date"
            id="endComp"
            placeholder="Окончание работы"
            class="form-control"
            v-model="experience.end"
          />
        </div>

        <div class="form-group">
          <label for="positionComp">Должность</label>
          <input
            type="text"
            id="positionComp"
            placeholder="Должность"
            class="form-control"
            v-model="experience.position"
          />
        </div>
        <div class="form-group">
          <label for="functionsComp">Обязанности</label>
          <textarea
            id="infoComp"
            placeholder="Обязанности"
            class="form-control"
            v-model="experience.functions"
            rows="4"
          />
        </div>

        <!-- Submit -->
        <button
          type="button"
          class="btn btn-success btn-block buttons"
          @click="sendExperience"
        >
          Сохраните опыт
        </button>
        <!-- END Submit -->
      </div>

      <button @click="$emit('change-modal')" class="btn btn-primary buttons">
        Закрыть окно создания опыта
      </button>
    </div>
  </div>
</template>
 
<script>
export default {
  name: "ModalWindow",
  data: () => ({
    experience: {
      organization: "",
      start: "",
      end: "",
      position: "",
      functions: "",
      resume: [],
    },
  }),
  methods: {
    sendExperience() {
      if (this.experience.organization !== "") {
        this.$emit("add-experience", this.experience);
        this.experience = {};
      }
    },
  },
};
</script>
 
<style scoped>
.modal {
  background: #ffffff;
  box-shadow: 20px 20px 20px 10px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
  padding: 50px;
}

.buttons {
  margin: 20px 0 0 0;
}
</style>