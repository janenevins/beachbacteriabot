from sys import argv
from utils.bacteriafoo import get_beach_results, get_beach_names
from utils.stories import make_story

# Here's a comment
def bot(beachname):
    results = get_beach_results(beachname)
    if not results:
        bnames = get_beach_names()
        print(beachname, 'does not exist.')
        print('You must pick a beach from this list:')
        for bname in bnames:
            print(bname)

    else:
        result = results[0]
        story = make_story(result, beachname)
        return story



if __name__ == '__main__': #I now realize I don't know how this works
    beachname = argv[1]
    story = bot(beachname)

    print(story)





#things to ad
# magnitude over the limit, like 2x the safe level of bacteria
#okay to swim
