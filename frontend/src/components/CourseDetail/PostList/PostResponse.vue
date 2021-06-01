<template>
  <div class="row-wrapper">
    <v-row class="mb-6 no-margin-bottom distance-top">
      <v-col cols="1" class="margin">
        <v-icon>mdi-thumb-up-outline</v-icon>
      </v-col>
      <v-col cols="10">
        <p>{{ response.content }}</p>
      </v-col>
    </v-row>
    <v-list-item>
        <v-list-item-avatar>
            <v-img src="@/assets/undraw/undraw_female_avatar_w3jk.svg"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
            <v-list-item-title>
                by {{response.created_by}}
            </v-list-item-title>
        </v-list-item-content>
    </v-list-item>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "PostResponse",
  props: {
    response: {
      type: Object as () => PostResponse,
    },
  },
});

interface PostResponse {
  id: number;
  content: string;
  created_by: string;
  created_at: string;
}
</script>

<style scoped>
.margin{
    margin-left: 10px;
}

.distance-top {
    margin-top: 25px;
}

.no-margin-bottom{
    margin-bottom: 0px !important;
}

.border-left {
  border-left: 3px solid gray;
}

.height-limit {
  height: 50%;
}
.row-wrapper {
  margin-left: 35px;
  border-left: 3px solid #CBCBCB;
  margin-bottom: 25px;
  display: inline-block;
}
</style>