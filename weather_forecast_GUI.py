import requests
import tkinter as tk
import getpass
import json
import datetime

#username into a variable
username = getpass.getuser()

#creating canvas
root = tk.Tk(className=' Weather', useTk=1)
canvas1 = tk.Canvas(root, width=640, height=800)
canvas1.pack()

#adding window icon
root.iconbitmap('weather.ico')

#Forbid resizing in the x or y direction
root.resizable(0, 0)

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
canvas1.create_window(400, 130, window=entry1)

#days entry box label
label4 = tk.Label(root, text='Days of forecast')
label4.config(font=('verdana', 12))
canvas1.create_window(120, 160, window=label4)

#days entry box
entry2 = tk.Entry(root)
canvas1.create_window(400, 160, window=entry2)

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
    #temporary saving response as json
    data = response.json()
    data2 = response.text  
     
    label1 = tk.Label(root, text='WEATHER FORECAST FOR ' + city.upper())
    label1.config(font=('verdana', 9, 'bold'))
    canvas1.create_window(320, 240, window=label1)
    
    #city input check
    if data['cod'] != '404':
                
        label2 = tk.Label(root, text='City Found'.upper())
        label2.config(font=('verdana', 9, 'bold'))
        canvas1.create_window(320, 280, window=label2)
        
        city_data_json = data['city']
        label3 = tk.Label(root, text='City Details:\n' + str(city_data_json['name']) + '\n' + str(city_data_json['country']))
        label3.config(font=('verdana', 10, 'bold'))
        canvas1.create_window(120, 350, window=label3)
        
        lb = tk.Listbox(root, height=30, width=35)
        lb.config(font=('verdana', 9))
        lb.place(x=260, y=300)
        for day in data['list']:
            date = str(datetime.datetime.fromtimestamp(day['dt']).strftime('%d-%m-%y'))
            weather =str(day['weather'][0]['description'])
            min_temp = float(day['temp']['min'])
            max_temp = float(day['temp']['max'])
            hum = int(day['humidity'])
            text = 'DATE:'
            text2 = 'Weather:'
            text3 = 'Temp min:'
            text4 = 'Temp max:'
            text5 = 'Humidity:'
            lb.insert('end', '{0} {1}'.format(text, date[0:11]))
            lb.insert('end', '{0} {1}'.format(text2, weather))
            lb.insert('end', '{0} {1}'.format(text3, min_temp))
            lb.insert('end', '{0} {1}'.format(text4, max_temp))
            lb.insert('end', '{0} {1}'.format(text5, hum))
            lb.insert('end', '')
            
        label4 = tk.Label(root, text='save the complete \n forecast in a \n txt file'.title())
        label4.config(font=('verdana', 9, 'bold'))
        canvas1.create_window(120, 500, window=label4)
        
        def create_txt():
            file = open("forecast.txt", "w")
            file.write(data2)
            file.close()
            
        button1 = tk.Button(text='Save', command=create_txt)
        button1.config(font=('verdana', 9, 'bold'))
        canvas1.create_window(120, 540, window=button1)
    
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
canvas1.create_window(320, 780, window=button2)

root.mainloop()