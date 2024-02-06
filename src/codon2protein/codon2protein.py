import csv
#  Read input file (FASTA) and remove the header (Nick)
# def read_fasta(fasta_file):
#     """
    
#     """
#     return('')

# Find start codons in the sequence (Daniel)
# def find_codon_start(codon):
#     """
    
#     """
#     return('')

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
      

if __name__ == '__main__': 
    codon_table = read_codon_table('/Users/afoix/Git/randomstuff/eippstuff/codon2protein/src/codon2protein/codon_table.csv')
    print(codon_table)

# Translate the codon to protein (Noah)
# def translate(sequence, codon_to_amino):
#     """
    
#     """
#     return('')

# Tie all together (Jacqueline)
# def main(fasta_input, fasta_output): 
#     """
    
#     """
#     return('') 
