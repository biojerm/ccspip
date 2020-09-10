class CompressedGene:
    def __init__(self, gene):
        self._compress(gene)

    def _compress(self, gene):
        self.bit_string = 1
        for nt in gene.upper():
            self.bit_string <<=2
            if nt == "A":
                self.bit_string |= 0b00
            elif nt == "C":
                self.bit_string |= 0b01
            elif nt == "G":
                self.bit_string |= 0b10
            elif nt == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nt))
    
    def decompress(self):
        gene = ""
        for i in range(0, self.bit_string.bit_length() -1, 2):
            # & uses bit math to set all but last two bits to zero
            # (effectively selecting the last two bits)
            bits = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self):
        return self.decompress()
    
if __name__ == "__main__":
    from sys import getsizeof
    original = 'ATCTGCTCGTCGTCAAAACCTTTGGCCTGCGGGT' * 100
    print(f"original is size {getsizeof(original)}")
    compressed = CompressedGene(original)
    print(f"compressed is size {getsizeof(compressed.bit_string)}")
    print(compressed)
    print(f"original and compressed are the same: {original == compressed.decompress()}")