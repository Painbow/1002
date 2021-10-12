import testFunctions
import json
import normanFunc
import pandas
import tablecreation

resource_id = "139a3035-e624-4f56-b63f-89ae28d4ae4c"
area = ""
carparkType = ""
freeparking = False;
validInput = True;
filter = False;
displayType = normanFunc.getUserInput()
if displayType == '1':
    print("Loading table for all carparks")
elif displayType == '2':
    area = input("Which area who you like to check?")
    print("Loading table for carpark near %s"%area)
elif displayType == '3':
    carparkType = normanFunc.getCarparkType()
    print("Loading table for carpark that are %s"%carparkType)
elif displayType == '4':
    freeparking = True;
    print("Loading table for carpark that are free")
else:
    validInput = False;

if validInput:
    #getting carpark info from api
    carparkinfo = "https://data.gov.sg/api/action/datastore_search?resource_id="+resource_id+"&q=" + area
    carparkInfoJson = testFunctions.getOutput(carparkinfo)
    #getting carpark avail info from api
    listOfCarparkData = normanFunc.getAllCarparkAvail()
    if len(carparkType)>0 or freeparking:
        filter = True

    if (carparkInfoJson['success']):
        result = carparkInfoJson['result']
        recordList = result['records']
        if len(carparkType) > 0 or freeparking:
            filter = True
        if filter:
            filterList = []
            for carpark in recordList:
                cpType = carpark["car_park_type"]
                cpFree = carpark["free_parking"]
                # print ("cptype %s and %s"%(cpType,carparkType))
                if freeparking and cpFree != "NO":
                    filterList.append(carpark)
                    # print("free carpark")
                elif len(carparkType)>0 and carparkType == cpType:
                    filterList.append(carpark)
                    # print("surface carpark")

            recordList = filterList

        for carpark in recordList:

            cpNo = carpark['car_park_no']
            availStatus = normanFunc.getCarparkAvail(listOfCarparkData, cpNo)
            if(availStatus != None):
                carpark['total_lot'] = availStatus[0]['total_lots']
                carpark['lot_type'] = availStatus[0]['lot_type']
                carpark['lot_available'] = availStatus[0]['lots_available']


        dataframe = pandas.json_normalize(recordList)
        tablecreation.LoadTable(dataframe)
    else:
        print("Unable to access API")


