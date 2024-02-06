import pytest
from codon2protein import read_fasta, find_start_codon, read_codon_table, translate 

# Define test data
TEST_CODON_TABLE = 'test_codon_table.csv'  # Assume this is your test CSV file
TEST_FASTA_FILE = 'test_fasta.fasta'

# Example test data in test_codon_table.csv:
# Codon,Amino Acid Abbreviation,Amino Acid Code,Amino Acid Name
# TTT,Phe,F,Phenylalanine
# CTG,Leu,L,Leucine
# ATT,Ile,I,Isoleucine 

def test_create_codon_to_amino_acid_dict():
    expected_result = {'TTT': 'F', 'CTG': 'L', 'ATT': 'I'}
    result = read_codon_table(TEST_CODON_TABLE)
    assert result == expected_result

def test_read_fasta():
    expected_result = "ATGCCGCCGCTCCTGGCGCCCCTGCTCTGCCTGGCGCTGCTGCCCGCGCTCGCCGCACGAGGTAGGCGCCCACCCACCCGCGAGCCCCCACTTTCCGCGCCCTTTGGAAACTTTGGCGGCGCCCGGCGCGCGCGCCCCAC"
    result = read_fasta(TEST_FASTA_FILE)
    assert result == expected_result

def test_translate():
    sequence="ATGTTTTTTTAATGTATGAGTAGGGGTTAG"    
    codon_table = {"ATG" : "start",
                   "TTT" : "P"    ,
                   "TAA" : "stop" ,
                   "TGT" : "C"    ,
                   "AGT" : "S"    ,
                   "AGG" : "A"    ,
                   "GGT" : "G"    ,
                   "TAG" : "stop" ,
                  } 
    expected_result = [(0,"PP"), (6,"SAG")]
    result = translate(sequence, codon_table)
    assert result == expected_result

@pytest.mark.find_start_codon
def test_find_start_codon():
    """Test start codon finder function"""
    assert find_start_codon(fasta_string="ATGCGGTAGTGAGATGGATAA") == [0, 13]
    assert find_start_codon(fasta_string="ATGCGGTAGTGAGATGGATAA", first=True) == [0]
    assert find_start_codon(fasta_string="ATGCGGTAGTGAGATGGATAA", oof=False) == [0]
