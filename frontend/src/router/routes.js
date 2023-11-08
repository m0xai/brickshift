
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { name: "home", path: '', component: () => import('pages/IndexPage.vue') }
    ]
  },
  {
    name: "login",
    path: "/login",
    component: () => import("pages/LoginPage.vue")
  },
  {
    name: "user-management",
    path: "/user-management",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/UserManagement.vue")}
    ]
  },
  {
    name: "profile",
    path: "/profile",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {path: "", component: () => import("pages/ProfilePage.vue")}
    ]
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
