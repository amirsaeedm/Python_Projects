import requests
import json

ip = input("Enter the IP Address: ")
dict1 = {"IP_Address":[],"Country":[],"City":[],"Longitude":[],"Latitude":[]}

api_request = requests.get("http://ipwhois.app/json/"+ip)
api = json.loads(api_request.content)

dict1["IP_Address"].append(api['ip'])
dict1["Country"].append(api['country'])
dict1["City"].append(api['city'])
dict1["Longitude"].append(api['longitude'])
dict1["Latitude"].append(api['latitude'])

print(dict1)
print('Program has Exited')