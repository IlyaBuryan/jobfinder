<template>
  <NuxtLink :to="job.link">{{ job.text }}</NuxtLink>
</template>

<script>
export default {
  props: {
    job: {
      type: Object,
    },
  },
};
</script>