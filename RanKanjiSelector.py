#create a list (kanjiset) which is filled with entries from
#a data file (kanjiList.py). Then loop over list, displaying a prompt
#for a kanji to practice. After practiced, any input pulls another kanji
#practice, until "x" is entered.

import random
import sys
import argparse

kanjiset = []
invert = False

parser = argparse.ArgumentParser()
parser.add_argument("--addKanji", help="add a string to the kanji library.", nargs="*")
args = parser.parse_args()


if args.addKanji:
    with open("kanjiList.py", 'a') as k:
        for i in sys.argv[2:]:
            k.write(i + ",\n")


#Create empty set globally; going to write to it in one func
#and loop over it in another func, so don't want it as a local
with open("kanjiList.py", "r", encoding ="utf-8") as k: # Populate kanjilist from file
    for line in k:
        kanjiset.append(line)

while True: # "Display a random Kanji" loop, until user decides they're done
    selection = random.randint(0, (len(kanjiset) - 1))
    element = kanjiset[selection]
    commaloc = element.find(',')
    str1 = element[0:(commaloc)]
    str2 = element[(commaloc + 2): -2]
    if invert :
        strswap = str1
        str1 = str2
        str2 = strswap
    print(str1)

    entry = input("'x' to exit | 's' to show element | 'r' to remove Kanji from this instance | 'i' to invert: ")
    if entry == "x":
        break
    elif entry == "r" :
        del kanjiset[selection]
    elif entry == "s" :
        print(str2, "\n")
    elif entry == "i" :
        if invert :
            invert = False
        else :
            invert = True
