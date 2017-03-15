import csv
import requests
from sys import argv


SRC_DATA_URL = 'https://data.smcgov.org/api/views/kpd9-xf4h/rows.csv?accessType=DOWNLOAD'

def get_data(): #this function downloads the data and creates a list of dictionaries
    resp = requests.get(SRC_DATA_URL)
    txt = resp.text
    lines = txt.splitlines()
    results = list(csv.DictReader(lines))
    return results

def fix_date_string(datestring):  #this function transforms the date string into something that can be correctly sorted
    """
    datestring change from '04/05/1984' to
    '1984-05-04'
    """
    ds = datestring.split('/')
    return '-'.join([ds[2], ds[0], ds[1]])

def __sortfoo(somerecord): #this creats the key to sort by the date
    a = somerecord['Process Date']
    b = fix_date_string(a)
    return b

def get_beach_names(): #this gets a list of beach names - for the user error result
    rows = get_data()
    names = []
    for r in rows:
        names.append(r['Site Name'])

    return set(names) #set() is an unordered collection with no duplicate elements

def get_beach_results(beachname): #this sorts all the records by Process Date
    all_rows = get_data()
    filtered_rows = []

    for row in all_rows:
        if row['Site Name'] == beachname.upper(): #Getting an error because in this beachname is a list? list object has no attribute upper
            filtered_rows.append(row)

    return sorted(filtered_rows, key=__sortfoo, reverse=True)

def make_story(result): #this returns a string that is printed out in a separate function
        result = get_beach_results(beachname)
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

def bot(beachname): #this function returs a list of the unique Site Names
    official_beachnames = get_beach_names()
    story = make_story(result)
    return official_beachnames



if __name__ == '__main__': #I now realize I don't know how this works
    beachname = argv
    bnames = bot(beachname)

    if argv in bnames: #I expect that argv is the name of the beach passed in from the command line like "python badbeachbot.py 'Surfers Beach'"
        print(story)
    else:
        print('You must pick a beach from this list', bnames)


#things to ad
#10 day avg
# magnitude over the limit, like 2x the safe level of bacteria
#list of beaches if it doesn't work - WIP
