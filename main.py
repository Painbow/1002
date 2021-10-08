# Example date_time parameter
# 2021-10-07T20:34:27+08:00

# Example request
# https://api.data.gov.sg/v1/transport/carpark-availability?date_time=2021-10-07T20%3A34%3A27%2B08%3A00

import requests
import json
import pandas
import testFunctions
import tablecreation
from tkinter import *
from pandastable import Table


outputJson = testFunctions.getOutput("https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c&q=woodlands")
dataframe = pandas.json_normalize(outputJson["result"]["records"])

tablecreation.LoadTable(dataframe)
