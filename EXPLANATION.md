## Data Structures Used (dictionaries)
'kmer_counts'
   - Keys are k-mer strings (e.g., "ATG")
   - Values are integers representing how many times the k-mer appears
'following_chars'
   - Keys are k-mer strings
   - Values are dictionaries with:
     - Keys: The four DNA bases (A, C, G, T)
     - Values: How many times each base follows the k-mer
    
  Used dictionaries so it was easy to look up a specific k-mer. It also updates the counts efficiently

## Handling Edge Cases
**First k-mer in a sequence**:
counting it and then tracking what character comes after

**Last k-mer in a sequence**:
count it but do not add anything to the "following_chars" dictionary

**Empty sequences**:

**Short sequences**
if sequence is shorter than k, no k-mers will be generated

## Avoiding Overcounting or Missing Context
**Clear separation of counting logic**
Each k-mer is considered exactly once in each sequence

**Proper sequence parsing**
FASTA file reader properly separates header lines from sequence data

**Careful index handling**
k-mer indices stay within the sequence bounds

**Special handling for the last k-mer**
last k-mer in each sequence is counted, but without trying to find a non-existent following character
