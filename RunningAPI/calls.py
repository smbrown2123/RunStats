# functions which send the requests to the api

import requests
import json
from RunningAPI.generic import *

def get_stats():
    renew_access() 
    params = get_api_parameters()
    ID = params[0]
    AccessToken = params[4]
    URL = f'https://www.strava.com/api/v3/athletes/{ID}/stats'
    PARAMS = {'access_token':AccessToken}

    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    
    return data

def get_activities(Page: int, PerPage = 200):
    renew_access()
    params = get_api_parameters()
    AccessToken = params[4]
    URL = 'https://www.strava.com/api/v3/athlete/activities'
    PARAMS = {'access_token':AccessToken, 'per_page':PerPage, 'page':Page}
    
    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    
    return data

def renew_access(grantType = 'refresh_token'):
    params = get_api_parameters()
    ClientID = params[1]
    ClientSecret = params[2]
    RefreshToken = params[3]
    
    URL = 'https://www.strava.com/oauth/token'
    PARAMS = {'client_id':ClientID, 'client_secret':ClientSecret, 'refresh_token':RefreshToken, 'grant_type':grantType}
    
    r = requests.post(url = URL, params = PARAMS)
    
    data = r.json()
    authToken = data['access_token']
    
    with open('params.json', 'r', encoding = 'utf-8') as f:
        data = json.load(f)
        
    data['parameters']['accesstoken'] = authToken
    
    with open('params.json', 'w', encoding = 'utf-8') as f:
        json.dump(data, f, ensure_ascii = 'False, indent = 4')
    
        
        