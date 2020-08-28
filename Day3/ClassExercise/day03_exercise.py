## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
    word_list = [i for i in word]
    vowels = ['a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E']
    vowelCount = 0
    for i in vowels:
        vowelCount += word_list.count(i)
    return vowelCount
