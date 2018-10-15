#!/usr/bin/env python

# Present option menu to users//user should type number w/o puncuation
# (1) translate a protein-coding nucleotide sequence to amino acids -or- 
# (2) randomly draw a codon from the sequence  

print ("CHOOSE FROM OPTIONS BELOW BY TYPING OPTION NUMBER:")
option = input("(1) translate a protein-coding nucleotide sequence to amino acids \n -or- (2) randomly draw a codon from sequence \n OPTION#: ")

# if else statement to complete OPTION#1
if option == "1":
    dnaSeq = input("Enter DNA sequence here in all caps: ")

# transcribe dna sequence to rna sequence 
    rnaSeq=dnaSeq.replace("T","U")
    print("Transcribed sequence: ")
    print(rnaSeq)

# setting dictionary for codon to amino acid
    codon2aa = {"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N", 
                "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T", 
                "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S", 
                "AUA":"I", "AUC":"I", "AUG":"M", "AUU":"I", 

                "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H", 
                "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P", 
                "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R", 
                "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L", 

                "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D", 
                "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A", 
                "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G", 
                "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V", 

                "UAA":"_", "UAC":"Y", "UAG":"_", "UAU":"T", 
                "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S", 
                "UGA":"_", "UGC":"C", "UGG":"W", "UGU":"C", 
                "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}

# translating rna codons to amino acids
    proteinSeq = ""
    for n in range(0, len(rnaSeq), 3):
        if rnaSeq[n:n+3] in codon2aa:
            proteinSeq += codon2aa[rnaSeq[n:n+3]]
    print("Protein sequence: ")
    print(proteinSeq)

# else statement to complete OPTION #2
# user inputs dna sequence//split dna sequence into a list of codons
else:
    dnaSeq = input("Enter DNA sequence here in all caps: ")
    codon= [dnaSeq[i:i+3] for i in range(0, len(dnaSeq), 3)]
    print(codon)

# print random codon back 
    import random
    randomCodon= random.choice(codon)
    print(randomCodon)
