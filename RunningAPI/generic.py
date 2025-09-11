# non running specific functions relating to the api

import RunningAPI.calls as calls
import json

def get_numner_of_activities():
    data = calls.get_stats()
    runs = data['all_run_totals']['count'] 
    cycles = data['all_ride_totals']['count'] 
    swims = data['all_swim_totals']['count']
    
    activities = runs + cycles + swims
    
    return activities

def get_api_parameters():
    with open('params.json') as f:
        params = json.load(f)

    ID = params["parameters"]["id"]
    ClientID = params["parameters"]["client_id"]
    ClientSecret = params["parameters"]["client_secret"]
    RefreshToken = params["parameters"]["refresh_token"]
    AccessToken = params["parameters"]["accesstoken"]
    
    return ID, ClientID, ClientSecret, RefreshToken, AccessToken