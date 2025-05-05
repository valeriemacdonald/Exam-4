#Parse genome sequence fragments from a file
#Analyze k-mers (substrings of length k) and what comes after them
#Output the frequency of each k-mer and the frequency of characters following each k-mer
#Write well-documented, tested code with multiple functions

#/mnt/homes4celsrs/shared/439539/reads.fa
#/python - exam4 for the file i created
#python ./V.M.Exam4.py /mnt/homes4celsrs/shared/439539/reads.fa 3

import sys

def read_fasta_file(filename):
    """
    Read the FASTA file and extract sequences
    Arguments: filename (str). which is the path to the FASTA file
    Returns: list of DNA sequences (str) from the file given
    """
    sequences = [] #store the sequences
    current_sequence = "" #builds the current sequence from nothing
    
    #open file and process it line by line
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('>'):
                # Found a header line, save the previous sequence if it exists
                if current_sequence:
                    sequences.append(current_sequence)
                current_sequence = "" #resets to nothing for next sequence
            else:
                current_sequence += line.strip() #adding the new sequence data to the current sequence, and removes any whitespace
        
        #add last sequence when end of file is reached       
        if current_sequence:
            sequences.append(current_sequence)
            
    return sequences
  
#Generate all k-mers possible from a sequence
#Arguments: DNA sequence (str) and k (int). it's the length of each k-mer
#Returns: the list of k-mer strings
def generate_kmers(sequence, k):
    kmers = [] #list that stores all of the k-mers
    #uses whatever the range of K is and sections off sequence areas
    for i in range(len(sequence) - k + 1):
        # Extract the k-mer at the current position
        kmer = sequence[i:i+k]
        kmers.append(sequence[i:i+k])
    return kmers
 
#Count k-mers and their following characters
#Arguments: DNA sequence (str) and k (int)
#Returns: dictionary of k-mer counts and a dictionary of following character frequencies per k-mer
def analyze_kmer_count(sequences, k):
    kmer_counts = {} #dictionary to store counts
    following_chars = {} #dictionary to store counts
    
    #processing!
    for sequence in sequences:
        # Process all k-mers except the last one (which has no following character)
        for i in range(len(sequence) - k):
            #extract current k-mer
            kmer = sequence[i:i+k]
            #Get the character that follows this k-mer
            next_char = sequence[i+k]
            # Count k-mer and update its count
            if kmer in kmer_counts:
                kmer_counts[kmer] += 1 # Increment if we've seen it before
            else:
                kmer_counts[kmer] = 1 # Initialize if it's new
             # Count following character
            if kmer not in following_chars:
                # Initialize counts for all possible DNA bases
                following_chars[kmer] = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
            following_chars[kmer][next_char] += 1 # Increment the count for the specific following character
            
        # Handle the last k-mer in the sequence
        last_kmer = sequence[-k:]
        # Update the count for the last k-mer
        if last_kmer in kmer_counts:
            kmer_counts[last_kmer] += 1
        else:
            kmer_counts[last_kmer] = 1
            
    return kmer_counts, following_chars
  
 #Write results to a file
#Arguments: kmer_counts (dict), following_chars (dict), output_file (str). The last is a path to the output file
#Returns: None
def write_results_to_file(kmer_counts, following_chars, output_file): 
    with open(output_file, 'w') as file:
        # Write the header line
        file.write("K-mer\tTotal Count\tFollowing Characters\n")
       
    # Process each k-mer in alphabetical order 
        for kmer in sorted(kmer_counts.keys()):
            file.write("{}\t{}\t".format(kmer, kmer_counts[kmer]))
            # If this k-mer has following characters, write those too
            if kmer in following_chars:
                follow_str = ", ".join(["{}:{}".format(char, count) for char, count in following_chars[kmer].items() if count > 0])
                file.write(follow_str)
            
            #end the line
            file.write("\n")
    
 #Coordinate the program flow. Handles command-line args, processes file, performs analysis, and then writes the result to the file
#Arguments: none
#Returns: none
def main():
# Check if the correct number of command line arguments were provided
    if len (sys.argv) != 3:
        print("Usage: python kmer_analyzer.py <fasta_file> <k>")
        sys.exit(1) # Exit with error code

     # Parse command line arguments       
    fasta_file = sys.argv[1] # First argument is FASTA file path
    k = int(sys.argv[2]) #second argument is k-mer size (convert to int)
    # Create output filename based on k value
    output_file = "kmer_results_k{}.txt".format(k)
    
    sequences = read_fasta_file(fasta_file)
     # Count k-mers and their following characters
    kmer_counts, following_chars = analyze_kmer_count(sequences, k)
    write_results_to_file(kmer_counts, following_chars, output_file)
    
    print("Analysis complete. Results written to {}".format(output_file))

#Ensures that the main function is only executed when the script is run directly (not when imported as a module) 
if __name__ == "__main__":
    main()