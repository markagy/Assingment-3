import urllib.request 
import json


def address(lat, lon):
  key= "bdc_914855f44b724991ab91b1c5fbe1bf83" 
  url= f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  country = result['countryName']
  city = result['city']
  country_code = result['countryCode']
  if country=="":
    ocean = result['localityInfo']['informative'][0]['name']
  else:
    ocean = None  
  return city, country,ocean,country_code



#