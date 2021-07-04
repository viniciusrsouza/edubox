<template>
  <v-dialog v-model="dialog" width="500">
    <v-card>
      <v-card-title>
        {{ $t("CoursePage.Assignments.NewAssignment") }}
      </v-card-title>

      <div>
        <v-container fluid fill-height>
          <v-row no-gutters style="height: 100%">
            <v-col cols="12">
              <v-form>
                <v-text-field label="Name" solo v-model="title"></v-text-field>
                <v-menu
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
                      prepend-icon="mdi-calendar"
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
                    <v-btn text color="primary" @click="$refs.menu.save(date)">
                      OK
                    </v-btn>
                  </v-date-picker>
                </v-menu>
                <v-textarea
                  label="Assignment Description"
                  solo
                  height="300"
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
          elevation="2"
          x-large
          color="#3B5C78"
          style="width: 20%"
          class="white--text"
          @click="create"
          :loading="loading"
          >Create</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  methods: {
    create() {
      // eslint-disable-next-line no-undef
      const payload: models.Assignment = {
        id: 0,
        title: this.title,
        description: this.description,
        deadline: this.date,
      };

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
