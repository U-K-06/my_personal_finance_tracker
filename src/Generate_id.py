from random import randint
from constants import Constants
import json

def generate_random_id():

    with open(Constants.JSON_IDS_PATH) as json_data:
        json_data = json.load(json_data)

    id = randint(Constants.START_RANDOM_IDS,Constants.END_RANDOM_IDS)

    while(id in json_data['ids']):
        id = randint(Constants.START_RANDOM_IDS,Constants.END_RANDOM_IDS)

    json_data['ids'].append(id)
    with open(Constants.JSON_IDS_PATH,'w') as json_file:
        json.dump(json_data,json_file)

        
def clear_ids():
    with open(Constants.JSON_IDS_PATH,'w') as json_file:
            data = {'ids':[]}
            json.dump(data,json_file)
