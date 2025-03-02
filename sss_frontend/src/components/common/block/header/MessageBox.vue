<template>
    <div class="notification-box">
        <svg>
            <use href="@/assets/svg/icon-sprite.svg#header-message"></use>
        </svg><span class="badge rounded-pill badge-info">3 </span>
    </div>
    <div class="onhover-show-div notification-dropdown">
        <h5 class="f-18 f-w-600 mb-0 dropdown-title">Messages </h5>
        <ul class="messages">
            <li class="d-flex  gap-2" :class="item.class" v-for="(item, index) in messages" :key="index">
                <div class="flex-shrink-0"><img :src="getImages(item.img)" alt="Graph"></div>
                <div class="flex-grow-1"> <a href="private-chat.html">
                        <h6 class="font-primary f-w-600">{{ item.name }}</h6>
                    </a>
                    <p>{{ item.msg }}</p>
                </div><span>{{ item.time }}</span>
            </li>
            <li><a class="f-w-700" href="email-application.html">Check all</a></li>
        </ul>
    </div>
</template>
<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { messages } from "@/core/data/header"
import { getImages } from "@/composables/common/getImages"

</script>