<template>
    <LogoView />
    <BreadCrumbs />
    <div class="header-wrapper col m-0">
        <div class="row">
            <SearchBar />
            <HeaderLogo />
            <div class="nav-right col-xxl-8 col-xl-6 col-md-7 col-8 pull-right right-header p-0 ms-auto">
                <ul class="nav-menus">
                    <li>
                        <SearchInput />
                    </li>
                    <li>
                        <HeaderSearch />
                    </li>
                    <li class="onhover-dropdown">
                        <NotificationBox />
                    </li>
                    <li class="onhover-dropdown">
                        <BookmarkSearch />
                    </li>
                    <li>
                        <ModeView />
                    </li>
                    <li class="language-nav">
                        <LanguageView />
                    </li>
                    <li class="onhover-dropdown">
                        <MessageBox />
                    </li>
                    <li class="cart-nav onhover-dropdown">
                        <CartBox />
                    </li>
                    <li class="profile-nav onhover-dropdown px-0 py-0">
                        <ProfileView />
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { defineAsyncComponent, defineEmits } from 'vue'
const LogoView = defineAsyncComponent(() => import("@/components/common/block/header/LogoView.vue"))
const SearchBar = defineAsyncComponent(() => import("@/components/common/block/header/SearchBar.vue"))
const HeaderLogo = defineAsyncComponent(() => import("@/components/common/block/header/HeaderLogo.vue"))
const SearchInput = defineAsyncComponent(() => import("@/components/common/block/header/SearchInput.vue"))
const HeaderSearch = defineAsyncComponent(() => import("@/components/common/block/header/HeaderSearch.vue"))
const NotificationBox = defineAsyncComponent(() => import("@/components/common/block/header/NotificationBox.vue"))
const BookmarkSearch = defineAsyncComponent(() => import("@/components/common/block/header/BookmarkSearch.vue"))
const ModeView = defineAsyncComponent(() => import("@/components/common/block/header/ModeView.vue"))
const MessageBox = defineAsyncComponent(() => import("@/components/common/block/header/MessageBox.vue"))
const CartBox = defineAsyncComponent(() => import("@/components/common/block/header/CartBox.vue"))
const ProfileView = defineAsyncComponent(() => import("@/components/common/block/header/ProfileView.vue"))
const LanguageView = defineAsyncComponent(() => import("@/components/common/block/header/LanguageView.vue"))
const BreadCrumbs = defineAsyncComponent(() => import("@/layout/BreadCrumbs.vue"))
let emit = defineEmits(['clicked']);
</script>