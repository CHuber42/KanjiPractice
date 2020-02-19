import sys

with open("kanjiList.py", 'a') as k:
    for i in sys.argv[1:]:
        k.write(i + ",\n")
