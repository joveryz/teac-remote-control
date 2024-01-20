import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import Notifications from '@kyvg/vue3-notification'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'

library.add(fas, fab, far)

const app = createApp(App)

app.use(createPinia())
app.use(Notifications)

app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
