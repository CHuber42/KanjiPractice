import random

kanjiset = []

with open("kanjiList.py", "r") as k:
    for line in k:
        kanjiset.append(line[:-2])

while True:
    print(random.choice(kanjiset))
    if input() == "x":
        break
