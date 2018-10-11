#! /usr/bin/python

mystring = input("Enter Your DNA Sequence: ")
#converts to lowercase
mystring = mystring.lower()
#makes complimentary strand
mystring = mystring.replace("c", "G")
mystring = mystring.replace("g", "C")
mystring = mystring.replace("a", "T")
mystring = mystring.replace("t", "A")
#print reverse order
print("Your reverse complimentary DNA Sequence is: ")
print(mystring[::-1])