import requests
import json

# non-library ways to retrieve data values

def carparkNo(x):
    return output["items"][0]["carpark_data"][x]["carpark_number"]


def lotNo(x):
    return output["items"][0]["carpark_data"][x]["carpark_info"][0]["total_lots"]


def lotType(x):
    return output["items"][0]["carpark_data"][x]["carpark_info"][0]["lot_type"]


def lotAvail(x):
    return output["items"][0]["carpark_data"][x]["carpark_info"][0]["lots_available"]


def upTime(x):
    return output["items"][0]["carpark_data"][x]["carpark_info"][0]["lots_available"]

# gets output from API call
def getOutput(x):
    r = requests.get(x)
    return json.loads(r.content)


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



