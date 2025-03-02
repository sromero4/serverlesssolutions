<template>
    <div>
        <SidebarLoge />
        <nav class="sidebar-main">
            <div id="sidebar-menu">
                <ul class="sidebar-links custom-scrollbar" id="simple-bar">
                    <NavMenu />
                </ul>
            </div>
        </nav>
    </div>
</template>
<script lang="ts" setup>
import { defineAsyncComponent, defineEmits } from 'vue'
const SidebarLoge = defineAsyncComponent(() => import("@/components/common/block/sidebar/SidebarLoge.vue"))
const NavMenu = defineAsyncComponent(() => import("@/components/common/block/sidebar/NavMenu.vue"))
let emit = defineEmits(['clicked']);
</script>