# to find gc count
# ((g + c)/total nucleotide)*100
##total nucleotide = A, T, G, C

dna =str(input("enter your sequence here in CAPITAL font: "))

g_count = dna.count("G")
c_count = dna.count("C")

gc_count = (g_count + c_count)
total_neucleotide = len(dna)

gc_percent = (gc_count / total_neucleotide)*100

print(f"GC percent of given DNA is: {round(gc_percent, 3)}%")

##f before string is used for formatting string while printing


a_count = dna.count("A")
t_count = dna.count("T")

at_count = (a_count + t_count)
total_neucleotide = len(dna)

at_percent = (at_count / total_neucleotide)*100

print(f"AT percent of given DNA is: {round(at_percent, 3)}%")
