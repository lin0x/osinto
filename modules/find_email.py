from fullcontact import FullContact
from .configuration import full_contact_api_key

fcontact = FullContact(full_contact_api_key)


def getData(email_address):
    try:
        info = fcontact.person(email=email_address)
        response = json.loads(info)

        print("Email Details:\n")
        print("*"*10)
        print("Full Name: : " + data['contactInfo']['fullName'])

    except:
        print("Unavailable!")
