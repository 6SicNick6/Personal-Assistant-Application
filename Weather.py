from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import requests

window = tk.Tk()
window.title("Weather app")
window.geometry("400x200")

input_frame = ttk.Frame(window)
input_frame.pack(pady=10)

api_key = "2b263e3597936d7450316fb67b4dc1da"
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}" 

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celcius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_celcius, temp_fahrenheit, icon, weather)
        return final
    else:
        return None
    
def search():
    global image_lbl
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        #image['bitmap'] = 'weather_icons/{}.png'.format(weather[4])
        temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5]
        img = "{}@2x.png".format(weather[4])
        #img = tk.PhotoImage(file='{}@2x.png'.format(weather[4]))
        #image_lbl.image = img
        image_lbl = Label(window, image=img)
        image_lbl.image = img
        image_lbl.pack()    
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

city_input = Label(input_frame, text="Enter your city:")
city_input.grid(row=0, column=0)

city_text = StringVar()
city_entry = Entry(input_frame, textvariable=city_text)
city_entry.grid(row=0, column=1)

search_btn = Button(input_frame, text="Show Weather", width=11, command=search)
search_btn.grid(row=1, column=1)

location_lbl = Label(input_frame, takefocus="Location", font=("bold", 20))
location_lbl.grid(row=2, column=1)

image_lbl = Label(input_frame, image="")
image_lbl.grid(row=3, column=1)

temp_lbl = Label(input_frame, text="")
temp_lbl.grid(row=4, column=1)

weather_lbl = Label(input_frame, text="")
weather_lbl.grid(row=5, column=1)

window.mainloop()