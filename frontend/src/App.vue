<script>
import Map from './components/Map.vue'
import Calendar from './components/Calendar.vue'
import Wordcloud from './components/Wordcloud.vue'
import Scroll_bar from './components/Scroll_bar.vue'

export default {
  name: 'App',

  components: {
    Map,
    Calendar,
    Wordcloud,
    Scroll_bar
  },

  data: () => ({
    //
  }),
}
</script>

<template>
  <div id="container">
    <v-row no-gutters id="upperRow" style="height: 65vh; width: 100%;">
      <v-col no-gutters id="map"
        style="justify-content: center; align-items: center; display:grid; margin: 15px 5px 7.5px 15px; padding: 10px 10px 5px 10px">
        <Map />
      </v-col>
      <v-col no-gutters id="toolbox" style="height: 63vh; align-items: center; display:grid; margin: 15px 15px 7.5px 5px; padding: 30px 10px 5px 10px">
        <p style="font-size:60px; text-align: center; font-weight: bold;"> Calendar</p>
        <Calendar />
      </v-col>
    </v-row>
    <v-row no-gutters id="lowerRow" style="height: 35vh; width: 100%;">
      <v-col no-gutters style="display:grid; margin: 10px 7.5px 15px 15px;"
        id="stockRecommendation">
        <Wordcloud/>
      </v-col>
      <v-col no-gutters id="wordcloud" style="height: 32vh; justify-content: center; align-items: center; margin: 10px 15px 15px 7.5px;">
        <Scroll_bar />
      </v-col>
    </v-row>
  </div>
</template>

<style>
html,
body {
  width: 100%;
  height: 100%;
  min-width: 1300px;
  margin: 0;
  overflow-y: visible;
  overflow-x: visible;
  font: 15px -apple-system, BlinkMacSystemFont,
    Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell,
    Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: flex;
  background-color: #BDC0BA;
}

#map,
#news-display,
#stockRecommendation,
#wordcloud,
#toolbox {
  -webkit-border-radius: 15px;
  -moz-border-radius: 15px;
  border-radius: 15px;
  border: none;
  background-color: #FFF;
}

.map {
  grid-area: map;
}

.toolbox {
  grid-area: toolbox;
}

.News-Recommendation {
  grid-area: News-Recommendation;
}

.Wordcloud {
  grid-area: Wordcloud;
}
</style>
