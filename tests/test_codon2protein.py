import pytest
from codon2protein import read_codon_table

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


