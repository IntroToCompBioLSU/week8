#!/usr/bin/env python

DNASeq= input("Enter DNA Sequence to Generate Reverse Complement: ")

#Convert Seq to upper
DNASeq= DNASeq.upper()
print("This is the Original Strand:", end= " ")
print(DNASeq)

#Converting:
DNASeq= DNASeq.replace("A", "t").replace("T", "A").replace("C", "g").replace("G", "c")
DNASeq= DNASeq.upper()	# DB: Creative, I like this approach.
print("This is the complement strand: ", end= " ")
print (DNASeq)

#Reversing:
ReverseDNA= DNASeq [::-1]
print("This is the Reverse complement strand: ", end= " ")
print(ReverseDNA)

# DB: Looks good overall.

#print(DNASeq.replace("A", "T"))
#elif DNASeq == "C":
        # print(DNASeq.replace("G", "G"))
#elif DNASeq == "G":
        # print(DNASeq.replace("G", "C"))
#elif DNASeq == "T":
        # print(DNASeq.replace("T", "A"))
#else:
        # print("This is not a valid entry!")
