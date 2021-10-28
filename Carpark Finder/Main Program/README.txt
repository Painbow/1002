Application User Manual
=======================

1. Run "Install Requirements Script.bat" or "py -m pip install -r requirements.txt" in Command Prompt

	- The application uses several libraries. In order for them to function certain packages have to be installed, preferably using pip.

2. Run "Launch Program Script.bat" or "python main.py" in the Main Program directory

	- Launching the application will greet you with 3 tabs, "Display Carpark Information", "Carpark Availability Graph" and "Statistics".



DISPLAY CARPARK INFORMATION
===========================

3. If desired, select filters such as which carpark type to display, and whether or not to only display carparks with free parking

	- By default, all carparks (all 2162 entries) will be displayed).

4. If desired, enter location keywords in the text box, to display entries related to that location.

	- By default, all locations will be displayed. 

	- Filtering by more than one location is possible. 
	  For instance, "bishan woodlands" will return carparks from Bishan as well as carparks from Woodlands.
	  
	- Some locations do not have carpark data entries (areas such as "marina", "bugis" etc. have no results).

5. Clicking "OK" will display a table with carpark information (if possible) and carpark availability (lots available).
	
	- Availability information is updated at various time intervals. Hence, sometimes, availability information may not be currently accessible.

6. Clicking on a row, will open a Google Map result with that carpark's location

	- Clicking on any cell in the row will return the location for that entry


DISPLAY CARPARK AVAILABILITY GRAPH
==================================

7. By default, data from the past 5 days will be retrieved, however users may specify how many days of information they wish to retrieve.
	
	- As the carpark availability site is queried several times according to the number of days specified, increasing the number of days may cause a longer delay before results are displayed

8. By default, results for carpark HE12 will be displayed, however users may define which carpark number should be used when searching for past days' availability records.

	- As carpark information is updated at various time intervals, there may be times when the carpark data cannot be retrieved. If this is the case, an error message will be produced.


DISPLAY STATISTICS
==================

9. Pressing "Fetch" will obtain some statistics regarding the spread of "carpark types" and "free parking".

	- A quick tally will be made and displayed