<template>
    <li class="back-btn"><a href="index.html"><img class="img-fluid" src="@/assets/images/logo/logo-icon.png" alt=""></a>
        <div class="mobile-back text-end"><span>Back</span><i class="fa fa-angle-right ps-2" aria-hidden="true"></i></div>
    </li>
    <li class="pin-title sidebar-main-title">
        <div>
            <h6>Pinned</h6>
        </div>
    </li>
    <li v-for="(menuItem, index) in menu" :key="index" class="sidebar-list"
        :class="{ ' sidebar-main-title': menuItem.type == 'headtitle' }">
        <div v-if="menuItem.type == 'headtitle'">
            <h6 class="lan-1">{{ $t(menuItem.headTitle1) }}</h6>
        </div>
        <i v-if="menuItem.type != 'headtitle'" class="fa fa-thumb-tack"></i>
        <router-link :to="menuItem.path" class="sidebar-link sidebar-title"
            :class="menuItem.title == store.perentName ? 'active' : ''" v-if="menuItem.type == 'link'"
            @click="store.subMenuToggle(menuItem.title)">
            <svg class=" stroke-icon">
                <use :xlink:href="require('@/assets/svg/icon-sprite.svg') + `#${menuItem.icon1}`"></use>
            </svg>
            <svg class="fill-icon">
                <use :xlink:href="require('@/assets/svg/icon-sprite.svg') + `#${menuItem.icon2}`"></use>
            </svg>
            <span>
                {{ $t(menuItem.title) }}
            </span>
        </router-link>
        <a :href="menuItem.path" class="sidebar-link sidebar-title"
            :class="menuItem.title == store.perentName ? 'active' : ''" v-if="menuItem.type == 'redirect'"
            @click="store.subMenuToggle(menuItem.title)">
            <svg class=" stroke-icon">
                <use :xlink:href="require('@/assets/svg/icon-sprite.svg') + `#${menuItem.icon1}`"></use>
            </svg>
            <svg class="fill-icon">
                <use :xlink:href="require('@/assets/svg/icon-sprite.svg') + `#${menuItem.icon2}`"></use>
            </svg>
            <span>
                {{ $t(menuItem.title) }}
            </span>
        </a>
    </li>
</template>
<script lang="ts" setup>
import { ref, onMounted, computed } from 'vue';
import { useMenuStore } from "@/store/menu";
import { useRoute } from 'vue-router'

let menuItems = ref();
let route = useRoute()
let store = useMenuStore();
let menu = store.data
</script>