import csv
import pandas as pd
import os
import re

def read_fasta(fasta_file: str='human_notch.fasta'):
    """
    Extract a DNA sequence from a FASTA file as a string

    Arguments:
      fasta_file: the path to the FASTA file to use

    Returns:
      A DNA string
    """
    # get all but the first line in the file
    lines = open(fasta_file, 'r').readlines()[1:]
    # strip lines from trailing '\n', join and return them
    return ''.join([l.strip() for l in lines])

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
        #codon_to_amino_acid = {row['Codon']:row['AA.Code'] for row in codon_reader}
        # Turn 'U's into 'T's
        codon_to_amino_acid = {row['Codon'].replace('U', 'T'):row['AA.Code'] for row in codon_reader}

    return codon_to_amino_acid

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
        list: List of startcodon positions. An entry in the list represents the position of the first base of the start codon.
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

# Translate the codon to protein (Noah)
def translate(dna_sequence: str, codon_table: dict):

    """This function translates DNA sequences into all conceivable proteins.
    Parameters:
        dna_sequence: DNA sequence
        codon_table: DNA to codon table

    Returns:
        proteins: list of all conceivable proteins that could be translated from input DNA sequence together with their associated start index in the dna sequence
    """

    proteins = []
    codon_starts = find_start_codon(dna_sequence, oof=False)

    for start_codon in codon_starts:
        protein = ''
        for i in range(start_codon, len(dna_sequence), 3):
            codon = dna_sequence[i:i + 3]
            amino_acid = codon_table[codon].upper()

            if amino_acid != 'STOP':
                protein += amino_acid
            else:
                proteins.append((start_codon, protein))
                break

    return proteins

# Tie all together (Jacqueline)
def codon2protein(fasta_input: str, codon_csv: str, output: str):
    """
    Generate all proteins out of the DNA sequence contained in a FASTA file
    according to the codon table from a given csv file.
    Writes the results as csv in a file at the given output path.

    Arguments:
        fasta_input: the path to a FASTA file containing a DNA sequence
        codon_csv: the path to a csv file containing a codon table
        output: the path to the file to write the csv results
    """

    # read dna sequence from input fasta file
    dna_sequence = read_fasta(fasta_input)
    # read codon table from input csv file
    codon_table = read_codon_table(codon_csv)

    # translate dna to proteins
    indexed_proteins = translate(dna_sequence, codon_table)

    #create empty dataframe for appending to
    df = pd.DataFrame(indexed_proteins, columns=['start_codon_index', 'translated_peptide'])
    #augment df with protein sizes
    df['translated_peptide_length'] = df['translated_peptide'].apply(len)
    #check structure of df
    print(df)
    # write output
    df.to_csv(output, index=False)

if __name__ == '__main__':
    codon2protein('human_notch.fasta', 'codon_table.csv', 'human_notch_translated_peptides.csv')
