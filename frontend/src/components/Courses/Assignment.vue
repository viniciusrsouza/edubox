<template>
  <div class="assignment-container">
    <div class="marker" />
    <div class="content">
      <div class="a-title">{{ assignment.title }}</div>
      <div class="a-due-date">{{ assignment.due_date }}</div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import t from "../../locale";
export default Vue.extend({
  name: "Assignment",
  methods: { t },
  props: {
    assignment: {
      type: Object as () => Assignment,
    },
  },
});

interface Assignment {
  id: number;
  title: string;
  due_date: string;
}
</script>

<style lang="scss" scoped>
.assignment-container {
  display: flex;
  align-items: center;
  gap: 0.5em;
  box-shadow: none;

  &:hover {
    background: #fcfcfc;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.1), 0 2px 5px 0 rgba(0, 0, 0, 0.08);
  }

  .marker {
    height: 0.5em;
    width: 0.5em;
    border-radius: 100%;
    background: $primary;
  }

  .content {
    .a-title {
      padding: 0;
      margin: 0;
      font-size: 1rem;
      font-weight: 500;
      color: $text-primary;
    }

    .a-due-date {
      font-size: 0.8rem;
      color: $text-secondary;
    }
  }
}
</style>
