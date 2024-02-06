import os

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
