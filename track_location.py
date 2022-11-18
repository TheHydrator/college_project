#!/usr/bin/env python
# coding: utf-8

# In[1]:


import phonenumbers
import opencage # latitude and longitude
import folium #a powerful Python library that helps you create several types of Leaflet maps
from phonenumbers import geocoder

import pyttsx3
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
number = "+919619376823"
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
API_KEY = "30d03aefbb7e44b6b51ab439473db921"
geocoder = OpenCageGeocode(API_KEY)
query = str(location)
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("mylocation.html")

talk(location)


# In[ ]:




