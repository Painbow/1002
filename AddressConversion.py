#  https://pypi.org/project/onemapsg/
#  letting user search for location and returning nearest
#  carpark base on x,y coordinates
from onemapsg import OneMapClient
import testFunctions
from scipy import spatial

#static data that is required
resource_id = "139a3035-e624-4f56-b63f-89ae28d4ae4c"
password = 'JDiRbZav7UvDhz4'
email = 'rashidarul@protonmail.com'

#return x, y cordinates
def searching(LocationName):
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
    arealist = coordinatesTupleOnly()
    tree = spatial.KDTree(arealist)
    result = tree.query([(x, y)]) #k=5?
    return arealist[result[1][0]]



# process data to prepare for searching
def coordinatesTupleOnly(LocationName = 'sengkang'):
    carparkinfo = "https://data.gov.sg/api/action/datastore_search?resource_id=" + resource_id + "&q=" + LocationName
    carparkInfoJson = testFunctions.getOutput(carparkinfo)
    xylist = []
    for carpark in carparkInfoJson['result']['records']:
        xytuple = ((carpark['x_coord']),carpark['y_coord'])
        xylist.append(xytuple)
    return xylist

# find a list of carpark in area
def findNearestArea(LocationName = 'sengkang'):
    carparkinfo = "https://data.gov.sg/api/action/datastore_search?resource_id=" + resource_id + "&q=" + LocationName
    carparkInfoJson = testFunctions.getOutput(carparkinfo)
    xylist = []
    for carpark in carparkInfoJson['result']['records']:
        xydic = {'car_park_no': carpark['car_park_no'],
                 'x_coord': carpark['x_coord'],
                'y_coord': carpark['y_coord']
                 }
        xylist.append(xydic)
    return xylist

#match carpark code back to area to find specific carpark
def matchingCarparkCode(x,y, LocationName='sengkang'):
    carparks = findNearestArea(LocationName)
    code = ''
    for carpark in carparks:
        if (carpark['x_coord'] == x) and (carpark['y_coord'] == y):
            code = carpark['car_park_no']
    return code

# program run area
# find a way to let user input

# step 2:
# run nearest cords and get back closest neighbour cordinates
coordinates = nearestCords(32051.5030,41600.0851)
# then use that to get the carpark code that belong to the neighbour
carparkcode = matchingCarparkCode(coordinates[0],coordinates[1])
print(carparkcode) # returns carpark code only and not the full detail yet

# step 1:
# one map searching of coordinates: From location name to coordinates.
# BLK 457 SENGKANG WEST RD cannot be found: limitations <<<< need non specific area :(
onemap = searching('sengkang west 457')
print(onemap)


