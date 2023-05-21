<template>
  <div class="container">
    <p class="showing-events">Showing recent events</p>
    <div v-bind="containerProps" class="scroll-container">
      <div v-bind="wrapperProps" class="list-dynamic">
        <div v-for="item in list" :key="item.index" class="list-item-dynamic">
          {{ item.data }}
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="less">
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10px;
}

.toggle-button {
  margin-bottom: 10px;
  padding: 8px 16px;
  font-size: 14px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.scroll-container {
  height: 25vh;
  // overflow: auto;
  // overflow-y: auto;
  // border: 1px solid #ccc;
  border-radius: 4px;
  width: 44vw; /* Increase the width value as desired */
  margin-top: 5px;
}
.showing-events {
  font-family: Arial, sans-serif;
  font-size: 20px;
  font-weight: bold;
  color: #606c76;
  font-family: "Roboto","Helvetica Neue","Helvetica","Arial";
}

.list-item-dynamic {
    // display: flex;
    align-items: center;
    padding: 1em;
    border-bottom: 1px solid;
    border-color: lightgray;
    font-weight: bold; /* Example: Change the font weight */
    color: #606c76; /* Example: Change the color */
    font-family: "Roboto","Helvetica Neue","Helvetica","Arial";
  }

.list-dynamic {
  width: 100%;
  height: 500px;
  // border: 2px solid;
  border-radius: 3px;
  // overflow-y: auto;
  border-color: #d3d3d3;
}
</style>

<script>
import { useVirtualList } from '@vueuse/core'
import EventJson from '../../../backend/data/EventDate.json'
export default {
  setup() {
    var allItems = []
    for (var i = 0 ; i < EventJson.length; i++){
      allItems.push(EventJson[i].title)
    }
    const { list, containerProps, wrapperProps } = useVirtualList(allItems, {
      itemHeight: 22,
    })

    return {list, containerProps, wrapperProps }
  },
}
</script>