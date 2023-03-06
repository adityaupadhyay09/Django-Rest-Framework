import requests
import json
import pprint


URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data= {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    pprint.pprint (data)
# get_data()

def post_data():
    data = {
        'name' : 'Chandan',
        'roll_no' : 190616,
        'city' : 'Ranchi'     
    }  
    
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    
    
post_data()