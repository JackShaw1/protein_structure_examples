from Bio.PDB import PDBParser
from Bio.PDB.SASA import ShrakeRupley

# Load PDB file
parser = PDBParser()
structure = parser.get_structure("structure", "AF-P34730-F1-model_v4_example.pdb")

# Create ShrakeRupley object
sr = ShrakeRupley()

# Calculate surface area
sr.compute(structure, level="S")

# Print total area
print("Total surface area:", structure.sasa)
