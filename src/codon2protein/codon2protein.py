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
    """
    
    """
    return('') 
