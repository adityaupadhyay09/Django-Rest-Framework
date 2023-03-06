import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Aditya Upadhyay',
    'roll_no' : '190607',
    'city' : 'Delhi'
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

