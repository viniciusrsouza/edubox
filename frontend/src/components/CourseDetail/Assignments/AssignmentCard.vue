<template>
  <v-expansion-panel class="a-container">
    <v-expansion-panel-header class="a-header">
      <v-icon class="a-icon" size="32">mdi-file-document-outline</v-icon>
      <div>
        <h2 class="a-title">{{ post.title }}</h2>
        <span class="a-publish-date">
          {{
            $t_f("CoursePage.Assignments.PublishDate", {
              created_at: pretty_date(post.created_at),
            })
          }}
        </span>
      </div>
      <span class="a-due-date"
        >due {{ pretty_date(post.assignment.deadline) }}</span
      >
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      <div class="a-content">
        <div class="a-description">
          {{ post.text }}
        </div>
        <div class="a-separator" />
        <div class="a-submissions">
          <input
            ref="file_picker"
            class="d-none"
            type="file"
            @change="onGetFile"
          />
          <div class="a-list">
            <div class="d-flex align-center">
              <h1 class="text-body-1 font-weight-medium">
                {{ $t("CoursePage.Assignments.Submission") }}
              </h1>
              <v-btn @click="getFile" icon color="primary" title="adasd">
                <v-icon>mdi-file-upload-outline</v-icon>
              </v-btn>
            </div>
            <v-chip
              v-if="file"
              class="mx-2 a-submission"
              close
              color="primary"
              outlined
              @click:close="file = null"
            >
              <v-icon left> mdi-file-check-outline </v-icon>
              {{ filename }}
            </v-chip>
          </div>
        </div>
      </div>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script lang="ts">
import { Post } from "@/models/models";
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
    post: {
      type: Object as () => Post,
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
    },
    pretty_date(date: string) {
      const d = new Date(date);
      const p_date = `${d.getUTCDate()}/${d.getUTCMonth()}/${d.getUTCFullYear()}`;
      return p_date;
    },
  },
  computed: {
    filename() {
      if (this.file) {
        const [name, extension] = this.file.name.split(".");
        return `${
          name.length > 8 ? `${name.slice(0, 8)}...` : `${name}.`
        }${extension}`;
      }
      return "";
    },
  },
});
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
  grid-template-columns: auto 1px 200px;
  gap: 2em;
  padding-top: 1em;
}

.a-separator {
  width: 100%;
  background: $hint;
}

.a-description {
  text-align: justify;
  text-justify: inter-word;
}

.a-submissions {
  display: inline-flex;
  flex-direction: column;
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
