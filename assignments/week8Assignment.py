#!/usr/bin/env python

# Presenting menu of options
print ("What would you like to do? ")

# User selects option from menu
option = input("(1) Translate a protein-coding nucleotide sequence to amino acids OR (2) Randomly draw a codon from the sequence? ")

# If user selects option 1.
if option == "1":
	dnaSeq = input("Enter protein-coding nucleotide sequence here (IN ALL CAPS): ")

# Option 1: Transcription of nucleotide sequence
	rnaSeq = dnaSeq.upper().replace("T","U") # DB: Could use .upper() here.
	print("Resulting transcription sequence: ")
	print(rnaSeq)

# Creating amino acid dictionary
	AminoDic = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
		"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
		"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
		"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
		"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
		"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
		"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
		"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
		"UAU":"Y", "UAC":"Y", "UAA":"stop", "UAG":"stop",
		"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
		"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
		"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
		"UGU":"C", "UGC":"C", "UGA":"stop", "UGG":"W",
		"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
		"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
		"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
		}

# Option 1: Translation of transcription sequence
	# rnaSeq = dnaSeq.replace("T","U")
	# dnaSeq = input("Enter transcription sequence here for translation: ")
	# DB: Why ask for input again? 
	proteinSeq = ""
	# AminoDic ={}  # DB: This seems to erase your amino acid dictionary. 
	for i in range(0, len(rnaSeq), 3):
		if rnaSeq[i:i+3] in AminoDic:
			proteinSeq += AminoDic[rnaSeq[i:i+3]]
	print("Protein Sequence: ")
	print(proteinSeq)

# If user selects option 2, input nucleotide sequence
elif option == "2":
	dnaSeq = input("Enter protein-coding nucleotide sequence here (IN ALL CAPS): ")
	codon = [dnaSeq[i:i+3] for i in range(0, len(dnaSeq), 3)]
	print(codon)

# Report random codon
	import random
	ranCodon = random.choice(codon)
	print(ranCodon)

# DB: Overall, very good! Just see a few comments above.