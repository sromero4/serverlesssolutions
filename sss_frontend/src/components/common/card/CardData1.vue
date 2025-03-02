<template>
    <div :class="colClass">
        <div class="card" :class="cardClass">
            <div class="card-header" :class="cardhaderClass">
                <h4 :class="titleClass">{{ title }}</h4>

            </div>
            <div class="card-body" :class="cardbodyClass">
                <slot />
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
let props = defineProps({
    title: String,
    cardClass: String,
    colClass: String,
    cardbodyClass: String,
    cardhaderClass: String,
    titleClass: String,

})
</script>