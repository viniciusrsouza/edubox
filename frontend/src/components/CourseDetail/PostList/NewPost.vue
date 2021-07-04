<template>
  <v-container fluid>
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          block
          prepend-inner-icon="mdi-pencil-outline"
          v-bind="attrs"
          v-on="on"
        >
          <v-icon>mdi-pencil-outline</v-icon>
          {{ $t("CoursePage.Feed.WriteNewPost") }}</v-btn
        >
        <!-- <v-textarea
          clearable
          auto-grow
          rows="1"
          clear-icon="mdi-close-circle"
          :label="$t('CoursePage.Feed.WriteNewPost')"
          prepend-inner-icon="mdi-pencil-outline"
          value=""
          v-bind="attrs"
          v-on="on"
        ></v-textarea> -->
      </template>

      <v-card>
        <v-card-title>
          {{ $t("CoursePage.Feed.WriteNewPost") }}
        </v-card-title>

        <div>
          <v-container fluid fill-height>
            <v-row no-gutters style="height: 100%">
              <v-col cols="12">
                <v-form>
                  <v-text-field label="Title" v-model="title"></v-text-field>
                  <v-checkbox
                    v-model="isAssignment"
                    :label="`Is this an assignment?`"
                  ></v-checkbox>
                  <v-menu
                    v-if="isAssignment"
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="false"
                    :return-value="date"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="date"
                        label="Due date"
                        prepend-inner-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="date" no-title scrollable>
                      <v-spacer></v-spacer>
                      <v-btn text color="primary" @click="menu = false">
                        Cancel
                      </v-btn>
                      <v-btn
                        text
                        color="primary"
                        @click="$refs.menu.save(date)"
                      >
                        OK
                      </v-btn>
                    </v-date-picker>
                  </v-menu>
                  <v-textarea
                    label="What are your thoughts?"
                    auto-grow
                    v-model="description"
                  ></v-textarea>
                </v-form>
              </v-col>
            </v-row>
          </v-container>
        </div>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            v-if="!isAssignment"
            elevation="2"
            x-large
            color="#3B5C78"
            style="width: 20%"
            class="white--text"
            @click="createPost"
            :loading="loading"
            >Create</v-btn
          >
          <v-btn
            v-if="isAssignment"
            elevation="2"
            x-large
            color="#3B5C78"
            style="width: 20%"
            class="white--text"
            @click="createPost"
            :loading="loading"
            >Create</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { mapState } from "vuex";
import UserService from "../../../services/user_service";
export default Vue.extend({
  async mounted() {
    try {
      let user = await UserService.fetchUser();
      this.userId = user.id;
    } catch (error) {
      console.log("error: ", error);
    }
  },

  computed: {
    ...mapState("course", ["course"]),
  },
  methods: {
    createPost() {
      if (!this.isAssignment) {
        // eslint-disable-next-line no-undef
        const payload: models.Post = {
          id: 0,
          author: this.userId,
          course: this.course.id,
          title: this.title,
          text: this.description,
        };

        this.$services.post.create(payload).then(() => {
          //clearing fields
          this.date = new Date(
            Date.now() - new Date().getTimezoneOffset() * 60000
          )
            .toISOString()
            .substr(0, 10);
          this.title = "";
          this.description = "";

          //closes dialog
          this.dialog = false;
        });
      }
      else{
        // eslint-disable-next-line no-undef
        const payload ={
          id: 0,
          author: this.userId,
          course: this.course.id,
          title: this.title,
          text: this.description,
          is_assignment: true,
          deadline: new Date(this.date).toISOString(),
        };

        this.$services.post.create(payload).then(() => {
          //clearing fields
          this.date = new Date(
            Date.now() - new Date().getTimezoneOffset() * 60000
          )
            .toISOString()
            .substr(0, 10);
          this.title = "";
          this.description = "";

          //closes dialog
          this.dialog = false;
        });
      }
    },
    createAssignment() {
      // eslint-disable-next-line no-undef
      const payload: models.Assignment = {
        id: 0,
        title: this.title,
        course: this.course.id,
        description: this.description,
        deadline: new Date(this.date).toISOString(),
      };

      console.log(new Date(this.date).toISOString());
      this.$services.assignment.create(payload).then(() => {
        //clearing fields
        this.date = new Date(
          Date.now() - new Date().getTimezoneOffset() * 60000
        )
          .toISOString()
          .substr(0, 10);
        this.title = "";
        this.description = "";

        //closes dialog
        this.dialog = false;
      });
    },
  },
  data() {
    return {
      userId: 0,
      isAssignment: false,
      dialog: false,
      title: "",
      description: "",
      date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      menu: false,
      modal: false,
      loading: false,
    };
  },
});
</script>
<style></style>
