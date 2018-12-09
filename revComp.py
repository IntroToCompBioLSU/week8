#!/usr/bin/env python

# input DNA sequence in all caps
complement = []
dnaSeq = input ("Input DNA sequence in all capital letters: ")

#reverses DNA sequence that user inputs
dnaSeq = dnaSeq[::-1]

#create compliment of dna Sequence
for i in dnaSeq:
	if i == "A":
		complement.append("T")
	elif i == "C":
		complement.append("G")
	elif i == "T":
                complement.append("A")
	elif i == "G":
                complement.append("C")


#converts list to a string
str = ''.join(complement)
print("reverse complement: ") 
print(str)
