import requests
import pprint

URL = "http://127.0.0.1:8000/stuinfo/"

r = requests.get(url = URL)

data = r.json()

pprint.pprint(data) #The pprint module in Python is used to pretty-print the output of complex data structures like dictionaries and lists