import csv
import requests



SRC_DATA_URL = 'https://data.smcgov.org/api/views/kpd9-xf4h/rows.csv?accessType=DOWNLOAD'

def get_data(): #this function downloads the data and creates a list of dictionaries
    resp = requests.get(SRC_DATA_URL)
    txt = resp.text
    lines = txt.splitlines()
    results = list(csv.DictReader(lines))
    return results
