# import phonenumbers
# import opencage
# from myphone import number
# import folium
# from phonenumbers import geocoder

# pepnumbr = phonenumbers.parse(number)
# location = geocoder.description_for_number(pepnumbr,"en")
# print(location)

# from phonenumbers import carrier
# service_pro = phonenumbers.parse(number)
# print(carrier.name_for_number(service_pro,"en"))



# from opencage.geocoder import OpenCageGeocode
# key = '4c4fbac41bad44c3a68441e5e5248145'

# geocoder = OpenCageGeocode(key)
# query = str(location)
# results = geocoder.geocode(query)







# print(results)


# let = results[0]['geometry']['lat']
# lag = results[0]['geometry']['lag']

# print(lat,lag)

# my_map = folium.Map(location=[lat,lag],zoom_start=9)

# folium.Marker([lat,lag],popup=location).add_to(my_map)


# my_map.save("mylocation.html")




import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from myphone import number  # Make sure this file defines: number = "+911234567890"

# Parse phone number
pepnumbr = phonenumbers.parse(number)

# Get location
location = geocoder.description_for_number(pepnumbr, "en")
print(location)

# Get service provider
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

# Use OpenCage API to get coordinates
key = '4c4fbac41bad44c3a68441e5e5248145'  # Use your own key securely
geocoder_api = OpenCageGeocode(key)
results = geocoder_api.geocode(location)

print(results)

# Extract coordinates (Fix typo: 'lag' ➝ 'lng', and 'let' ➝ 'lat')
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

# Create map and add marker
my_map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(my_map)

# Save the map
my_map.save("mylocation.html")
