<template>
  <div class="student-container">
    <div class="student student-1">
      <v-img src="@/assets/undraw/undraw_male_avatar_323b.svg" />
    </div>
    <div class="student student-2">
      <v-img src="@/assets/undraw/undraw_profile_pic_ic5t.svg" />
    </div>
    <div class="student student-3">
      <v-img src="@/assets/undraw/undraw_female_avatar_w3jk.svg" />
    </div>
    <div class="student student-rest">
      {{ loaded_students ? loaded_students.rest : "" }}
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "Students",
  props: {
    students: {
      type: Array,
    },
  },
  data: () => ({
    loaded_students: {
      first: null,
      second: null,
      third: null,
      rest: null,
    } as Students,
  }),
  methods: {
    getStudents: function (): Students {
      return {
        first: this.$props.students[0] !== null ? "URL" : null,
        second: this.$props.students[1] !== null ? "URL" : null,
        third: this.$props.students[2] !== null ? "URL" : null,
        rest:
          this.$props.students[3] !== null
            ? this.$props.students.length - 3
            : null,
      };
    },
  },
  beforeMount: function () {
    this.loaded_students = this.getStudents();
  },
});

type Students = {
  first: string | null;
  second: string | null;
  third: string | null;
  rest: number | null;
};
</script>

<style lang="scss" scoped>
.student-container {
  display: inline-flex;
  flex-direction: row;
  padding: 0 0.3em;
}

.student {
  background: white;
  height: 32px;
  width: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 100%;
  border: 2px solid white;
  margin: 0 -0.3em;
  color: white;
}

.student-1 {
  z-index: 0;
}

.student-2 {
  z-index: 1;
}

.student-3 {
  z-index: 2;
}

.student-rest {
  background: $primary;
  z-index: 3;
  user-select: none;
}
</style>
