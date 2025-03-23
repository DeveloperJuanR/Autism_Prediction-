# Autism_Prediction Data

# We Fetched the DNA Sequence for Autism using a common Database
from Bio import Entrez, SeqIO
Entrez.email = "your_email@example.com"  # Replace with your email
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="NM_030627.4")
recs = list(SeqIO.parse(handle, "genbank"))
handle.close()

# Checks if any records were retrieved
if recs:
    autism_dna = recs[0].seq
    print(f"Our Sequence for autism is:\n{autism_dna}")
else:
    print("No records found. Check the accession number or database parameters.")




print("-------------------------------------------------------------------")
print("----------------- WELCOME TO AUTISM PROTEIN ANALYSIS---------------")
print("-------------------------------------------------------------------")


print("Here is the analysis of the Autism DNA Data:")
# Tells us the length of our DNA Sequence 
print(f'- Total Nucleotides: {len(autism_dna)}')

# Molecular weight 
from Bio.SeqUtils import molecular_weight
print(f"- Our Molecular Weight is:", molecular_weight(autism_dna) )

#GC content - higher GC content implies more stable molecule ---------------
def gc_content (seq):
    return round ((seq.count("G") + seq.count("C")) / len(seq) * 100, 6)
print(f"- GC Content:", gc_content(autism_dna))
percent_gc = ((gc_content(autism_dna) / len(autism_dna)) * 100)
print(f"- Percent GC: {round(percent_gc,2)} %")
if percent_gc > 0.60:
  print("- Based on GC % this molecule is very stable")
elif percent_gc > 0.40:
  print("- Based on GC % this molecule is moderate stable")
else:
  print("- Based on GC % this molecule is not  stable")

# Transcription DNA -> RNA 
def transcription(seq):
  return seq.replace("T", "U")
print("- DNA/RNA Transcription: " + transcription(autism_dna)) # Turned DNA -> RNA


# Makes a chart graphing all the Nucleotides in a table:
print("- Nucleotide Frequency Data Results:")
count_nucleotides = {
    'A': autism_dna.count('A'),
    'T': autism_dna.count('T'),
    'C': autism_dna.count('C'),
    'G': autism_dna.count('G')
}
import matplotlib.pyplot as plt
width = 0.5
plt.bar(count_nucleotides.keys(), count_nucleotides.values(), width, color=['b', 'r', 'm', 'c'])
plt.xlabel('Nucleotide')
plt.ylabel('Frequency')
plt.title('Nucleotide Frequency')
