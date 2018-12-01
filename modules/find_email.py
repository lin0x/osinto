from fullcontact import fullcontact
from .configuration import *
import json

fcontact = FullContact(fullcontact_api_key)


def getData(email_address):
    try:
        info = fcontact.person(email=email_address)
        response = json.loads(info)

        print("Email Details:\n")
        print("*"*10)
        print("Full Name: : " + data['contactInfo']['fullName'])

    except:
        print("Unavailable!")
