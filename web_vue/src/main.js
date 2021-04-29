import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import baseURL from '../public/command'
Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)


axios.defaults.baseURL=baseURL.axiosConfig.baseURL;
Vue.prototype.axios = axios
axios.interceptors.request.use(config => {
  config.url  = encodeURI(config.url)
  return config
});
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
