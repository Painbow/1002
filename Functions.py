from datetime import datetime
import requests
import json
import onemapsg
from onemapsg import OneMapClient
from scipy import spatial
import webbrowser
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

#return x, y cordinates
def searching(LocationName):
    password = 'JDiRbZav7UvDhz4'
    email = 'rashidarul@protonmail.com'
    #authentication info
    #need sign up
    client = OneMapClient(email,password)

    #returns a dictionary
    apisearchresult = client.search(LocationName)

    #could be prone to error in location search
    #returns a dictionary inside a list inside above dictionary
    resultdictionary = apisearchresult['results'][0]

    #get x,y cordinates of search result
    xcord = resultdictionary['X']
    ycord = resultdictionary['Y']
    return xcord, ycord

#nearest cords searching
#KDtree query can return a certain number of neighbour
# add k variable in query to increase output of query.
def nearestCords(x, y):
    arealist = coordinatesTupleOnly(LocationName)
    tree = spatial.KDTree(arealist)
    result = tree.query([(x, y)]) #k=5?
    return arealist[result[1][0]]


# process data to prepare for searching
def coordinatesTupleOnly(LocationName):
    carparkinfo = carparkInfoUrl + resource_id + "&q=" + LocationName
    carparkInfoJson = getOutput(carparkinfo)
    xylist = []
    for carpark in carparkInfoJson['result']['records']:
        xytuple = ((carpark['x_coord']),carpark['y_coord'])
        xylist.append(xytuple)
    return xylist

# find a list of carpark in area
def findNearestArea(LocationName):
    carparkinfo = carparkInfoUrl + resource_id + "&q=" + LocationName
    carparkInfoJson = getOutput(carparkinfo)
    xylist = []
    for carpark in carparkInfoJson['result']['records']:
        xydic = {'car_park_no': carpark['car_park_no'],
                 'x_coord': carpark['x_coord'],
                'y_coord': carpark['y_coord']
                 }
        xylist.append(xydic)
    return xylist

#match carpark code back to area to find specific carpark
def matchingCarparkCode(x,y, LocationName):
    carparks = findNearestArea(LocationName)
    code = ''
    for carpark in carparks:
        if (carpark['x_coord'] == x) and (carpark['y_coord'] == y):
            code = carpark['car_park_no']
    return code

def openlink(y1, x1):

    # yCoord, xCoord = 103.8846673,1.3213042
    yCoord, xCoord = convertXYToLatLong(y1, x1)
    webbrowser.open('https://www.google.com/maps/search/' + str(xCoord) + ',' + str(yCoord))

# Converts the x & y coordinates to longitude & latitude to be used for google map search
def convertXYToLatLong(y1, x1):
    transformer = Transformer.from_crs('epsg:3414', 'epsg:4757', always_xy=True)
    return transformer.transform(y1, x1)


def getPastDays(totalDays):
    days = []
    now = datetime.now()
    for i in range(0,totalDays):
        date = now.date()
        time = now.time()
        nowDay = date.day
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
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()