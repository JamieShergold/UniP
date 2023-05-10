def read_fasta_file(file_path):
    sequences = {}
    with open(file_path, "r") as f:
        current_sequence = ""
        current_header = None
        for line in f:
            if line.startswith(">"):
                if current_header is not None:
                    sequences[current_header] = current_sequence
                current_header = line.strip()[1:]
                current_sequence = ""
            else:
                current_sequence += line.strip()
        sequences[current_header] = current_sequence
    return sequences


def extract_sequence_range(sequences, positions):
    extracted_sequences = {}
    for accession, sequence in sequences.items():
        start, end = positions.get(accession, (1, len(sequence)))
        extracted_sequence = sequence[start-1:end]
        extracted_sequences[accession] = extracted_sequence
    return extracted_sequences


fasta_file_path = "1Dataset_file_GB.fasta"
sequences = read_fasta_file(fasta_file_path)
positions = {
    "AE007317.1": (70250, 70401),
    "AP017971.1": (81032, 81184),
    # accessions and positions here
}
extracted_sequences = extract_sequence_range(sequences, positions)

output_file_path = "extracted_sequences.txt"
with open(output_file_path, "w") as f:
    for accession, sequence in extracted_sequences.items():
        f.write(">" + accession + "\n")
        f.write(sequence + "\n")
