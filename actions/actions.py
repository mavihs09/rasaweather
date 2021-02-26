# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city=tracker.latest_message['text']

        api_address='https://serene-coast-83014.herokuapp.com/temperature/'

        url = api_address + city 
        json_data = requests.get(url).json()
        Town = json_data['name']
        Weather = json_data['weather'][0]['main']

        format_add = json_data['main']
        Temp = int(format_add['temp']-272.15)
        Maxi = int(format_add['temp_max']-272.15)
        Mini = int(format_add['temp_min']-273.15)

        Humidity = format_add['humidity']
        Pressure = format_add['pressure']
        WS = json_data['wind']['speed']

        dispatcher.utter_template("utter_temp",tracker,city=Town,weather=Weather,temp=Temp,maxi=Maxi,mini=Mini,hum=Humidity,press=Pressure,ws=WS)
        

        return []
