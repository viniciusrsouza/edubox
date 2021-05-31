<template>
  <div class="ma-12 pa-12">
    <v-card width="256" class="mx-auto">
      <v-navigation-drawer permanent>
        <v-list>
          <v-list-item class="px-2">
            <v-list-item-avatar>
              <v-img
                src="@/assets/undraw/undraw_female_avatar_w3jk.svg"
              ></v-img>
            </v-list-item-avatar>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title> Linear Algebra </v-list-item-title>
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
              <v-icon>mdi-newspaper-variant-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Feed</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-format-list-bulleted</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Activities</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-account-multiple</v-icon>
            </v-list-item-icon>
            <v-list-item-title>People</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-divider></v-divider>
      <v-list nav dense>
        <v-list-item>
          <v-list-item-content >
            <v-list-item-title> Courses </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "SideBar",
});
</script>>

<style>
</style>