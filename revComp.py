#!/usr/bin/env python

# input DNA sequence in all caps
complement = []
dnaSeq = input ("Input DNA sequence in all capital letters: ")
dnaSeq = dnaSeq.upper()

#reverses DNA sequence that user inputs
dnaSeq = dnaSeq[::-1]

#create compliment of dna Sequence
for i in dnaSeq:
	if i == "A":
		complement.append("T")
	elif i == "C":
		complement.append("G")
	elif i == "T":
		complement.append("A")		# DB: Best to keep indentation style the same
	elif i == "G":
		complement.append("C")


#converts list to a string
str = ''.join(complement)		# DB: It's good practice to avoid generic variable names
print("reverse complement: ")	#     like 'str'. Maybe use 'revComp'?
print(str)

# DB: Good! You could make it a little more general by using .upper() to automatically
#     convert the sequence to uppercase (see above)