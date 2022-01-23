<template>
  <li>
    <NuxtLink :to="job[2]">{{ job[1] }}</NuxtLink>
  </li>
</template>

<script>
export default {
  props: {
    job: {
      type: Array,
    },
  },
};
</script>