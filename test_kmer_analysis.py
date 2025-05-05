#TESTING SCRIPT

import pytest 
from VMExam4 import read_fasta_file, generate_kmers, analyze_kmer_count, write_results_to_file
import os 



def test_generate_kmers():
    """
    Tests the Generate_kmers function with different inputs (standard sequences, various types of edge cases)
    Uses assert to make sure the generated k-mer lists are correct
    Arguments: none
    Return: none
    """
 #simple sequence being tested
    sequence = "ATGTCTGTCTGAA"
    
    # Test with k=2
    kmers_k2 = generate_kmers(sequence, 2)
    assert kmers_k2 == ['AT', 'TG', 'GT', 'TC', 'CT', 'TG', 'GT', 'TC', 'CT', 'TG', 'GA', 'AA']
    
    # Test with k=3
    kmers_k3 = generate_kmers(sequence, 3)
    assert kmers_k3 == ['ATG', 'TGT', 'GTC', 'TCT', 'CTG', 'TGT', 'GTC', 'TCT', 'CTG', 'TGA', 'GAA']
    
    # Edge case: k = sequence length
    kmers_k13 = generate_kmers(sequence, 13)
    assert kmers_k13 == ['ATGTCTGTCTGAA']
    
    # Edge case: empty sequence
    kmers_empty = generate_kmers("", 2)
    assert kmers_empty == []
    
    #Edge case: sequence < k
    result = generate_kmers("AT", 5)
    assert result == []
    
def test_analyze_kmer_count():
    """
    Tests the analyze_kmer_count function
    Checks frequency counts and following characters. Using assert
    Arguments: none
    Return: none
    """
    sequences = ["ATGTCTGTCTGAA"]
    
    # Test with k=2
    kmer_counts, following_chars = analyze_kmer_count(sequences, 2)
    
    # Check kmer counts
    assert kmer_counts['AT'] == 1
    assert kmer_counts['TG'] == 3
    assert kmer_counts['GT'] == 2
    assert kmer_counts['TC'] == 2
    assert kmer_counts['CT'] == 2
    assert kmer_counts['GA'] == 1
    assert kmer_counts['AA'] == 1
    
    # Check following characters
    assert following_chars['AT']['G'] == 1
    assert following_chars['TG']['T'] == 2
    assert following_chars['TG']['A'] == 1
    
    # Test with k=3
    kmer_counts, following_chars = analyze_kmer_count(sequences, 3)
    assert kmer_counts['ATG'] == 1
    assert kmer_counts['TGT'] == 2
    assert following_chars['TGT']['C'] == 2
    
def test_write_results_to_file():
    """
    Tests the write_results_to_file function works correctly
    Puts a small sample of the data into the file, and then reads to check the contents match 
    Arguments: none
    Return: none
    """
    kmer_counts = {'AT': 1, 'TG': 3}
    following_chars = {
        'AT': {'A': 0, 'C': 0, 'G': 1, 'T': 0},
        'TG': {'A': 1, 'C': 0, 'G': 0, 'T': 2}
    }
    output_file = "test_output.txt"
    
    write_results_to_file(kmer_counts, following_chars, output_file)
    
    # Read the file and check content
    with open(output_file, 'r') as file:
        lines = file.readlines()
        
    assert len(lines) == 3  # Header + 2 k-mers
    assert "K-mer\tTotal Count\tFollowing Characters" in lines[0]
    assert "AT\t1\tG:1" in lines[1]
    assert "TG\t3\tA:1, T:2" in lines[2]
    
    # Clean up
    os.remove(output_file)