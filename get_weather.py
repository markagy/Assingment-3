import urllib.request
import json
from get_iss import iss_loc


def iss_weather():
    lat, lon = iss_loc()

    key = "f6d64712fc593c4f75df0dba7ecb3255"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric"
    

    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    temp_c = result["main"]["temp"]
    desc = result["weather"][0]["description"]
    humidity = result["main"]["humidity"]

    print(temp_c, desc, humidity)


