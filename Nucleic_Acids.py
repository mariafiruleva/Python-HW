class Dna(str):
    def __init__(self, dna_seq):
        all_nucleotides = set()
        if len(dna_seq) != 0:
            for nucl in dna_seq.upper():
                if nucl not in 'ATGC':
                    all_nucleotides.add(nucl)
            if len(all_nucleotides) == 0:
                self.sequence = dna_seq.upper()
            else:
                raise ValueError(dna_seq + " is inapropriate DNA sequence because it contains " + repr(all_nucleotides))
        else:
            raise ValueError('Your sequence is empty')

    def gc(self):
        gc_content = ((self.sequence.count('C') + self.sequence.count('G')) * 100) / len(self.sequence)
        return gc_content

    def reverse_complement(self):
        complementarity = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'U': 'A'}
        reversed_seq = list()
        for i in self.sequence:
            reversed_seq.append(complementarity[i])
        return ''.join(reversed_seq)

    def transcribe(self):
        complementarity = {'T': 'A', 'C': 'G', 'G': 'C', 'A': 'U'}
        rna_seq = list()
        for i in self.sequence:
            rna_seq.append(complementarity[i])
        rna_object = Rna(''.join(rna_seq))
        return rna_object


class Rna(Dna):
    def __init__(self, rna_seq):
        all_nucleotides = set()
        if len(rna_seq) != 0:
            for nucl in rna_seq.upper():
                if nucl not in 'AUGC':
                    all_nucleotides.add(nucl)
            if len(all_nucleotides) == 0:
                self.sequence = rna_seq.upper()
            else:
                raise ValueError(rna_seq + " is inapropriate RNA sequence because it contains " + repr(all_nucleotides))
        else:
            raise ValueError('Your sequence is empty')

