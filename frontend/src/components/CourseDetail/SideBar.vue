<template>
  <div class="ma-12 pa-12">
    <v-card width="256" class="mx-auto">
      <v-navigation-drawer permanent>
        <v-list>
          <v-list-item class="px-2" two-line>
            <v-list-item-avatar>
              <v-img
                src="@/assets/undraw/undraw_female_avatar_w3jk.svg"
              ></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title class="text-color-blue">
                Linear Algebra
              </v-list-item-title>
              <v-list-item-subtitle>
                Prof. Rosanne Wiseman
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider></v-divider>
        <v-list nav dense>
          <v-list-item link>
            <v-list-item-icon>
              <v-icon class="text-color-blue"
                >mdi-newspaper-variant-outline</v-icon
              >
            </v-list-item-icon>
            <v-list-item-title class="text-color-blue">Feed</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-icon>
              <v-icon class="text-color-blue">mdi-format-list-bulleted</v-icon>
            </v-list-item-icon>
            <v-list-item-title class="text-color-blue"
              >Activities</v-list-item-title
            >
          </v-list-item>
          <v-list-item link>
            <v-list-item-icon>
              <v-icon class="text-color-blue">mdi-account-multiple</v-icon>
            </v-list-item-icon>
            <v-list-item-title class="text-color-blue"
              >People</v-list-item-title
            >
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-divider></v-divider>
      <v-list nav dense>
        <v-list-item>
          <v-list-item-content class="align-text-center text-color-blue">
            <v-list-item-title>
              Courses <v-icon x-small>mdi-open-in-new</v-icon>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-icon>
            <v-icon class="text-color-blue">mdi-plus-circle-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-title class="text-color-blue"
            >Join new course</v-list-item-title
          >
        </v-list-item>
        <DisciplineListItem v-for="course in courses" :key="course.id" :course="course"/>
      </v-list>
    </v-card>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import DisciplineListItem from "./DisciplineListItem.vue";
export default Vue.extend({
  name: "SideBar",
  components: {
    DisciplineListItem,
  },
  data: () => ({
    courses: [
      {
        id: 1,
        title: "Artificial Intelligence",
        professor: "Prof. Harold",
        picture: "https://randomuser.me/api/portraits/men/33.jpg",
      },
      {
        id: 2,
        title: "Calculus II",
        professor: "Prof. Mary Jones",
        picture: "https://randomuser.me/api/portraits/women/60.jpg",
      },
      {
        id: 3,
        title: "Computer Graphics",
        professor: "Prof. Christine Silas",
        picture: "https://randomuser.me/api/portraits/women/0.jpg",
      },
    ],
  }),
});
</script>>

<style lang="scss" scoped>
.align-text-center {
  text-align: center;
}
.text-color-blue {
  color: #3b5c78;
}
</style>