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
        v-for="(m, index) in markers"
        :position="m.position"
        :clickable="true"
        :draggable="true"
        @click="center = m.position"
      />
    </GMapCluster>
  </GMapMap>
</template>

<script>
import crimeJson from '../../../backend/CrimeDate.json'

export default {
  data() {
    return {
      center: { lat: 38.5509409, lng: -121.7358303 },
      markers: [],
    };
  },
  mounted(){
    for (var i = 0; i < crimeJson.length; i++){
      let position = {
        lat: crimeJson[i].lat,
        lng: crimeJson[i].lng
      }
      this.markers.push(position)
    }
  }
};
</script>

<style>
body {
  margin: 0;
}
</style>
