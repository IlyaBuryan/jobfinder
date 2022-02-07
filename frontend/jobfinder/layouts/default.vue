<template>
  <div>
    <Header />

    <div class="main-container">
      <nuxt />
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: { Header, Footer },
};
</script>

<style scoped lang="scss">
.main-container {
  max-width: 100%;
  display: flex;
}
</style>
