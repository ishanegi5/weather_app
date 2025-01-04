import requests
import json
import pyttsx3
city=input("Enter the city name: ")
url=f"https://api.weatherapi.com/v1/current.json?key=eee807ff601a4dd4982113351250301&q={city}"
r=requests.get(url)
# print(r.text)       #till here also the program is fine
information=json.loads(r.text)
winfo=information["current"]["temp_c"]
t_d_info=information["location"]["localtime"]
engine=pyttsx3.init()
engine.say(f"temperature in {city} is: {winfo} at {t_d_info}")
engine.runAndWait()