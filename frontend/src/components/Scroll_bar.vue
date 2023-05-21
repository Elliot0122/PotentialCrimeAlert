<template>
    <p>Showing {{ isEven ? 'even' : 'odd' }} items</p>
    <button @click="toggle">Toggle Even/Odd</button>
    <div v-bind="containerProps" class="scroll-container">
      <div v-bind="wrapperProps">
        <div v-for="item in list" :key="item.index" class="scroll-item">
          Row: {{ item.data }}
        </div>
      </div>
    </div>
  </template>
  
  <style>
  .scroll-container {
    height: 26vh;
    overflow: auto;
    overflow-y: hidden;
  }
  
  .scroll-item {
    height: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  </style>
  
  <script>
  import { useVirtualList } from '@vueuse/core'
  import { computed, ref } from 'vue'
  
  export default {
    setup() {
      const isEven = ref(false)
      const toggle = () => {
        isEven.value = !isEven.value
      }
  
      const allItems = Array.from(Array(99999).keys())
      const filteredList = computed(() =>
        allItems.filter(i => (isEven.value ? i % 2 === 0 : i % 2 === 1))
      )
  
      const { list, containerProps, wrapperProps } = useVirtualList(filteredList, {
        itemHeight: 22,
      })
  
      return { isEven, toggle, list, containerProps, wrapperProps }
    },
  }
  </script>
  