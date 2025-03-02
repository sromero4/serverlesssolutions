import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import 'bootstrap/dist/js/bootstrap.bundle'
import "bootstrap/dist/js/bootstrap.min.js";
import "./assets/scss/app.scss"

import VueFeather from "vue-feather";

import English from "@/core/locales/en.json"
import لعربية from "@/core/locales/ae.json"
import 简体中文 from "@/core/locales/cn.json"
import Português from "@/core/locales/pt.json"
import Français from "@/core/locales/fr.json"
import Deutsch from "@/core/locales/de.json"
import Español from "@/core/locales/es.json"

import { createI18n } from 'vue-i18n'
const i18n = createI18n({
    legacy: false,
    locale: '',
    messages: {
        English: English,
        Español: Español,
        Deutsch: Deutsch,
        Français: Français,
        Português: Português,
        简体中文: 简体中文,
        لعربية: لعربية,
    }
})

createApp(App)
    .use(router)
    .use(createPinia())
    .use(i18n)
    .component(VueFeather.name, VueFeather)
    .mount('#app')
