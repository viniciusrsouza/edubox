<template>
  <v-card>
    <v-row class="mb-6">
      <v-col class="margin-10" cols="6">
        <div>
          <h3 class="main-color">
            <v-icon class="main-color" x-large>
              mdi-file-document-outline </v-icon
            >{{ assignment.title }}
          </h3>
        </div>
        <div class="subtitle">
          Activity posted at {{ assignment.posted_date }}
        </div>
        <div class="small-font">
          {{ assignment.description }}
        </div>
      </v-col>

      <v-col class="margin-10" cols="5">
        <h3 class="main-color">Due date: {{ assignment.due_date }}</h3>
        <div class="rounded-corner main-color">
          <v-file-input
            class="file-select"
            show-size
            counter
            label="Attach Assignment"
            v-model="file"
          ></v-file-input>
        </div>
        <v-btn @click="submit" block color="primary" class="submit-button">
          Submit
        </v-btn>
      </v-col>
    </v-row>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../../locale";
export default Vue.extend({
  data() {
    return {
      file: null,
    };
  },

  props: {
    assignment: {
      type: Object as () => Assignment,
    },
  },
  methods: {
    t,
    submit() {
      console.log(this.file);
    },
  },
});

interface Assignment {
  id: number;
  title: string;
  posted_date: string;
  description: string;
  due_date: string;
}
</script>

<style lang="scss" scoped>
.submit-button {
  margin-top: 5px;
}

.main-color {
  color: $primary;
}

.margin-10 {
  margin-left: 10px;
}

.subtitle {
  color: rgba(0, 0, 0, 0.6);
}

.inherit {
  margin-left: inherit;
}

.rounded-corner {
  border-radius: 25px;
  border: 2px solid $primary;
  position: relative;
}

.attach-file {
  position: absolute;
  top: 30%;
  left: 30%;
}

.small-font {
  font-size: 80%;
}

.file-select {
  margin: auto;
  width: 70%;
}
</style>