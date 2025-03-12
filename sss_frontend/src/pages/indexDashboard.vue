<template>
    <div class="container-fluid">
        <div class="row starter-main">
            <StarterMain />

        </div>
    </div>
</template>
<script lang="ts" setup>
import { defineAsyncComponent } from 'vue'
const StarterMain = defineAsyncComponent(() => import("@/components/theme/dashboard/StarterMain.vue"))

</script>