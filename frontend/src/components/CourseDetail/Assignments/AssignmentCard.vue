<template>
  <v-expansion-panel class="a-container">
    <v-expansion-panel-header class="a-header">
      <v-icon class="a-icon" size="32">mdi-file-document-outline</v-icon>
      <div>
        <h2 class="a-title">{{ assignment.title }}</h2>
        <span class="a-publish-date">
          {{ $t_f("CoursePage.Assignments.PublishDate", assignment) }}
        </span>
      </div>
      <span class="a-due-date">due July 7th</span>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      <div class="a-content">
        <div class="a-description">
          {{ assignment.description }}
        </div>
        <div class="a-submissions">
          <input
            ref="file_picker"
            class="d-none"
            type="file"
            @change="onGetFile"
          />
          <v-btn @click="getFile">
            <v-icon>mdi-plus</v-icon>
            {{ t("CoursePage.Assignments.NewAssignment") }}
          </v-btn>
          <div class="a-list">
            <v-chip
              v-if="file"
              class="mx-2 a-submission"
              close
              color="primary"
              outlined
              @click:close="file = null"
            >
              <v-icon left> mdi-file-check-outline </v-icon>
              {{ file.name }}
            </v-chip>
          </div>
        </div>
      </div>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../../locale";

export default Vue.extend({
  data() {
    return {
      file: null,
      loading: false,
    };
  },

  props: {
    assignment: {
      type: Object as () => Assignment,
    },
  },
  methods: {
    t,
    getFile() {
      this.loading = true;
      window.addEventListener(
        "focus",
        () => {
          this.loading = false;
        },
        { once: true }
      );

      const fp: any = this.$refs.file_picker;
      fp?.click?.();
    },
    onGetFile(e: any) {
      this.file = e.target.files[0];
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
.a-header {
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  gap: 1em;
  align-items: center;

  .a-title,
  .a-icon {
    color: $primary;
  }

  .a-publish-date {
    color: $text-secondary;
    font-size: 0.8rem;
  }

  .a-due-date {
    color: $text-primary;
    font-weight: 600;
  }
}

.a-content {
  display: grid;
  grid-template-columns: auto 300px;
  gap: 4em;
  padding-top: 1em;
}

.a-description {
  text-align: justify;
  text-justify: inter-word;
}

.a-submissions {
  display: inline-flex;
  flex-direction: column;
  align-items: flex-end;

  .a-list {
    padding-top: 1em;
    display: inline-flex;
    flex-direction: column;
    gap: 0.5em;
  }
}

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

//
<v-card>
//     <v-row class="mb-6">
//       <v-col class="margin-10" cols="6">
//         <div>
//           <h3 class="main-color">
//             <v-icon class="main-color" x-large>
//               mdi-file-document-outline </v-icon
//             >{{ assignment.title }}
//           </h3>
//         </div>
//         <div class="subtitle">
//           Activity posted at {{ assignment.posted_date }}
//         </div>
//         <div class="small-font">
  //         {{ assignment.description }}
  //       </div>
  //     </v-col>

  //     <v-col class="margin-10" cols="5">
  //       <h3 class="main-color">Due date: {{ assignment.due_date }}</h3>
  //       <div class="rounded-corner main-color">
  //         <v-file-input
  //           class="file-select"
  //           show-size
  //           counter
  //           label="Attach Assignment"
  //           v-model="file"
  //         ></v-file-input>
  //       </div>
  //       <v-btn @click="submit" block color="primary" class="submit-button">
  //         Submit
  //       </v-btn>
  //     </v-col>
  //   </v-row>
  // </v-card>
