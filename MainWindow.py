from datetime import datetime
import requests
import json
import webbrowser
import pyproj
from pyproj import Transformer
from datetime import datetime , timedelta
import matplotlib.pyplot as plt


carparkAvailUrl = "https://api.data.gov.sg/v1/transport/carpark-availability?"

# Obtains JSON output from a link
def getOutput(x):
    r = requests.get(x)
    return json.loads(r.content)

# Obtain JSON output containing carpark availability entries
def getAllCarparkAvail():
    carparkAvailJson = getOutput(carparkAvailUrl)
    carpark_data = carparkAvailJson['items']
    listOfCarparkData = carpark_data[0]['carpark_data']
    return listOfCarparkData

# Get Carpark Availability entries, corresponding to the filtered Carpark Information
def getCarparkAvail(listOfCarparkData,carparkNo):
    carparkInfo = None
    for carpark in listOfCarparkData:
        cpno = carpark['carpark_number']
        if cpno == carparkNo:
            carparkInfo = carpark['carpark_info']
    return carparkInfo

# Converts the SYV1 coordinates from the table into longitude and latitude for a Google Map result
def openlink(y1, x1):
    xfm = pyproj.Transformer.from_crs('EPSG:3414', 'EPSG:4326', always_xy=True)
    yCoord, xCoord = xfm.transform(x1, y1)
    webbrowser.open('https://www.google.com/maps/search/' + str(xCoord) + ',' + str(yCoord))

# Obtains list of timestamps to use for obtaining past data
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

# Gets past carpark availability information
def getCarparkAvailAtTime(listOfTime,carparkNo):
    availList = []
    for date in listOfTime:
        avail_lots = 0
        url = carparkAvailUrl + "date_time=" + date
        result = getOutput(url)
        carpark_data = result['items']
        listOfCarparkData = carpark_data[0]['carpark_data']
        for carparks in listOfCarparkData:
            if carparks["carpark_number"] == carparkNo:
                avail_lots = int(carparks["carpark_info"][0]["lots_available"])
                availList.append(avail_lots)

    return availList

# Plots graph using past carpark availability information
def plotGraph(title,xlabel,ylabel,xvalue,yvalue):
    plt.plot(xvalue, yvalue)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
