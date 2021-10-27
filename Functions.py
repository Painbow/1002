from datetime import datetime
import requests
import json
import webbrowser
import pyproj
from pyproj import Transformer
from datetime import datetime , timedelta
import matplotlib.pyplot as plt

resource_id = "139a3035-e624-4f56-b63f-89ae28d4ae4c"
carparkAvailUrl = "https://api.data.gov.sg/v1/transport/carpark-availability?"
carparkInfoUrl = "https://data.gov.sg/api/action/datastore_search?resource_id="
def getOutput(x):
    r = requests.get(x)
    return json.loads(r.content)

def getAllCarparkAvail():
    carparkAvailJson = getOutput(carparkAvailUrl)
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

def openlink(y1, x1):

    # yCoord, xCoord = 103.8846673,1.3213042
    xfm = pyproj.Transformer.from_crs('EPSG:3414', 'EPSG:4326', always_xy=True)
    yCoord, xCoord = xfm.transform(x1, y1)
    webbrowser.open('https://www.google.com/maps/search/' + str(xCoord) + ',' + str(yCoord))

# Converts the x & y coordinates to longitude & latitude to be used for google map search
def convertXYToLatLong(y1, x1):
    transformer = Transformer.from_crs('epsg:3414', 'epsg:4326', always_xy=True)
    return transformer.transform(y1, x1)


def getPastDays(totalDays):
    days = []
    now = datetime.now()
    for i in range(0,totalDays):
        date = now.date()
        time = now.time()
        date = date - timedelta(days=i)
        newDate = str(date)+"T"+str(time)
        days.append(newDate)
    return days

def getCarparkAvailAtTime(listOfTime,carparkNo):
    availList = []
    for date in listOfTime:
        availLots = 0
        url = carparkAvailUrl + "date_time=" + date
        result = getOutput(url)
        carpark_data = result['items']
        listOfCarparkData = carpark_data[0]['carpark_data']
        for carparks in listOfCarparkData:
            if carparks["carpark_number"] == carparkNo:
                availLots = int(carparks["carpark_info"][0]["lots_available"])
                availList.append(availLots)

    return availList

def plotGraph(title,xlabel,ylabel,xvalue,yvalue):
    plt.plot(xvalue, yvalue)
    xlabel = xlabel.replace
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
