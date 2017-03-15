import csv
import requests

SRC_DATA_URL = 'https://data.smcgov.org/api/views/kpd9-xf4h/rows.csv?accessType=DOWNLOAD'

def get_data():
    resp = requests.get(SRC_DATA_URL)
    txt = resp.text
    lines = txt.splitlines()
    results = list(csv.DictReader(lines))
    return results

def fix_date_string(datestring):
    """
    datestring change from '04/05/1984' to
    '1984-05-04'
    """
    ds = datestring.split('/')
    return '-'.join([ds[2], ds[0], ds[1]])

def __sortfoo(somerecord):
    a = somerecord['Process Date']
    b = fix_date_string(a)
    return b

def get_beach_names():
    rows = get_data()
    names = []
    for r in rows:
        names.append(r['Site Name'])

    return set(names)

def get_beach_results(beachname):
    all_rows = get_data()
    filtered_rows = []

    for row in all_rows:
        if row['Site Name'] == beachname.upper():
            filtered_rows.append(row)

    return sorted(filtered_rows, key=__sortfoo, reverse=True)

def make_story(result):
    ecoccus_count = int(result['Enterolert Enterococci Result'])
    storytemplate = """
    {beach_name} has an Entero bacteria count of {e_count}
    on the date of {process_date}.
    """

    return storytemplate.format(
        beach_name=result['Site Name'],
        e_count=ecoccus_count,
        process_date=result['Process Date']
    )

def bot(beachname):
    official_beachnames = get_beach_names()

#10 day avg
#%increase
#list of beaches if it doesn't work
