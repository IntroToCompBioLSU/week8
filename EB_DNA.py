#! /usr/bin/python
#program expects a DNA Sequence of letters
#will work as a word count function for every letter in a string
def count_dict(mystring):
    count = {}
# count
    for word in mystring: 
        count[word] = mystring.count(word)
# prints in order a-c-g-t
    for letter in sorted(count):
        print (letter + ': ' + str(count[letter]))
mystring = input("Enter Your DNA Sequence: ")
count_dict(mystring)