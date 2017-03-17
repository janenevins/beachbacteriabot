from sys import argv

def get_beach_names(): #this works in the interactive shell, but the function doesn't work when I paste it in
    rows = get_data()
    names = []
    for r in rows:
        names.append(r['Site Name'])

    return set(names) #set() is an unordered collection with no duplicate elements


def make_story(result): #this returns a string that is printed out in a separate function
        result = get_beach_results(beachname)
    ecoccus_count = int(result['Enterolert Enterococci Result'])
    storytemplate = """
    {beach_name} has an Entero bacteria count of {e_count}
    on the date of {process_date}. This is {number}times the safe limit.
    """

    return storytemplate.format(
        beach_name=result['Site Name'],
        e_count=ecoccus_count,
        process_date=result['Process Date']
    )

def bot(beachname): #this function returns a list of the unique Site Names
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

    
