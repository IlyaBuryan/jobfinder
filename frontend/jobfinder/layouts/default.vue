<template>
  <div>
    <Header />

    <Footer />

    <div class="container">
      <nuxt />
    </div>

  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Header.vue'

export default {
  components: {Header, Footer}

}
</script>
