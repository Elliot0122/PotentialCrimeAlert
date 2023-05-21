import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import VueGoogleMaps from 'vue-google-maps-community-fork'
import { setupCalendar, Calendar} from 'v-calendar';
import 'v-calendar/style.css';
import VueDatepickerUi from 'vue-datepicker-ui';
import 'vue-datepicker-ui/lib/vuedatepickerui.css';

loadFonts()

createApp(App)
  .use(vuetify)
  .use(setupCalendar, {})
  .component('VCalendar', Calendar)
  .component('Datepicker', VueDatepickerUi)
  .use(VueGoogleMaps, {
    load: {
      key: 'AIzaSyDImDc1pPOI2VTYG8Pb0xPedM8TuYHvI8A',
    },
  })
  .mount('#app')
