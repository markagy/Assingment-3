
import urllib.request 
import json



def get_map_flag(code):
    if code:
        url= f'https://restcountries.com/v3.1/alpha/{code}'
        #url=f'https://restcountries.com/v3.1/name/{country}'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        flag = result[0]['flags']['png']
        g_map = result[0]['maps']['googleMaps']
    else:
        flag = None
        g_map = None
        #print('There is no map available because ISS is over water')
    
    return flag, g_map
