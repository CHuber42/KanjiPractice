#create a list (kanjiset) which is filled with entries from
#a data file (kanjiList.py). Then loop over list, displaying a prompt
#for a kanji to practice. After practiced, any input pulls another kanji
#practice, until "x" is entered.

import random
import sys
import argparse

#Global tools: kanjiset holds the prompts stripped from the prompt file (kanjiList.py)
#invert holds the state of read practice v write practice: False = write practice, True = read practice
kanjiset = []
invert = False

#Argparser to handle the addition of new entries to the prompt file (practice dictionary)
parser = argparse.ArgumentParser()
parser.add_argument("--addKanji", help="add a string to the kanji library.", nargs="*")
args = parser.parse_args()


if args.addKanji:
    with open("kanjiList.py", 'a') as k:
        for i in sys.argv[2:]:
            k.write(i + ",\n")


#Import the lines of prompts from the "dictionary file" (kanjiList.py)
with open("kanjiList.py", "r", encoding ="utf-8") as k:
    for line in k:
        kanjiset.append(line)


while True: # "Display a random Kanji" loop, until user decides they're done
    selection = random.randint(0, (len(kanjiset) - 1)) #if len = 50, addresses = 0-49
    element = kanjiset[selection]      #|
    commaloc = element.find(',')       #| These lines sub-str the prompt form from str = "str1, str2,"
    str1 = element[0:(commaloc)]       #| to "str1" "str2"; write mode prompt is held in str1, Kanji/readprompt in str2
    str2 = element[(commaloc + 2): -2] #|
    if invert :                        #Swap the strings if in "read practice" mode
        strswap = str1
        str1 = str2
        str2 = strswap
    print(str1)                        #Print the selected prompt for the selected entry

    entry = input("'x' to exit | 's' to show element | 'r' to remove Kanji from this instance | 'i' to invert: ")
    if entry == "x":        #Exit program
        break
    elif entry == "r" :     #Skip this entry for the remainder of today's practice
        del kanjiset[selection]
    elif entry == "s" :     #Show the answer to this prompt
        print(str2, "\n")
    elif entry == "i" :     #Switch between reading and writing practice modes
        if invert :
            invert = False
        else :
            invert = True
