from Bio.PDB import PDBParser, Selection

# Function to count residues
def count_residues(structure):
    residue_count = {}
    for model in structure:
        for chain in model:
            for residue in chain:
                residue_name = residue.get_resname()
                if residue_name in residue_count:
                    residue_count[residue_name] += 1
                else:
                    residue_count[residue_name] = 1
    return residue_count

# Load PDB file
parser = PDBParser()
structure = parser.get_structure("structure", "your_pdb_file.pdb")

# Count residues
residue_counts = count_residues(structure)

# Print distribution
print("Residue Distribution:")
for residue, count in residue_counts.items():
    print(f"{residue}: {count}")
