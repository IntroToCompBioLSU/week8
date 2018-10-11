#!/usr/bin/env python

#Writing python script that accepts a sequence from user and prints out the reverse complement to the screen.

dnaSeq = input("Input your DNA sequence here. ")
print("%s" % (dnaSeq) [::-1])

nuc = "A"
for nuc in dnaSeq:
	if nuc == "A":
		print("T")
	elif nuc == "C":
        	print("G")
	elif nuc == "T":
        	print("A")
	elif nuc == "G":
        	print("C")
	else:
        	print("This is not a valid nucleotide!")
dnaSeq = ' '.join(dnaSeq)
