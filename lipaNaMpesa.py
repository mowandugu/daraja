import requests
from access_token import generate_access_token
from encode import generate_password
from utils import get_timestamp
import keys
from requests.auth import HTTPBasicAuth


formatted_time = get_timestamp()
decoded_password = generate_password(formatted_time)


def lipa_na_mpesa():


    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "5",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_shortCode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://kujaribu.com/api",
        "AccountReference": "12345678",
        "TransactionDesc": "Pay School Fees"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

lipa_na_mpesa()