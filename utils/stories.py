from sys import argv
SAFE_BACTERIA_LEVEL = 104



def bacteria_ratio(row):
    return round(float(row['Enterolert Enterococci Result']) / SAFE_BACTERIA_LEVEL, 1)



def make_story(result, beachname): #this returns a string that is printed out in a separate function
    bac_ratio = bacteria_ratio(result)
    ecoccus_count = int(result['Enterolert Enterococci Result'])

    storytemplate = """
    {beach_name} has an Entero bacteria count of {e_count}
    on the date of {process_date}. This is {number} times the safe limit.
    """

    story = storytemplate.format(beach_name=beachname,
            e_count=ecoccus_count,
            process_date=result['Process Date'],
            number=bac_ratio)

    return story


