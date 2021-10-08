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

def getOutput(x):
    r = requests.get(x)
    return json.loads(r.content)



