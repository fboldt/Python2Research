def read_seq(inputfile):
    """Reads and returns the input sequence with special characters removed."""
    
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n","")
    seq = seq.replace("\r","")
    return seq

def translate(seq):
    """Translate a string containing a nucleotide sequence into a string containing the corresponding sequence of amino acids.
    Nucleotides are translated in triplets using the table dictionary; each amino acid 4 is encoded with a string of length 1."""
    
    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""
    # check that the sequence length is divisibe by 3
    if len(seq) % 3 == 0:
        # loop over the sequence
        for i in range(0,len(seq), 3):
            # extract a single codon
            codon = seq[i:i+3]
            # look up the codon and store the result
            protein += table[codon]
    return protein

inputfile = "python_case_studies/translation/dna.txt"
dna = read_seq(inputfile)

protein = translate(dna[20:938])[:-1]

if protein == read_seq("python_case_studies/translation/protein.txt"):
    print("Success!")
