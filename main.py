from flask import Flask,  render_template
import json
import urllib.request
from get_iss_loc import iss_loc
from get_weather import iss_weather
from get_distance import dist
from get_reverse_geo import address
from get_country_info import get_map_flag

app = Flask('app')



@app.route('/')
def main():
    #get the latitude and longitude of the ISS location:
    lat, lon = iss_loc()

    # get the temperature, description and humidity below ISS
    temp, desc, humidity = iss_weather(lat,lon)

    #get distance between me and ISS
    my_lat = 46.5204601 # latitude for cambrian college
    my_lon = -81.0160148 # longitude for cambrian college
    distance = dist(my_lat,my_lon,lat,lon)

    
    #Get the country,country code,  city and water body the ISS is currently flying over
    city, country, ocean, code = address(lat,lon)

    #Get the flag and map_link of the country using country code
    country_flag, map_link = get_map_flag(code)

    return render_template('index.html', lat = lat , lon=lon, distance = distance, temp = temp, desc = desc, humidity = humidity, city=city, country = country, ocean =ocean, map_link=map_link, country_flag=country_flag)


app.run(host='0.0.0.0', port=5000)

