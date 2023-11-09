
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { name: "home", path: '', component: () => import('pages/IndexPage.vue') }
    ]
  },
  {
    path: "/login",
    component: () => import("layouts/LoginLayout.vue"),
    children: [
      { name: "login", path: '', component: () => import('pages/LoginPage.vue') }
    ]
  },
  {
    path: "/user-management",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { name: "user-management", path: "", component: () => import("pages/UserManagement.vue")}
    ]
  },
  {
    path: "/profile",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {name: "profile", path: "", component: () => import("pages/ProfilePage.vue")}
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
