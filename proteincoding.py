#!/usr/bin/env python
#This script selectes between translation or random draw of a sequence 

# DB: Most lines should not be indented.


print ("Type 1 for translation or 2 for random codon selection.")
options = input("1. Translation reinput sequence: \n -or- 2. Random selection reinput sequence: ")

#for those who selected 1
# if options == 1:		# DB: Missing colon here, also need two equals signs
# 	AminoSequence = []	# DB: This will write over the sequence you read in.
# 	AminoSequence = AminoSequence [::-1]	# DB: Don't need to reverse sequence for translation

#Create complement strand		# DB: You don't need to create the complement sequence to do translation.
# if i == ("A"):		# DB: Missing colon here, also need two equals signs
# 	AminoSequence.append ("T")
# if i = ("T"):		# DB: Missing colon here, also need two equals signs
# 	AminoSequence.append ("A")
# if i = ("C"):		# DB: Missing colon here, also need two equals signs
# 	AminoSequence.append ("G")
# if i = ("G"):		# DB: Missing colon here, also need two equals signs
# 	AminoSequence.append ("C")
# print (AminoSequence)

if options == 1:
	Aminosequence = input("Please enter your DNA sequence:")	# DB: Need parentheses here
	Aminosequence = Aminosequence.upper()

	#This transcripts DNA to RNA
	AminoSequence.replace("T","U")
	RNA = AminoSequence

#This creates codon
	Codon = [RNA[i:i:3]] for i in range(0, len(RNA), 3)	# Need to fix this syntax
	print(Codon)

#List of Codon to protein
	CodonToAA = { "UUU":"PHE","UUC":"PHE","UUA":"LEU","UUG":"LEU","UCU":"SER","UCC":"SER","UCA":"SER","UCG":"SER","UAU":"TYR","UAC":"TYR","UAA":"STOP","UAG":"STOP","UGU":"CYS","UGC":"CYS","UGA":"STOP","UGG":"TRP","CUU":"LEU","CUC":"LEU","CUA":"LEU","CUG":"LEU","CCU":"PRO","CCC":"PRO","CCA":"PRO","CCG":"PRO","CAU":"HIS","CAC":"HIS","CAA":"GLN","CAG":"GLN","CGU":"ARG","CGC":"ARG","CGA":"ARG","CGG":"ARG","AUU":"ILE","AUC":"ILE","AUA":"ILE","AUG":"MET-or-START","ACU":"THR","ACC":"THR","ACA":"THR","ACG":"THR","AAU":"ASN","ACC":"ASN","AAA":"LYS","AAG":"LYS","AGU":"SER","AGC":"SER","AGA":"ARG","AGG":"ARG","GUU":"VAL","GUC":"VAL","GUA":"VAL","GUG":"VAL","GCU":"ALA","GCC":"ALA","GCA":"ALA","GCG":"ALA","GAU":"ASP","GAC":"ASP","GAA":"GLU","GAG":"GLU","GGU":"GLY","GGC":"GLY","GGA":"GLY","GGA":"GLY","GGG":"GLY"}
	
	# DB: Here you could use the library you defined to translate the sequence to amino acids

#for those who selected 2
if options == 2:	# DB: Option 2 should randomly select a codon, not translate


# DB: I see the beginnings of what you were trying to do, but there are quite a few syntax
#     errors and some flow problems.