from datetime import datetime
import requests
import json
import onemapsg
from onemapsg import OneMapClient
from scipy import spatial
import webbrowser
from pyproj import Transformer

resource_id = "139a3035-e624-4f56-b63f-89ae28d4ae4c"

def getOutput(x):
    r = requests.get(x)
    return json.loads(r.content)

def getAllCarparkAvail():
    carparkAvail = "https://api.data.gov.sg/v1/transport/carpark-availability"
    carparkAvailJson = getOutput(carparkAvail)
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
    carparkinfo = "https://data.gov.sg/api/action/datastore_search?resource_id=" + resource_id + "&q=" + LocationName
    carparkInfoJson = getOutput(carparkinfo)
    xylist = []
    for carpark in carparkInfoJson['result']['records']:
        xytuple = ((carpark['x_coord']),carpark['y_coord'])
        xylist.append(xytuple)
    return xylist

# find a list of carpark in area
def findNearestArea(LocationName):
    carparkinfo = "https://data.gov.sg/api/action/datastore_search?resource_id=" + resource_id + "&q=" + LocationName
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

def openlink(x1, y1):
    yCoord, xCoord = convertXYToLatLong(x1, y1)
    webbrowser.open('https://www.google.com/maps/search/' + str(yCoord) + ',' + str(xCoord))

# Converts the x & y coordinates to longitude & latitude to be used for google map search
def convertXYToLatLong(x1, y1):
    transformer = Transformer.from_crs('epsg:3414', 'epsg:4757', always_xy=True)
    return transformer.transform(x1, y1)