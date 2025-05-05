# Title: Exam 4 K-mer Analysis Tool

# Course and Semester: DSP 439, Spring 2025

# Author: Valerie MacDonald

# Project Description:
This tool analyzes DNA sequences by breaking them into k-mers (substrings of length k) and counting how often each k-mer appears and which characters follow them. The user can input what length the kmer is, in the terminal when running the file. 

# Usage
python V.M.Exam4.py <fasta_file> <k>
  `<fasta_file>` is the path to a FASTA format file containing DNA sequences 
  `<k>` is the length of k-mers to analyze

# Output:
The tool generates a tab-delimited text file with the following columns:
1. K-mer sequence
2. Total count of the k-mer
3. Following characters and their frequencies

# Testing:
Run the tests with pytest:
pytest test_kmer_analyzer.py
