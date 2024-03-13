import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(city, data):
    if data['cod'] == '404':
        messagebox.showerror("ERROR", "CITY NOT FOUND")
    else:
        temperature = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        messagebox.showinfo("WEATHER FORECAST", f"WEATHER IN  {city}: {weather_desc}, TEMPERATURE: {temperature}°C")

def get_weather_forecast():
    city = city_entry.get()
    api_key = 'enter-your-api-here'
    weather_data = get_weather(city, api_key)
    display_weather(city, weather_data)

window = tk.Tk()
window.title("WEATHER FORECAST APPLICATION")

label = tk.Label(window, text="ENTER CITY NAME:")
label.pack(padx=10, pady=10)
city_entry = tk.Entry(window)
city_entry.pack()

submit_button = tk.Button(window, text="GET WEATHER FORECAST", command=get_weather_forecast)
submit_button.pack(padx=10, pady=10)

window.mainloop()
