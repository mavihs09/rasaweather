import requests

def Weather(city):

    api_address='http://api.openweathermap.org/data/2.5/weather?q='
    api_address1 = '&appid=639abaa2a3314a03b2a01e926252ed4a'
    #city = input('Enter the City Name :')
    url = api_address + city + api_address1
    json_data = requests.get(url).json()
    format_add = json_data['main']
    print(format_add)
    print("Weather is {0} Temperature is mininum {1} Celcius and maximum is {2} Celcius".format(
        json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
    return format_add

