#! /usr/bin/python
#will reverse anything 
mystring = input("Enter Your DNA Sequence: ")
#converts to lowercase
mystring = mystring.lower()
#makes complimentary strand
mystring = mystring.replace("c", "G")
mystring = mystring.replace("g", "C")
mystring = mystring.replace("a", "T")
mystring = mystring.replace("t", "A")
#print everse order
print(mystring[::-1])