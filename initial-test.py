# Created by Nick Rose, Sep-17
# Initial development file to grow understanding of Python and look at getting pairwise distances from the Google Maps Services Distance API

import os
import csv
import requests
from urllib.parse import urlencode
import webbrowser

# Set base url as basis on which to make queries
BASE_URL ="https://maps.googleapis.com/maps/api/distancematrix/json?"

os.chdir("C:\\Users\\Nick\\Documents\\Documents\\Decision Support\\App Development - Pub Crawl Creator")
newfile = csv.DictReader(open('Bristol Pubs - Origins.csv'))
str_origins = []
For row in newfile:
  str_origins.append(row['Origins'])
  
newfile = csv.DictReader(open('Bristol Pubs - Destinations.csv'))
str_destinations = []
For row in newfile:
  str_destinations.append(row['Destinations'])


#str_origins = ['Alterego, Bristol', 'The Bank, Bristol']
#str_destinations = ['The Lansdown, Bristol', 'The Crown, Bristol', 'Ye Shakespear, Bristol']

mydict = ['origins':str_origins,'destinations':str_destinations,'mode':'walking','language':'en-EN','key':'MY-KEY']

Send_URL = BASE_URL + urlencode(mydict, doseq = True)

# Test to see whether we get a JSON webpage showing the pairwise walking distances between pubs 
webbrowser.open(SEND_URL)

# If so then get into reading the JSON text returned by this URL


### NOTES ###
# A little confused about the library here: https://github.com/googlemaps/google-maps-services-python

# Test on the fly with webbrowser
#url = "https://maps.googleapis.com/maps/api/staticmap?size=600x400"
#webbrowser.open(url)
