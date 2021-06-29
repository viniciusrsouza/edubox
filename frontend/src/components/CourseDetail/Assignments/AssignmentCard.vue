<template>
  <v-expansion-panel class="a-container">
    <v-expansion-panel-header class="a-header">
      <v-icon class="a-icon" size="32">mdi-file-document-outline</v-icon>
      <div>
        <h2 class="a-title">Neural Networks Essay</h2>
        <span class="a-publish-date">published at 12:28, June 20th</span>
      </div>
      <span class="a-due-date">due July 7th</span>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      <div class="a-content">
        <div class="a-description">
          <p>
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Distinctio
            dicta temporibus dolorem a et tempora excepturi vel mollitia aut
            deserunt sapiente in consequatur amet accusamus natus earum, minus,
            esse fuga blanditiis voluptatibus aperiam, suscipit numquam!
            Consequatur, laborum ab exercitationem similique dolore obcaecati
            molestiae maiores quas?
            <br />
            <br />
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Consequuntur veniam sequi, minus facilis et magni, mollitia ipsum
            quo, saepe possimus maxime. Minus, numquam corrupti quia sit animi,
            dolor quae qui ut debitis doloremque deleniti. Ad!
            <br />
            <br />
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Atque
            nesciunt voluptatum repudiandae sequi? Rem, dolorum velit mollitia
            labore aut cumque iste accusamus autem reiciendis earum!
          </p>
        </div>
        <div class="a-submissions">
          <v-btn>
            <v-icon>mdi-add</v-icon>
          </v-btn>
          <div class="a-list">
            <v-chip class="ma-2 a-submission" close color="primary" outlined>
              <v-icon left> mdi-file-check-outline </v-icon>
              file-name.pdf
            </v-chip>
            <v-chip class="ma-2 a-submission" close color="primary" outlined>
              <v-icon left> mdi-file-check-outline </v-icon>
              file-name.pdf
            </v-chip>
            <v-chip class="ma-2 a-submission" close color="primary" outlined>
              <v-icon left> mdi-file-check-outline </v-icon>
              file-name.pdf
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
//           {{ assignment.description }}
//         </div>
//       </v-col>

//       <v-col class="margin-10" cols="5">
//         <h3 class="main-color">Due date: {{ assignment.due_date }}</h3>
//         <div class="rounded-corner main-color">
//           <v-file-input
//             class="file-select"
//             show-size
//             counter
//             label="Attach Assignment"
//             v-model="file"
//           ></v-file-input>
//           <!-- <h5 class="attach-file">
//             <v-icon class="main-color" x-large> mdi-paperclip </v-icon>
//             Attach Assignment
//           </h5> -->
//         </div>
//         <v-btn @click="submit" block color="primary" class="submit-button">
//           Submit
//         </v-btn>
//       </v-col>
//     </v-row>
//   </v-card>
