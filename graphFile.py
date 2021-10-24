import Functions

timeStamps = Functions.getPastDays(5)
availTime = Functions.getCarparkAvailAtTime(timeStamps,"HE12")
Functions.plotGraph("Carpark Availability for the Past 5 days","Time","Carpark Avail",timeStamps,availTime)