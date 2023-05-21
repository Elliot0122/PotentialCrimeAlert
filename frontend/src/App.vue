<script>
import Map from './components/Map.vue'
import Wordcloud from './components/Wordcloud.vue'

export default {
  name: 'App',

  components: {
    Map,
    Wordcloud
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
      <v-col no-gutters id="toolbox" style="height: 20vh; justify-content: center; align-items: center; display:grid; margin: 15px 15px 7.5px 5px; padding: 10px 10px 5px 10px">
        <toolbox />
      </v-col>
    </v-row>
    <v-row no-gutters id="lowerRow" style="height: 35vh; width: 100%;">
      <v-col no-gutters style="display:grid; margin: 10px 7.5px 15px 15px;"
        id="stockRecommendation">
        <Wordcloud/>
      </v-col>
      <v-col no-gutters id="wordcloud" style="height: 10vh; justify-content: center; align-items: center; margin: 10px 15px 15px 7.5px;">
        456
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
  overflow-y: hidden;
  overflow-x: hidden;
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