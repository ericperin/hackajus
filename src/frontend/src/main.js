import Vue from 'vue';
import App from './App.vue';
import VueSweetalert2 from 'vue-sweetalert2';
import InputMask from 'jquery-mask-plugin';
window.$ = require('jquery');

import 'sweetalert2/dist/sweetalert2.min.css';

Vue.use(VueSweetalert2);
Vue.use(InputMask);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app')
