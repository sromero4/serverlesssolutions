<template>
    <div class="cart-box">
        <svg>
            <use href="@/assets/svg/icon-sprite.svg#stroke-ecommerce"></use>
        </svg>
    </div>
    <div class="cart-dropdown onhover-show-div">
        <h5 class="f-18 f-w-600 mb-0 dropdown-title">Cart</h5>
        <ul>
            <li v-for="(item, index) in cart" :key="index">
                <div class="d-flex"><img class="img-fluid b-r-5 me-3 img-60" :src='getImages(item.img)' alt="">
                    <div class="flex-grow-1"><span class="f-w-600">{{
                        item.title
                    }}</span>
                        <div class="qty-box">
                            <div class="input-group"><span class="input-group-prepend">
                                    <button class="btn quantity-left-minus" type="button" data-type="minus" data-field=""
                                        v-on:click="decrement()">-</button></span>
                                <input class="form-control input-number" type="text" name="quantity" v-model="count"><span
                                    class="input-group-prepend">
                                    <button class="btn quantity-rig t-plus" type="button" data-type="plus" data-field=""
                                        v-on:click="increment()">+</button></span>
                            </div>
                        </div>
                        <h6 class="font-primary">${{ item.price }}</h6>
                    </div>
                    <div class="close-circle"><a class="bg-danger"><vue-feather type="x"></vue-feather></a></div>
                </div>
            </li>
            <li class="total">
                <h6 class="mb-0">Order Total : <span class="f-w-600 f-right">$1000.00</span></h6>
            </li>
            <li class="text-center"><a class="d-block mb-3 view-cart f-w-700" href="cart.html">Go to your cart</a><a
                    class="btn btn-primary view-checkout" href="checkout.html">Checkout</a></li>
        </ul>
    </div>
</template>
<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { cart } from "@/core/data/header"
import { getImages } from "@/composables/common/getImages"
let count = ref<number>(1)
function decrement() {
    count.value--
}
function increment() {
    count.value++
}
</script>