# Kanji Practice Randomizer

### This tool tracks the dictionary of Kanji you've entered, and assigns one at random to practice.

#### By _Christopher Huber_
[Link](https://github.com/CHuber42/KanjiPractice) to the GitHub repository where
this is stored.

## Basic operation of the tool:

kanjiList.py contains the list of entries from which you would like to generate
random prompts from, in the form of comma-ended lines EG "thing,\n"

From command line:
RanKanjiSelector.py will engage the random-prompt version of the tool.
### Added in 2nd major release:
addKanji.py "entry1" "entry2" ... has been deprecated.
This functionality is now packaged inside the main file using flag:
 "--addKanji".
ex:
RanKanjiSelector.py --addKanji "thing to add" "another thing to add".

__arg can be any text prompt you wish, be it "go" or "go (as in 'after')",
for clarification!__

RanKanjiSelector.py will present a prompt. X exits program - all others
result in a new random entry.

### Possible support for the future:


* Add func to remove mastered Kanji from the practice list

* Add ability to display the Kanji at prompt, if reminder is required
(IE, a "dictionary")
