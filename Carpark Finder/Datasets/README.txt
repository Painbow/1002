For our project, we do not store any JSON outputs as files.

While this may reduce loading speeds (less need to constantly retrieve data), the goal of the application is to obtain information in real-time.

However, included are several examples of data outputs from the two API URLs that our project utilises.

1. Carpark Information Raw
(https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c&limit=2162)

Included is the (formatted) JSON output from the URL. The output has to be normalised to strip away unnecessary information (timestamp etc.).

2. Carpark information Normalised
An Excel file to emulate how a normalised version of the JSON ouput would look like.The normalised version is what will be used to generate a pandas dataframe to display the results.

2. Carpark Availability
(https://api.data.gov.sg/v1/transport/carpark-availability?)

Included is the (formatted) JSON output from the URL. Since we are only accessing certain values from the output, the output does not need to be normalised.

