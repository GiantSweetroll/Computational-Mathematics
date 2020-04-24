#Muhammad Rifqi Dwi Budianto
#31058833


nucleotides = {'A', 'C', 'G', 'T'}
#pairs: {G, C} and {A, T}


#Question 1A
def checkSequence(dnaMolecule):
    if dnaMolecule != '':   #To check if the dnaMolecule string is empty
        for i in dnaMolecule:   #Loops through each character in dnaMolecule
            if (i not in nucleotides): #Check if the character doesn't exist in nucleotides
                return False
    
    else:
        return False
    return True
#Question 1B
def complement(dnaStrand):
    complement = ''
    
    for i in dnaStrand: #loops through each character in dnaStrand
        #Check for character and assign it its opposite partner to complement variable
        if i == 'A':
            complement += 'T'
        elif i == 'T':
            complement += 'A'
        elif i == 'G':
            complement += 'C'
        else:   #C
            complement += 'G'
    
    return complement

#Question 1C
def mostRepeated(dnaMolecule, sequence):
    if (sequence not in dnaMolecule):   #Check if sequence exists in dnaMolecule
        return -1
    else:
        chains = []     #list to store the number of chains in every iteration
        index = -1      #to be used to access the 'chains' list
        seqLen = len(sequence)  #Length of the sequence
        
        #loop through dnaMolecule
        for i in range(len(dnaMolecule)):
            sub = dnaMolecule[i : i + seqLen]   #Get the word in current iteration
            if (sub == sequence):   #Check if the word equals to the sequence
                index += 1
                prevSub = sub   #Used to check if chain is broken
                #Loop through dnaMolecule again, this time in seqLen increments
                for j in range(i, len(dnaMolecule), seqLen):
                    sub = dnaMolecule[j : j + seqLen]
                    if (sub == sequence and sub == prevSub):    #Making sure chain is not broken
                        #If chain in current index doesnt exit, make it
                        if (index >= len(chains)):
                            chains.append(1)
                        else:
                            chains[index] += 1
                    prevSub = sub
        
        #Return longest
        longest = 0
        for i in chains:
            if i > longest:
                longest = i
        
        return longest

#Question 1D
def firstNonRepeated(dnaMolecule,size):
    used = []   #Used to store words that have been checked before
    
    for i in range(len(dnaMolecule)):
        sub = dnaMolecule[i : i + size]
        #Check for duplicates of sub
        if sub not in dnaMolecule[i+size:] and sub not in used:
            if (len(sub) == size):  #To make sure sub has the same length as 'size'
                return sub
            else:
                return -1
        else:
            #Add the word with duplicate to the 'used' list
            if (sub not in used):
                used.append(sub)
    
    return -1

#Question 1E
def longestSequence(dnaMolecule,sequence):
    chains = []
    indexes = []
    
    #Find the indexes of the occurrence of 'sequence'
    for i in range(len(dnaMolecule)):
        if (dnaMolecule[i : i + len(sequence)] == sequence):
            indexes.append(i)
    
    #Create chains using the indexes
    index = 0
    for i in indexes:
        chains.append(dnaMolecule[index : i + len(sequence) - 1])   #slice dnaMolecule up to the second last characters of 'sequence'
        index = i+1
    chains.append(dnaMolecule[index:])  #append the remaining chain
    
    #Find longest chain
    longest = ''
    for chain in chains:
        if len(chain) > len(longest):
            longest = chain
    
    return longest
