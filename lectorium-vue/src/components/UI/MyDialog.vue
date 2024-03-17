<template>
  <div class="dialog" v-if="show" @click.stop="hideDialog">
    <div @click.stop class="dialog__content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import toggleMixin from "@/mixins/toggleMixin";

export default {
  name: "MyDialog",
  mixins: [toggleMixin],
  methods: {
    hideDialog() {
      this.$emit("close"); // Вызываем событие при закрытии диалога
    },
  },
};
</script>

<style>

.dialog {
  z-index: 999;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  display: flex;
}
.dialog__content {
  z-index: 999;
  margin: auto;
  background: white;
  border-radius: 12px;
  padding: 15px;
  border: 2px solid black;
}
</style>
