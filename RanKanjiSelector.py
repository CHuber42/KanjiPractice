#create a list (kanjiset) which is filled with entries from
#a data file (kanjiList.py). Then loop over list, displaying a prompt
#for a kanji to practice. After practiced, any input pulls another kanji
#practice, until "x" is entered.

import random
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--addKanji", help="add a string to the kanji library.", nargs="*")


args = parser.parse_args()

if args.addKanji:
    with open("kanjiList.py", 'a') as k:
        for i in sys.argv[2:]:
            k.write(i + ",\n")

else :

    #Create empty set globally; going to write to it in one func
    #and loop over it in another func, so don't want it as a local
    kanjiset = []

    with open("kanjiList.py", "r") as k: # Populate kanjilist from file
        for line in k:
            kanjiset.append(line[:-2]) # Last 2 chars of each line are ",\n"

    while True: # "Display a random Kanji" loop, until user decides they're done
        print(random.choice(kanjiset))
        if input() == "x":
            break
