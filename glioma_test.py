from Bio.Seq import Seq

print("\n--- PEDIATRIC GLIOMA STEM CELL DATA TRACKER ---")

# 1. This represents a targeted DNA strand from a mutated neural stem cell
mutated_dna = Seq("ATGGCCATTGCAATGAGGTAA")
print(f"[1] Original DNA Blueprint: {mutated_dna}")

# 2. Transcription: The cell makes an mRNA copy of the mutated gene
mrna_copy = mutated_dna.transcribe()
print(f"[2] Transcribed mRNA Copy:  {mrna_copy}")

# 3. Translation: The cell reads the mRNA to build an active protein
protein_chain = mrna_copy.translate()
print(f"[3] Synthesized Protein:    {protein_chain}")

print("-----------------------------------------------\n")