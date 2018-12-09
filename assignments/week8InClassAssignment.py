#!/usr/bin/env python

#Writing python script that accepts a sequence from user and prints out the reverse complement to the screen.

dnaSeq = input("Input your DNA sequence here. ")
dnaSeq = dnaSeq.upper()
print("%s" % (dnaSeq) [::-1])  
# DB: Maybe add a few comments throughout to indicate what you're doing. For instance,
#     reversing the sequence with this line.

nuc = "A"  # DB: I don't think you need this at all.
for nuc in dnaSeq:
	if nuc == "A":
		print("T",end="")
	elif nuc == "C":
        print("G",end="")
	elif nuc == "T":
        print("A",end="")
	elif nuc == "G":
        print("C",end="")
	else:
        print("This is not a valid nucleotide!")

        	
# DB: Overall, really good! A couple suggestions: (1) You could add .upper() to the sequence
#     that's read in, to make sure it's uppercase. (2) Right now, the reverse complement
#     is printed out with a different nucleotide on each line. By adding the argument
#     end="" to the print statements, all the nucleotides will be printed on the same line.
