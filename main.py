# Example date_time parameter
# 2021-10-07T20:34:27+08:00

# Example request
# https://api.data.gov.sg/v1/transport/carpark-availability?date_time=2021-10-07T20%3A34%3A27%2B08%3A00

import requests

# prints output of an API call
# r is bytes class
url = "https://api.data.gov.sg/v1/transport/carpark-availability?date_time=2021-10-07T20%3A34%3A27%2B08%3A00"
r = requests.get(url)

eval(r.content.decode("utf-8"))


# {"items":[{"timestamp":"2021-10-07T20:34:26+08:00", "carpark_data": [
# {"carpark_info":[{"total_lots":"105","lot_type":"C","lots_available":"26"}],"carpark_number":"HE12","update_datetime":"2021-10-07T20:15:41"},
# {"carpark_info":[{"total_lots":"583","lot_type":"C","lots_available":"411"}],"carpark_number":"HLM","update_datetime":"2021-10-07T20:15:25"},