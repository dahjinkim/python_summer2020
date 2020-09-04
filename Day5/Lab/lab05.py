import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

index = []
keyword = re.compile(r"the")
for i, line in enumerate(obama):
	if keyword.search(line):
		print(i)
		print(line)
		index.append(i)

no_the = []
for i, line in enumerate(obama):
	if i not in index:
		print(line)
		no_the.append(line)

len(no_the)


# TODO: print lines that contain a word of any length starting with s and ending with e

keyword = re.compile(r"^s[a-z]*e$")
for i, line in enumerate(obama):
	word = re.split(r'\s', line)
	for w in word:
		if keyword.search(w):
			print(line)


## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = input("Please enter a date in the format MM.DD.YY: ")
