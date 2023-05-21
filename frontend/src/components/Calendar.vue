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
                    Change Date
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
                highlight: {
                    color: "purple",
                    fillMode: "light",
                },
                dates:[
                ]
            },
        ],
        selectedDate: [],
    }
    },

    
    mounted(){
        const url = new URL(window.location.href);
        var urlString = url.toString()
        console.log(this.selectedDate)
        if(urlString.includes("?")){
            var yearStart = url.searchParams.get('yearStart')
            var yearEnd = url.searchParams.get('yearEnd')
            var monthStart = url.searchParams.get('monthStart')-1
            var monthEnd = url.searchParams.get('monthEnd')-1
            var dayStart = url.searchParams.get('dayStart')
            var dayEnd = url.searchParams.get('dayEnd')
            console.log(monthStart)
            var startDate = new Date(yearStart, monthStart, dayStart)
            var endDate = new Date(yearEnd, monthEnd, dayEnd)
            this.selectedDate[0] = startDate
            this.selectedDate[1] = endDate
        }
        else{
            this.selectedDate[0] = Date()
            this.selectedDate[1] = new Date(new Date().getTime() + 9 * 24 * 60 * 60 * 1000)
        }
        console.log(this.selectedDate)
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
  
