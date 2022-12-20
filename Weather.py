import PySimpleGUI as sg
import requests
import json
def get_weather(city):
    r = requests.get("http://wthrcdn.etouch.cn/weather_mini?citykey=" + city)
    result = json.loads(r.text)
    return result["data"]["forecast"][0]["type"]
sg.SetOptions(text_justification='center') 
layout = [ 
           [ sg.Text("City", size = (20, 1)), sg.Input(key = "-CITY-") ],
           [ sg.Text("Weather", size = (20, 1)), sg.Input(key = "-WEATHER-") ],
           [ sg.Button("Submit")]
         ]
window = sg.Window("Weather App", layout)
event, values = window.read()
print(event, values)
city = values["-CITY-"]
weather = get_weather(city)
print(weather)
window.close()
