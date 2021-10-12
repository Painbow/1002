from datetime import datetime
import testFunctions
import json

def getUserInput():
    msg = "********************************\n"
    msg += "1. Display all carpark\n"
    msg += "2. Display by area\n"
    msg += "3. Display by carpark type\n"
    msg += "4. Display free parking\n"
    msg += "********************************"
    print(msg)
    displayType = input("Filter carpark by?: ")
    return displayType

def getCarparkType():
    msg = "********************************\n"
    msg += "1. Multi-Storey Car Park\n"
    msg += "2. Surface Car Park\n"
    msg += "********************************"
    print (msg)
    carparkType = input("Which type of carpark do you want to see?")
    if carparkType == '1':
        return "MULTI-STOREY CAR PARK"
    elif carparkType == '2':
        return "SURFACE CAR PARK"
    else:
        print("invalid input, try again")
        return getCarparkType()

def getAllCarparkAvail():
    carparkAvail = "https://api.data.gov.sg/v1/transport/carpark-availability"
    carparkAvailJson = testFunctions.getOutput(carparkAvail)
    carpark_data = carparkAvailJson['items']
    listOfCarparkData = carpark_data[0]['carpark_data']
    return listOfCarparkData

def getCarparkAvail(listOfCarparkData,carparkNo):
    carparkInfo = None
    for carpark in listOfCarparkData:
        cpno = carpark['carpark_number']
        if cpno == carparkNo:
            carparkInfo = carpark['carpark_info']
    return carparkInfo

def getCurrentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time