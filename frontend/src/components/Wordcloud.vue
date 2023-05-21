<template>
    <vue-word-cloud
    style="
        height: 92%;
        width: 100%;
    "
    :words="words"
    :color="([, weight]) => weight > 5 ? 'DeepPink' : weight > 2 ? 'RoyalBlue' : 'Indigo'"
    font-family="impact"
    enter-animation = "true"
    spacing = "0.25"
    rotation-unit = "rad"
    font-size-ratio = 5
    weight = "0.5"
    />
</template>

<script>
import VueWordCloud from 'vuewordcloud';
import wordcloudJson from '../../../backend/data/wordcloud.json'

export default {
  components: {
    [VueWordCloud.name]: VueWordCloud,
  },

  data(){
    return{
      words: []
    }
  },
  mounted(){
    for (var i = 0; i < wordcloudJson.length; i++){
      var data = []
      data.push(wordcloudJson[i].category)
      data.push(wordcloudJson[i].frequency)
      this.words.push(data)
    }
  }
};


</script>