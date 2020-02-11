import requests
import tkinter as tk
import getpass


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

#get forecast function-creating labels
def get_forecast():
    city = entry1.get()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid=408973bfe4332ff2c0599a72e8fd8e0e'.format(city)
    r = requests.get(url)
    
    label1 = tk.Label(root, text='WEATHER FORECAST FOR  ' + city.upper())
    label1.config(font=('verdana', 9, 'bold'))
    canvas1.create_window(320, 240, window=label1)
    
    label2 = tk.Label(root, text=r)
    label2.config(font=('verdana', 8, 'bold'))
    canvas1.create_window(320, 260, window=label2)

#creating a button and adding the function    
button1 = tk.Button(text='Get forecast', command=get_forecast)
button1.config(bg='red', fg='white', font=('verdana', 9, 'bold'))
canvas1.create_window(320, 200, window=button1)

#exit button
button2 = tk.Button(text='Exit', command=root.destroy)
button2.config(bg='Black', fg='white', font=('verdana', 10, 'bold'))
canvas1.create_window(320, 600, window=button2)

root.mainloop()