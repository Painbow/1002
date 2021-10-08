# Example date_time parameter
# 2021-10-07T20:34:27+08:00

# Example request
# https://api.data.gov.sg/v1/transport/carpark-availability?date_time=2021-10-07T20%3A34%3A27%2B08%3A00

# Default Output is a dictionary,
    # contains a list (items),
        # > timestamp,
        # > carpark_data
            # contains a list
                # contains a dictionary
                    # > carpark_info
                        # contains a list
                            # contains a dictionary
                                # > total_lots
                                # > lot_type
                                # > lots_available
                    # > carpark_number
                    # > update_datetime

# Format to access data is items, 0, timestamp/carpark_data, <index of dictionary>, carpark_info/carpark_number/update_datetime, 0, total_lots/lot_type/lot_available

# {'timestamp': '2021-10-07T20:34:26+08:00', 'carpark_data': [{'carpark_info': [{'total_lots': '105', 'lot_type': 'C', 'lots_available': '26'}], 'carpark_number': 'HE12', 'update_datetime': '2021-10-07T20:15:41'}]}