#!/usr/bin/env python
# DB: I adjusted shebang line again.

#Amino Acid Translation Dictionary
aminoAcids = {"AAA":"Lysine ", "AAC":"Asparagine ", "AAG":"Lysine ", "AAU":"Asparagine ", 
"ACA":"Threonine ", "ACC":"Threonine ", "ACG":"Threonine ", "ACU":"Threonine ", 
"AGA":"Arginine ", "AGC":"Serine ", "AGG":"Arginine ", "AGU":"Serine ", 
"AUA":"Isoleucine ", "AUC":"Isoleucine ", "AUG":"Methionine ", "AUU":"Isoleucine ", 
"CAA":"Glutamine ", "CAC":"Hisdadine ", "CAG":"Glutamine ", "CAU":"Hisdadine ", 
"CCA":"Proline ", "CCC":"Proline ", "CCG":"Proline ", "CCU":"Proline ", 
"CGA":"Arginine ", "CGC":"Arginine ", "CGG":"Arginine ", "CGU":"Arginine ", 
"CUA":"Leucine ", "CUC":"Leucine ", "CUG":"Leucine ", "CUU":"Leucine ", 
"GAA":"Glutamate ", "GAC":"Aspartate ", "GAG":"Glutamate ", "GAU":"Aspartate ", 
"GCA":"Alanine ", "GCC":"Alanine ", "GCG":"Alanine ", "GCU":"Alanine ", 
"GGA":"Glycine ", "GGC":"Glycine ", "GGG":"Glycine ", "GGU":"Glycine ", 
"GUA":"Valine ", "GUC":"Valine ", "GUG":"Valine ", "GUU":"Valine ", 
"UAA":"Stop ", "UAC":"Tyrosine ", "UAG":"Stop ", "UAU":"Threonine ", 
"UCA":"Serine ", "UCC":"Serine ", "UCG":"Serine ", "UCU":"Serine ", 
"UGA":"Stop ", "UGC":"Cysteine ", "UGG":"Tryptophan ", "UGU":"Cysteine ", 
"UUA":"Leucine ", "UUC":"Phenylalanine ", "UUG":"Leucine ", "UUU":"Phenylalanine "}
print ("Choose an option:")
option = input("(1) translate a protein-coding nucleotide sequence to amino acids \n -or- (2) randomly draw a codon from sequence \n OPTION#: ")
dna = input("Please enter your DNA sequence: ")
dna = dna.upper()  
rna=dna.replace("T","U")
#option 1
if option == "1":
	# translating codons to amino acids
	protein = ""
	for n in range(0, len(rna), 3):
		if rna[n:n+3] in aminoAcids:
			protein += aminoAcids[rna[n:n+3]]
	print("Protein sequence: ")
	print(protein)
#option 2 
elif option == "2":
	code = [dna[i:i+3] for i in range(0, len(dna), 3)]
	import random
	codon = random.choice(code)
	print(codon)
	
# DB: Very good! Again, I'd suggest more spacing and a bit more commenting to keep things
#     organized and clear.