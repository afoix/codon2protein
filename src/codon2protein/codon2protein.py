import csv
import pandas as pd
import os
import re

#  Read input file (FASTA) and remove the header (Nick)
def read_fasta(fasta_file):
    # I created a folder on my Desktop called 'codon2protein'
    # This folder contains the 'human_notch.fasta' file
    # Depending on the folders you have to change the path

    # Define the path to the FASTA file
    fasta_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'codon2protein', 'human_notch.fasta')
    
    # Check if the file exists
    if os.path.exists(fasta_file_path):
        # Read the contents of the file
        with open(fasta_file_path, 'r') as fasta_file:
            lines = fasta_file.readlines()
    
        # Remove the header from the FASTA file
        sequence_lines = []
        for line in lines:
            if not line.startswith('>'):  # Remove lines starting with '>'
                sequence_lines.append(line.strip())
    
        # Concatenate the lines to form the sequence
        sequence = ''.join(sequence_lines)
    
        # Print or use the sequence as needed
        print(sequence[:100])

else:
    print("The file does not exist.")
    
# Find start codons in the sequence (Daniel)
def find_start_codon(fasta_string: str, first=False, oof=True) -> list:
    """identify start codons in the provided fasta string

    Args:
        fasta_string (str): string of DNA nucleotides
        first (bool, optional): If false, returns the position of all start codons in the string.
        If true, returns only the first observation of the start codon. Defaults to False.
        oof(bool, optional): If true, keeps all found start codons. If false, removes all codons that do not
        align with the first starting base of the fasta string.
    Returns:
        list: List of startcodon positions. An entry in the list represents the position of  the first base of the start codon.
    """
    # apply regex search on string to find all start codons
    scodons=[c.start() for c in re.finditer(pattern="ATG", string = fasta_string)]

    # remove out of frames codons if wanted
    if oof==False:
        scodons = [s for s in scodons if s%3==0]

    # remove all but the first start codon
    if first == True:
        return [scodons[0]]
    else:
        return scodons
    

# Read codon_table.csv and create a dictionary (Anna)
def read_codon_table(codon_table='codon_table.csv'):
    """
    Create a dictionary that maps RNA codons to amino acids.

    Constructs dictionary by reading a .csv file containing codon to amino
    acid mappings.

    Arguments:
        codon_table (string, optional): path to the .csv file containing
            codon to amino acid mappings. Assumed column structure is
            'Codon', 'Amino Acid Abbreviation', 'Amino Acid Code', and
            'Amino Acid Name'. Default is 'codon_table.csv'
    Returns:
        (dictionary, string:string): dictionary with codons as keys and
            amino acid codes as values.
    """
    
    codon_to_amino_acid = {}
    
    with open(codon_table, 'r') as file:
        codon_reader = csv.DictReader(file)
        codon_to_amino_acid = {row['Codon']:row['AA.Code'] for row in codon_reader}
        
    return codon_to_amino_acid
      

# Translate the codon to protein (Noah)
def translate(fasta_file, codon_table):

    """This function translates DNA sequences from FASTA files into all conceivable proteins.

    #Parameters:
    #    fasta_file: FASTA file DNA sequence
    #    codon_table: DNA to codon table

    #Returns:
    #    proteins: list of all conceivable proteins that could be translated from input DNA sequence
    """
    
    sequences = read_fasta(fasta_file)
    proteins = []

    codon_starts = find_codon_start(sequence)

    for start_codon in codon_starts:
        protein = ''
        for i in range(start_codon, len(sequence), 3):
                
            codon = sequence[i:i + 3]
            amino_acid = codon_table.get

            if amino_acid != 'STOP':
                protein += amino_acid
            else:
                proteins.append(protein)
                break

    return proteins

# Tie all together (Jacqueline)
def main(fasta_input, fasta_output): 

    #create empty dataframe for appending to
    data = {"start_codon_index": [], "translated_peptide": []}
    fasta_output = pd.DataFrame(data)
    #check structure of df
    print(fasta_output)

    #RUN THE FOLLOWING ONCE
    # run import fasta
    # run read codon table

    #RUN THE FOLLOWING (likely in for loop, depends on implementation)
    # run find start codon (Daniel) -- output is (ideally, list of) start codon indexes
    # run translate codon to AA (Noah) -- output is (ideally, list of) translated codons

    # append input to dataframe, assuming proteins and codons are lists
    for i in 0..len(proteins):
        fasta_output=fasta_output.append({"start_codon_index": [codons[i]], "translated_peptide": [proteins[i]]},ignore_index=True)
    
    return(fasta_output) 
