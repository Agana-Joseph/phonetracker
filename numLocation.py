# To get the country location of the number
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
import phonenumbers

import folium

from phoneNum import number

from phonenumbers import geocoder

key = "cd28d6e13b2045d89eb8da3f4d36c903"

personNum = phonenumbers.parse(number)

personLocation = geocoder.description_for_number(personNum, "en")
print(personLocation)

# Get service provider e.g Aitel, MTN, ETC

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

# Get the latitude and longitude for  the map
geocoder = OpenCageGeocode(key)
query = str(personLocation)

result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=personLocation).add_to(myMap)

# Print map in HTML file

myMap.save("mytracker.html")
