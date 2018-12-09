#!/usr/bin/env python


######## Jacob Searight : Jacobssearight : Biol4800 : Week 8 Assignment : 10.16.18

######## The goal of this code is to give the user two options based on typing the number 1, or anything else; therefore, only 1 and 2 should be entered into the code. The two options are to 1: translate a DNA sequence into amino acids (single letter) or 2: randomly draw a codon from said dna sequence.
######## The DNA sequence should be entered after selecting your option. 

######## To receive input command
print("Would you like to... 1: turn your DNA sequence into an amino acid sequence, or 2: randomly select a codon from a DNA sequence.")
command = input()
DNAseq = input("Enter the DNA sequence (caps): ")

######## The codon dictionary was copied and pasted from an internet source (https://www.biostars.org/p/2903/).
######## For the codon translation table, all thymine nucelic acids must be replaced with uracil.
RNAseq = DNAseq.replace("T","U")

codon = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
	"UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
	"UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
	"UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
	"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
	"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
	"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
	"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
	"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
	"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
	"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
	"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
	"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
	"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
	"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
	"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}


######## the sequence stored in variable DNAseq is now RNAseq, we now need to read every three RNA bases and match them to a codon, contained in the variable DNAcodon. A for loop is used. 
DNAcodon = ""
for base in range(0, len(RNAseq), 3):
	if RNAseq[base:base+3] in codon:
		DNAcodon += codon[RNAseq[base:base+3]]


######## if else statement for command 1

if command == "1":
	print ("Your DNA to Codon sequence:")
	print (DNAcodon)



######## if else statement for command 2
if command == "2":
	import random
	rDNAcodon = random.choice(DNAcodon)
	print ("A random codon from your DNA sequence:")
	print (rDNAcodon)
