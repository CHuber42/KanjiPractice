# Kanji Practice Randomizer

### This tool tracks the dictionary of Kanji you've entered, and assigns one at random to practice.

#### By _Christopher Huber_
[Link](https://github.com/CHuber42/KanjiPractice) to the GitHub repository where
this is stored.

## Operational Environment:

kanjiList.py contains a list of entries (newline separated values) from which you
would like to generate random prompts from, in the form of:

"Prompt", "Kanji Character",

For more details on this prompt structure, see Update 2.

## Usage:

From command line:
RanKanjiSelector.py will engage the random-prompt version of the tool.

The optional flag "--addKanji" "arg1" "arg2" . . . "argN" will add the arguments
to the kanjiList.py file. That is, it adds new entries to your personalized library
of Kanji to practice.

During the operational loop of the tool, you will be prompted. Valid inputs are:
* 'r' : Remove this entry from the list (ex: done practicing this Kanji; see update 1)
* 's' : Show the corresponding Kanji character for this prompt (ex: can't remember what to practice; see update 2)
* 'i' : Invert between english prompt and kanji prompt (write practice vs read practice; see update 2)
* 'x' : Exit the tool
* Any other entry (or none): Grab a new practice prompt (loop)


### Updates:

##### Update 2: 's', 'i'

Major implementation change to the working environment:
Firstly, each line in the prompting file (kanjiList.py in my case) now has the corresponding
CKJ character on it. The format of each line is:

"prompt of choice in english", "CKJ character","\n"

This interacts with a few moving pieces:

1.
* 's' at prompt will show the kanji you're supposed to practice, if you've forgotten it
* 'i' at prompt will invert the prompt, to display the kanji instead of the prompt (to help with reading instead of writing)
* 'i' again will re-invert the prompt (return it to its default state)

2.
* In order to properly display the character, your shell must be capable of displaying utf-8 chars
  in standard powershell for win-10 this can be done by switching to a compatible font.

3.
* The functionality to include the Kanji character in --addKanji mode is untested;
  this means, for now, adding new lines to the prompt file can be done either fully manual or
  partially with --addKanji and then manually adding the kanji character.


##### Update 1: --addKanji, 'r'

addKanji.py "entry1" "entry2" ... has been deprecated.
This functionality is now packaged inside the main file using flag:        
"--addKanji".
ex:
RanKanjiSelector.py --addKanji "thing to add" "another thing to add".

__arg can be any text prompt you wish, be it "go" or "go (as in 'after')",
for clarification! HOWEVER, because of update 2 using CSVs to parse entries,
DO NOT include commas in your prompt!
OK: "thing/as in an object"
NOT OK: "thing, as in an object"__

Also new: At prompt, 'r' will remove the entry from the prompt list. Designed
to help focus energy on new entries and less on previously-mastered entries.

### Possible support for the future:


* Add func to remove mastered Kanji from the prompt file
