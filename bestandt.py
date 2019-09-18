#open sequence file.
o = open("test.txt", "r")

#Reads contents of the file from left to right into a variable
seq = o.read()

#total length of the sequence
TL = (len(seq))

#count the amount of G's and C's and puts them in respecting variables
G = seq.count("G")
C = seq.count("C")
A = seq.count("A")
T = seq.count("T")

#GC% calculation: (G + C)/(total number of characters)
Total = ((G + C) / TL) * 100
TotalAT = ((A + T) / TL) * 100

print("seqeunce has a GC% OF:", (Total.__round__(2)))
print("seqeunce has a AT% of:", (TotalAT.__round__(2)))
print("Total %:", Total + TotalAT)
