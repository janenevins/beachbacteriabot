from bacteriafoo import get_data
from stories import make_story, bot, get_beach_results
from datehelper.py import fix_date_string, __sortfoo





def get_beach_results(beachname): #this sorts all the records by Process Date
    all_rows = get_data()
    filtered_rows = []

    for row in all_rows:
        if row['Site Name'] == beachname.upper(): #Getting an error because in this beachname is a list? list object has no attribute upper
            filtered_rows.append(row)

    return sorted(filtered_rows, key=__sortfoo, reverse=True)



def bacteria_ratio():
sortedrows = get_beach_results(beachname)

for row in sortedrows:
    round(float(row['Enterolert Enterococci Result'])/104, 1)

    return bac_ratio







#things to ad
# magnitude over the limit, like 2x the safe level of bacteria
#okay to swim
