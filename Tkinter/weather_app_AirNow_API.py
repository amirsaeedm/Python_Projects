from tkinter import *
from PIL import ImageTk,Image
import requests
import json


root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('codemy.ico')
#root.geometry("400x40")

# Las Vagas Zipcode = 89129
# Grangeville Zicode = 83530
# Baton Rouge Zipcode = 70801
#Fresno Zipcode = 93650

def ziplook():

	try:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+str(zip_entry.get())+"&distance=5&API_KEY=69EA2B78-84BE-425E-863D-FB093D6E93B3")
		api = json.loads(api_request.content)
		city = api[0]['ReportingArea']
		quality = api[0]['AQI']
		category = api[0]['Category']['Name']

		if category=='Good':
			weather_color = '#0C0'
		elif category=='Moderate':
			weather_color = '#FFFF00'
		elif category=='Unhealthy for Sensitive Groups':
			weather_color = '#FF9900'
		elif category=='Unhealthy':
			weather_color = '#FF0000'
		elif category=='Very Unhealthy':
			weather_color = '#990066'
		elif category=='Hazardous':
			weather_color = '#660000'

		root.configure(background=weather_color)
		myLabel = Label(root,text=city+" Air Quality "+str(quality)+"  "+category,font=('Helvetica',20),background=weather_color)
		myLabel.grid(row=1,column=0,columnspan=2)
		myLable.forget()

	except Exception as e:
		api = "Error ..."

zip_entry = Entry(root)
zip_entry.grid(row=0,column=0,stick=W+E+N+S)

zip_button = Button(root,text='Lookup ZipCode',command=ziplook)
zip_button.grid(row=0,column=1,stick=W+E+N+S)

root.mainloop()