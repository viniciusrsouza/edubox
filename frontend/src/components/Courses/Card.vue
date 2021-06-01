<template>
  <v-card elevation="8" class="course-card-container">
    <div class="options">
      <v-btn
        icon
        :class="'btn ' + (favorite ? 'btn-star-clicked' : '')"
        @click="onClickStar"
      >
        <v-icon>{{ favorite ? "mdi-star" : "mdi-star-outline" }}</v-icon>
      </v-btn>
      <v-btn icon class="btn"> <v-icon>mdi-dots-horizontal</v-icon></v-btn>
    </div>
    <div class="header">
      <div class="title">
        <v-img
          height="48px"
          width="48px"
          contain
          src="@/assets/undraw/undraw_female_avatar_w3jk.svg"
        />
        <div class="title-text">{{ course.title }}</div>
      </div>
      <div class="description">{{ course.description }}</div>
    </div>
    <div class="assignments">
      <div class="assignments-title">{{ t("assignments") }}:</div>
      <Assignment
        v-for="assignment in assignments"
        :key="assignment.id"
        :assignment="assignment"
      />
    </div>
    <div class="footer">
      <<<<<<< HEAD
      <v-btn class="btn" @click="redirect(course.id)" text>{{
        t("see_more")
      }}</v-btn>
      =======
      <v-btn @click="redirect()" class="btn" text>{{ t("see_more") }}</v-btn>
      >>>>>>> adf16022d09a2caa8127385b35d9500e7a6eac41
      <Students :students="[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]" />
    </div>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import Assignment from "./Assignment.vue";
import Students from "./Students.vue";
import t from "../../locale";
export default Vue.extend({
  name: "Card",
  methods: {
    t,
    onClickStar: function () {
      this.favorite = !this.favorite;
    },
    redirect(id: number) {
      this.$router.push(`course/${id}`);
    },
  },
  components: { Assignment, Students },
  props: {
    course: {
      type: Object as () => Course,
    },
  },
  data: function () {
    return {
      assignments: [
        { id: 0, title: "RNN Project - VA1", due_date: "March 14, 2021" },
        {
          id: 1,
          title: "Intelligent Agents Essay",
          due_date: "March 24, 2021",
        },
      ],
      favorite: this.$props.course.favorite,
    };
  },
});

interface Course {
  id: number;
  title: string;
  description: string;
  favorite: boolean;
}
</script>

<style lang="scss" scoped>
.course-card-container {
  padding: 0 1em;

  .options {
    display: flex;
    justify-content: flex-end;
    margin-bottom: -1.2em;

    .btn {
      color: $hint;
    }

    .btn-star-clicked {
      color: $star;
    }
  }

  .title {
    display: inline-flex;
    padding: 0.5em 0;
    align-items: center;
  }

  .title-text {
    color: $text-primary;
    font-weight: bold;
    font-size: 1.2rem;
    padding: 0 0.8em;
  }

  .description {
    color: $text-secondary;
    font-size: 0.8rem;
    padding: 0 0.5em;
    height: 10em;
  }

  .assignments {
    .assignments-title {
      font-size: 0.8rem;
      text-transform: capitalize;
      margin-bottom: 0.5em;
    }
  }

  .footer {
    display: flex;
    justify-content: space-between;
    padding: 0.5em 0;

    .btn {
      color: $primary;
      padding: 1em;
    }
  }
}
</style>
