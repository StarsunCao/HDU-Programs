import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Layout from '@/layout'


export const constantRoutes = [{
        path: '/login',
        component: () =>
            import ('@/views/login/index'),
        hidden: true
    },

    {
        path: '/404',
        component: () =>
            import ('@/views/404'),
        hidden: true
    },


    {
        path: '/material',
        component: Layout,
        children: [{
            path: 'material',
            name: 'search',
            component: () =>
                import ('@/views/material/search'),
            meta: {
                title: 'search',
            }
        }, ]
    },
    {
        path: "/detail",
        component: Layout,
        name: "detail",
        component: () =>
            import ("@/views/material/detail"),
    },
    {
        path: '/editInfo',
        component: Layout,

        name: 'edit',
        component: () =>
            import ('@/views//material/editInfo'),


    },

    {
        path: '/',
        component: Layout,
        children: [{
            path: 'add',
            name: 'add',
            component: () =>
                import ('@/views//material/newInfo'),
            meta: {
                title: 'add apartment',
            }
        }]
    },
    {
        path: '/admin',
        component: Layout,
        children: [{
            path: 'admin',
            name: 'admin',
            component: () =>
                import ('@/views/material/admin'),
            meta: {
                title: 'admin',
            }
        }, ]
    },
    {
        path: '*',
        redirect: '/404',
        hidden: true
    }
]

const createRouter = () => new Router({
    scrollBehavior: () => ({
        y: 0
    }),
    routes: constantRoutes
})

const router = createRouter()

export function resetRouter() {
    const newRouter = createRouter()
    router.matcher = newRouter.matcher
}

export default router