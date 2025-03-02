<template>
    <span class="header-search">
        <svg>
            <use href="@/assets/svg/icon-sprite.svg#search"></use>
        </svg></span>
</template>
<script lang="ts" setup>
import { ref } from 'vue'
let filtered = ref<boolean>(false);

function collapseFilter() {
    filtered.value = !filtered.value;
}
</script>