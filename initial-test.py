# Test on the fly with webbrowser
#url = "https://maps.googleapis.com/maps/api/staticmap?size=600x400"
#webbrowser.open(url)
import os
import csv
import requests
from urllib.parse import urlencode
import webbrowser

print('1')

# Set base url as basis on which to make queries
BASE_URL ="https://maps.googleapis.com/maps/api/distancematrix/json?"

print('BASE_URL')

os.chdir("C:\\Users\\Nick\\Documents\\Documents\\Decision Support\\App 

Development - Pub Crawl Creator")
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

mydict = ['origins':str_origins,'destinations':str_destinations,'mode':'walking','language':'en-EN','key':'AIzaSyCEkcQlgD77bHxS_g31KwsUWoHvFuiT-YY']

Send_URL = BASE_URL + urlencode(mydict, doseq = True)

webbrowser.open(SEND_URL)

# A little confused about the library here: 

https://github.com/googlemaps/google-maps-services-python
