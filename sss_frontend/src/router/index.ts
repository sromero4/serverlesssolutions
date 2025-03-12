import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import BodyView from "@/layout/BodyView.vue"
import indexDashboard from "@/pages/ecommerce/indexProductList.vue"

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: BodyView,
    meta: {
      title: 'Default | Mofi - Premium Admin Template',
    },
    children: [
      {
        path: '',
        name: 'defaultRoot',
        component: indexDashboard,
        meta: {
          title: 'Default | Mofi - Premium Admin Template',
        }
      }
    ]
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
router.beforeEach((to,) => {
  if (typeof (to.meta.title) === 'string') {
    document.title = to.meta.title;
  }

});

export default router
