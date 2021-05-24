import requests
import keys
from requests.auth import HTTPBasicAuth



def generate_access_token():

    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))


    json_response = r.json() # {'access_token': 'F1cmMs12nHDpqy5Vbo0c4WxrM85u', 'expires_in': '3599'}

    my_access_token = json_response['access_token']

    return my_access_token
