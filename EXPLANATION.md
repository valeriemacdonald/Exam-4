## Data Structures Used (dictionaries)
**Dictionary for K-mer Counts (kmer_counts)**:
This dictionary stores the count of each k-mer (k) that is found in the DNA sequences. The key is (k) and the value is the count of occurences of the k-mer across the sequences. 
{'ATG': 5, 'GCT': 3, 'TGA': 4}

**Dictionary for Following Character Frequencies (following_chars)**:
This dictionary stores the frequency of DNA bases (A, C, G, T) that appear directly after each k-mer in the sequence. The key is (k) and the value is another dictionary with the four DNA bases aa keys. Included are their corresponding counts as values. 
{'ATG': {'A': 2, 'C': 1, 'G': 0, 'T': 2}, 'GCT': {'A': 0, 'C': 2, 'G': 1, 'T': 0}}

## Handling Edge Cases
**First k-mer in a sequence**:
Counting it and then tracking what character comes after. No special handling because it loops through sequence from start

**Last k-mer in a sequence**:
Needs special attention. We count it but do not add anything to the "following_chars" dictionary

**Short sequences**
If the sequence is shorter than k, no k-mers will be generated

## Avoiding Overcounting or Missing Context
**Clear separation of counting logic**
Each k-mer is considered exactly once in each sequence.
for i in range(len(sequence) - k):
    kmer = sequence[i:i+k]
    kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1

**Proper sequence parsing**
FASTA file reader properly separates header lines from sequence data

**Careful index handling**
K-mer indices stay within the sequence bounds
next_char = sequence[i+k]
following_chars[kmer][next_char] += 1

**Special handling for the last k-mer**
The last k-mer in each sequence is counted, but without trying to find a non-existent following character
