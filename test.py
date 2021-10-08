test = "{'item': [{'timestamp': '2021-10-07T20:34:26+08:00', 'carpark_data': [{'carpark_info': [{'total_lots': '105', 'lot_type': 'C', 'lots_available': '26'}], 'carpark_number': 'HE12', 'update_datetime': '2021-10-07T20:15:41'}]}]}"


# Defailt Output is a dictionary,
    # containing a list (items),
        # > timestamp,
        # > carpark_data
            # which contains a list
                # which contains a dictionary
                    # > carpark_info
                        # contains a list
                            #containing a dictionary
                                # > total_lots
                                # > lot_type
                                # > lots_available
                    # > carpark_number
                    # > update_datetime


print((eval(test)["item"])[0]["carpark_data"][0]["carpark_info"][0]["total_lots"])

 # {'timestamp': '2021-10-07T20:34:26+08:00', 'carpark_data': [{'carpark_info': [{'total_lots': '105', 'lot_type': 'C', 'lots_available': '26'}], 'carpark_number': 'HE12', 'update_datetime': '2021-10-07T20:15:41'}]}