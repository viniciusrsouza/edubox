<template>
  <v-card>
      <NewPost/>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue'
import NewPost from './NewPost.vue'
export default Vue.extend({
    components: {
        NewPost
    }
})
</script>

<style>

</style>