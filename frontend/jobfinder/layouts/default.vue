<template>
  <div>
    <Header />

    <div class="container">
      <nuxt />
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  components: {Header, Footer}

}
</script>
<style lang="scss">
.container {
  width: 100%;
}

</style>
