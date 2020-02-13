import requests
import tkinter as tk
import getpass
import json

#username into a variable
username = getpass.getuser()

#creating canvas
root = tk.Tk(className=' Weather', useTk=1)
canvas1 = tk.Canvas(root, width=640, height=640)
canvas1.pack()

#Greeting
label1 = tk.Label(root, text='Welcome, ' + username + '!')
label1.config(font=('verdana', 20))
canvas1.create_window(320, 30, window=label1)

#Header
label2 = tk.Label(root, text='Weather Forecast')
label2.config(font=('verdana', 18, 'bold'))
canvas1.create_window(320, 70, window=label2)

#city entry box label
label3 = tk.Label(root, text='Enter a city name')
label3.config(font=('verdana', 12))
canvas1.create_window(120, 130, window=label3)

#city entry box 
entry1 = tk.Entry(root)
canvas1.create_window(380, 130, window=entry1)

#get forecast function-creating labels
def get_forecast():
    city = entry1.get()
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":city,"units":"metric"}

    headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "78034bcf5emsh6d33f4776102e77p10adaajsn7041714f6122"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #temporary saving response as json
    data = response.text
    data2 = response.json()
             
    label1 = tk.Label(root, text='WEATHER FORECAST FOR ' + city.upper())
    label1.config(font=('verdana', 9, 'bold'))
    canvas1.create_window(320, 240, window=label1)
    
    #city input check
    if data2['sys']['cod'] != '404':
        #creating json file from response file if city is found
        f = open("weather.json", "w")
        f.write(data)
        f.close()
        country_name = data2["sys"]["country"]
        city_name = data2["sys"]["name"]
        current_temperature = data2["main"]["temp"]
        current_pressure = data2["main"]["pressure"]
        current_humidity = data2["main"]["humidity"]
        weather_description = data2["weather"]["main"]  
                
        label2 = tk.Label(root, text='City Found'.upper() + '\n JSON File Created')
        label2.config(font=('verdana', 9, 'bold'))
        canvas1.create_window(320, 280, window=label2)
        
        label3 = tk.Label(root, text='City Details: \n ' + city_name + '\n' + country_name)
        label3.config(font=('verdana', 9, 'bold'))
        canvas1.create_window(100, 340, window=label3)
        
        label4 = tk.Label(root, text=" Temperature (Celsius) = " + str(current_temperature) + "\n atmospheric pressure (hPa) = " + str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))
        label4.config(font=('verdana', 9, 'bold'))
        canvas1.create_window(500, 340, window=label4)  
    else:
        label5 = tk.Label(root, text='City Not Found')
        label5.config(font=('verdana', 9, 'bold'))
        canvas1.create_window(320, 280, window=label5)
        

#creating a button and adding the function    
button1 = tk.Button(text='Get forecast', command=get_forecast)
button1.config(bg='red', fg='white', font=('verdana', 9, 'bold'))
canvas1.create_window(320, 200, window=button1)

#exit button
button2 = tk.Button(text='Exit', command=root.destroy)
button2.config(bg='Black', fg='white', font=('verdana', 10, 'bold'))
canvas1.create_window(320, 600, window=button2)

root.mainloop()