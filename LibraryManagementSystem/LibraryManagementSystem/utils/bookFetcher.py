import requests

global recursionCtr
recursionCtr = 0

def fetchBookDetils(booktitle=''):
    URL = f'https://frappe.io/api/method/frappe-library?page=2&title={booktitle}'
    res = requests.get(URL)
    data = res.json()['message'] # FETCHING ONLY MESSAGE PART FROM REQUEST
    return data


