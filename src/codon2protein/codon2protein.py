#import pandas for use in creating dataframe
import pandas as pd

#  Read input file (FASTA) and remove the header (Nick)
def read_fasta(fasta_file):
    """
    
    """
    return('')

# Find start codons in the sequence (Daniel)
def find_codon_start(codon):
    """
    
    """
    return('')

# Read codon_table.csv and create a dictionary (Anna)
def read_codon_table(codon_table='codon_table.csv'):
    """
    
    """
    return('')      

# Translate the codon to protein (Noah)
def translate(sequence, codon_to_amino):
    """
    
    """
    return('')

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

    # append input to dataframe, assuming codon_to_amino and codons are lists
    for i in 0..len(codon_to_amino):
        fasta_output=fasta_output.append({"start_codon_index": [codons[i]], "translated_peptide": [codon_to_amino[i]]},ignore_index=True)
    
    return(fasta_output) 
