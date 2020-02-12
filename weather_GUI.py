import requests
import tkinter as tk
import getpass
import json

#username into a variable
username = getpass.getuser()

#creating canvas
root = tk.Tk(className='Weather', useTk=1)
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

#days entry box label
label4 = tk.Label(root, text='Days of forecast')
label4.config(font=('verdana', 12))
canvas1.create_window(120, 160, window=label4)

#days entry box
entry2 = tk.Entry(root)
canvas1.create_window(380, 160, window=entry2)

#get forecast function-creating labels
def get_forecast():
    city = entry1.get()
    days = entry2.get()
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

    querystring = {"q":city,"cnt":days,"units":"metric"}

    headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "78034bcf5emsh6d33f4776102e77p10adaajsn7041714f6122"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    data2 = response.text
        
    label1 = tk.Label(root, text='WEATHER FORECAST FOR ' + city.upper())
    label1.config(font=('verdana', 9, 'bold'))
    canvas1.create_window(320, 240, window=label1)
    
    #city input check
    if data['cod'] != '404':
        #writing the response.json to a txt file
        with open('weather.txt', 'w') as file:
            file.write(json.dumps(data))
        #writing the response to a json file
        f = open("weather.json", "w")
        f.write(data2)
        f.close() 
            
        label2 = tk.Label(root, text='City Found. \n TXT File Created \n JSON File Created')
        label2.config(font=('verdana', 9, 'bold'))
        canvas1.create_window(320, 280, window=label2)
    else:
        label4 = tk.Label(root, text='City Not Found')
        label4.config(font=('verdana', 9, 'bold'))
        canvas1.create_window(320, 280, window=label4)
        

#creating a button and adding the function    
button1 = tk.Button(text='Get forecast', command=get_forecast)
button1.config(bg='red', fg='white', font=('verdana', 9, 'bold'))
canvas1.create_window(320, 200, window=button1)

#exit button
button2 = tk.Button(text='Exit', command=root.destroy)
button2.config(bg='Black', fg='white', font=('verdana', 10, 'bold'))
canvas1.create_window(320, 600, window=button2)

root.mainloop()