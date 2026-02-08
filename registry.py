# used to import/export to json and store all the stuff

import json

# get the json file and extract


cores = {"Light Red": 2} #change this to an import export to json prolly?

def convert_to_json(user_list): # list of User objects
    json_dict = {}
    for user in user_list:
        # convert a user class to a dict
        json_dict[user.ID] = {}
        json_dict[user.ID]["CoreColor"] = user.Core_Color