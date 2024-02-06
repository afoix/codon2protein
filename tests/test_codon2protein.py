import pytest
from codon2protein import read_codon_table, find_start_codon

# Define test data
TEST_CODON_TABLE = 'test_codon_table.csv'  # Assume this is your test CSV file

# Example test data in test_codon_table.csv:
# Codon,Amino Acid Abbreviation,Amino Acid Code,Amino Acid Name
# UUU,Phe,F,Phenylalanine
# CUG,Leu,L,Leucine
# AUU,Ile,I,Isoleucine 

def test_create_codon_to_amino_acid_dict():
    expected_result = {'UUU': 'F', 'CUG': 'L', 'AUU': 'I'}
    result = read_codon_table(TEST_CODON_TABLE)
    assert result == expected_result

from codon2protein import find_start_codon

@pytest.mark.find_start_codon
def test_find_start_codon():
    """Test start codon finder function"""
    assert find_start_codon(fasta_string="ATGCGGTAGTGAGATGGATAA") == [0, 13]
    assert find_start_codon(fasta_string="ATGCGGTAGTGAGATGGATAA", first=True) == [0]
    assert find_start_codon(fasta_string="ATGCGGTAGTGAGATGGATAA", oof=False) == [0]
