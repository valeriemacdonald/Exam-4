# Exam 4 K-mer Analysis Tool
This tool analyzes DNA sequences by breaking them into k-mers (substrings of length k) and counting how often each k-mer appears and which characters follow them.

##Usage
python V.M.Exam4.py <fasta_file> <k>
  `<fasta_file>` is the path to a FASTA format file containing DNA sequences 
  `<k>` is the length of k-mers to analyze

## Output
The tool generates a tab-delimited text file with the following columns:
1. K-mer sequence
2. Total count of the k-mer
3. Following characters and their frequencies

## Testing
Run the tests with pytest:
pytest test_kmer_analyzer.py
