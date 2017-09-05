from urllib.parse import urlencode
import webbrowser

# Set base url as basis on which to make queries
BASE_URL ="https://maps.googleapis.com/maps/api/distancematrix/json?"

# Test on the fly with webbrowser
#url = "https://maps.googleapis.com/maps/api/staticmap?size=600x400"
#webbrowser.open(url)

str_origins = ['Alterego, Bristol', 'The Bank, Bristol']
str_destinations = ['The Lansdown, Bristol', 'The Crown, Bristol', 'Ye Shakespear, Bristol']

mydict = ['origins':str_origins,'destinations':str_destinations,'mode':'walking','language':'en-EN','key':'AIzaSyCEkcQlgD77bHxS_g31KwsUWoHvFuiT-YY']

Send_URL = BASE_URL + urlencode(mydict, doseq = True)

webbrowser.open(SEND_URL)

# A little confused about the library here: https://github.com/googlemaps/google-maps-services-python
