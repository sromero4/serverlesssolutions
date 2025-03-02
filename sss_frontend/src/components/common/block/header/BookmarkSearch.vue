<template>
    <svg>
        <use href="@/assets/svg/icon-sprite.svg#header-bookmark"></use>
    </svg>
    <div class="onhover-show-div bookmark-flip">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="front">
                    <h5 class="f-18 f-w-600 mb-0 dropdown-title">Bookmark</h5>
                    <ul class="bookmark-dropdown">
                        <li>
                            <div class="row">
                                <div class="col-4 text-center" v-for="(item, index) in bookmark" :key="index">
                                    <div class="bookmark-content">
                                        <div class="bookmark-icon " :class="item.class"><vue-feather :class="item.class"
                                                :type="item.icon"></vue-feather></div><span :class="item.font">{{ item.title
                                                }}</span>
                                    </div>
                                </div>
                            </div>
                        </li>
                        <li><a class="f-w-700 d-block flip-back" id="flip-back" href="javascript:void(0)"
                                @click="openBookmark">Back</a></li>
                    </ul>
                </div>
                <div class="back">
                    <ul>
                        <li>
                            <div class="bookmark-dropdown flip-back-content">
                                <input type="text" placeholder="search...">
                            </div>
                        </li>
                        <li><a class="f-w-700 d-block flip-back" id="flip-back" href="javascript:void(0)">Back</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { bookmarks } from "@/core/data/header"
let bookmark = ref();
let bookmarkSearchBox = ref<boolean>(false)
function openBookmark() {
    bookmarkSearchBox.value = !bookmarkSearchBox.value;

}
onMounted(() => {
    try {
        bookmark.value = bookmarks;
    } catch (error) {
        console.error('Error fetching user data:', error);
    }
})
</script>