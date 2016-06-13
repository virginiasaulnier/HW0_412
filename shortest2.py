from Bio import Entrez
from Bio import SeqIO
Entrez.email = "virginia.saulnier@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["FJ817486 JX069768 JX469983"], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format

i=0
count = len(records)
while i != count:
    if len(records[i].seq) < len(records[i+1].seq):#if the first record's sequence is shorter than the second record do something
        records[i+1] = records[1]#make the first record the new second record
        
    elif len(records[i].seq) > len(records[i+1].seq):#else if the first record is larger, keep going
        i = i+1
        



print records[i].description#print the remaining record
print records[i].seq#print the remaining sequence
