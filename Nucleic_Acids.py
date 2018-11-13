class Dna(str):
    def __init__(self, dna_seq):
        all_nucleotides = set()
        if dna_seq:
            for nucl in dna_seq.upper():
                if nucl not in 'ATGC':
                    all_nucleotides.add(nucl)
            if len(all_nucleotides) == 0:
                self.sequence = dna_seq.upper()
            else:
                raise ValueError(
                    "Your sequence is inapropriate DNA sequence because it contains " + repr(all_nucleotides))
        else:
            raise ValueError('Your sequence is empty')

    def gc(self):
        return ((self.sequence.count('C') + self.sequence.count('G')) * 100) / len(self.sequence)

    def reverse_complement(self):
        complementarity = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'U': 'A'}
        reversed_seq = list()
        for i in self.sequence:
            reversed_seq.append(complementarity[i])
        if type(self) is Dna:
            return Dna(''.join(reversed(reversed_seq)))
        else:
            return Rna(''.join(reversed(reversed_seq)).replace('T', 'U'))

    def transcribe(self):
        if type(self) is Rna:
            raise ValueError('Your sequence is RNA, so it can not be transcribed')
        else:
            seq_type = input("Write type of your sequence (sense strand or antisense strand) from 5' to 3': ")
            if seq_type == "antisense strand":
                complementarity = {'T': 'A', 'C': 'G', 'G': 'C', 'A': 'U'}
                rna_seq = list()
                for nucl in self.sequence:
                    rna_seq.append(complementarity[nucl])
                rna_object = Rna(''.join(reversed(rna_seq)))
                return rna_object
            elif seq_type == "sense strand":
                return Rna(self.sequence.replace('T', 'U'))
            else:
                raise ValueError('Your write the incorrect type of your sequence')


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
                raise ValueError(
                    "Your sequence is inapropriate RNA sequence because it contains " + repr(all_nucleotides))
        else:
            raise ValueError('Your sequence is empty')
