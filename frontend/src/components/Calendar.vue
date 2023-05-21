<template>
    <div >
        <VCalendar expanded :attributes='attrs'/>
        <div class="Picker">
            <Datepicker
                range
                v-model="selectedDate"
                lang="en"
            />
            <div class = "Button">
                <button @click="warn(selectedDate, $event)">
                    Submit
                </button>
            </div>
            
        </div>
    </div>
    
</template>

<script >

import { render } from "vue3-word-cloud";
import eventJson from "../../../backend/data/date.json"

export default{
    data(){
        return{
            attrs:[
            {
                dot: true,
                dates:[
                ]
            },
        ],
        selectedDate: [
        new Date(),
        new Date(new Date().getTime() + 9 * 24 * 60 * 60 * 1000)],
    }
    },

    
    mounted(){
        for(var i=0; i<eventJson.length;i++){
            var temp = new Date(eventJson[i].year, (eventJson[i].month)-1, eventJson[i].date)
            this.attrs[0].dates.push(temp)
        }
    },

    methods: {
        warn(message, event) {
            // now we have access to the native event
            if (event) {
            event.preventDefault()
            }
            // alert(message)
            // console.log(message[0].getMonth()+1,message[0].getDate(),message[0].getFullYear()) 
            // // console.log(message)
            var yearStart = message[0].getFullYear()
            var monthStart = message[0].getMonth()+1
            var dayStart = message[0].getDate()
            var yearEnd = message[1].getFullYear()
            var monthEnd = message[1].getMonth()+1
            var dayEnd = message[1].getDate()
            var newURL = "http://127.0.0.1:3000/api?yearStart=" + yearStart + "&monthStart=" + monthStart + "&dayStart=" + dayStart + "&yearEnd=" + yearEnd + "&monthEnd=" + monthEnd + "&dayEnd=" + dayEnd
            window.location.href = newURL;
        }
    }
};



</script>



<style>
/* :root{
    --v-calendar-input-font-size: 5rem;
} */
.vc-container .vc-weekday-1, .vc-container .vc-weekday-7 {
  color: #6366f1;
}
/* .v-calendar .input-field input{
    font-size: large;
} */

.Picker{
    
    /* margin: auto;
    width: 50%;
    padding: 10px; */
    display: flex;
    justify-content: left;
    align-items: left;
    margin-left: 50px;
    margin-top: 50px;
} 

.Button{
    margin-left: 30px;
    margin-top: 15px;
    font-size:larger;
}




</style>
  
