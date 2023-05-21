import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import VueGoogleMaps from 'vue-google-maps-community-fork'

loadFonts()

createApp(App)
  .use(vuetify)
  .use(VueGoogleMaps, {
    load: {
      key: 'AIzaSyDImDc1pPOI2VTYG8Pb0xPedM8TuYHvI8A',
    },
  })
  .mount('#app')