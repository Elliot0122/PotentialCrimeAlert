<template>
  <GMapMap
    :center="center"
    :zoom="13"
    map-type-id="terrain"
    style="width: 100vh; height: 60vh"
  >
    <GMapCluster :zoomOnClick="true">
      <GMapMarker
        :key="index"
        v-for="(m, index) in crimeMarkers"
        :position="m.position"
        :clickable="true"
        :draggable="true"
        @click="center = m.position"
      />
    </GMapCluster>
    <GMapCluster :zoomOnClick="true">
      <GMapMarker
        :key="index"
        :icon="'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'"
        v-for="(m, index) in eventMarkers"
        :position="m.position"
        :clickable="true"
        :draggable="true"
        @click="center = m.position"
      />
    </GMapCluster>
  </GMapMap>
</template>

<script>
import crimeJson from '../../../Backend/CrimeDate.json'
import eventJson from '../../../Backend/temp.json'

export default {
  data() {
    return {
      center: { lat: 38.5509409, lng: -121.7358303 },
      crimeMarkers: [],
      eventMarkers: [],
    };
  },
  mounted(){
    for(var i = 0; i < crimeJson.length; i++){
      var data = {
        position : {
          lat: crimeJson[i].lat,
          lng: crimeJson[i].lng
        }
      }
      this.crimeMarkers.push(data)
    }
    
    for(i = 0; i < eventJson.length; i++){
      data = {
        position : {
          lat: eventJson[i].lat,
          lng: eventJson[i].lng
        }
      }
      this.eventMarkers.push(data)
    }
  }
};
</script>

<style>
body {
  margin: 0;
}
</style>
