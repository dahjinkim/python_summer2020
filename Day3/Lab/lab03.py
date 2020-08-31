import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int

## make all characters capitalized
def shout(txt):
	if type(txt) in [int, float]:
			raise TypeError(" Input should be a str.")
	else:
		return txt.upper()
# shout("shhhh")
# shout(1234)

## reverse all characters in string
def reverse(txt):
	if type(txt) in [int, float]:
		raise TypeError(" Input should be a str.")
	else:
		return txt[::-1]
# reverse("krow")
# reverse(222)

## reverse word order in string
def reversewords(txt):
	if type(txt) in [int, float]:
		raise TypeError(" Input should be a str.")
	else:
		sentence = txt.split()[::-1]
		return ' '.join(sentence)

# reversewords("it did we")

## reverses letters in each word
def reversewordletters(txt):
	if type(txt) in [int, float]:
		raise TypeError(" Input should be a str.")
	else:
		re_txt = reverse(txt)
		return reversewords(re_txt)
		#sentence = txt.split()
		#for i in sentence:
		#	 = reverse(i)
		#return ' '.join(re_sentence)
# reversewordletters("we did it")

## change text to piglatin.. google it!
# See: https://www.wikihow.com/Speak-Pig-Latin
def piglatin(txt):
	if type(txt) in [int, float]:
		raise TypeError(" Input should be a str.")
	else:
		txt = txt.lower()
		new_txt = [i for i in txt]
		if new_txt[0] not in ["a", "e", "i", "u", "o"]:
			pig_txt = new_txt.pop(0)
			new_txt.append("-" + pig_txt + "ay")
		else: new_txt.append("-yay")
		return ''.join(new_txt)
# piglatin("Hello")
# piglatin("BOOO")
# you need to have a different condition when the word begins with a vowel

## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.

# string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

# for i in string_list:
#	try:
#		print("\tThis execution for: {}".format(i))
#		print("shout: " + shout(i))
#		print("reverse: " + reverse(i))
#		print("reversewords: " + reversewords(i))
#		print("reversewordletters:" + reversewordletters(i))
#		print("piglatin: " + piglatin(i))
#	except TypeError:
#		print("Type error. Input must be str.")
