def count_dna(dna):
    dna_count = {}
    dna_count['A'] = 0
    dna_count['C'] = 0
    dna_count['G'] = 0
    dna_count['T'] = 0
    for i in dna:
        if i == 'A':
            dna_count['A'] += 1
        elif i == 'C':
            dna_count['C'] += 1
        elif i == 'G':
            dna_count['G'] += 1
        elif i == 'T':
            dna_count['T'] += 1
        else:
            print("Invalid character found in DNA sequence.")
            raise SystemExit('Invalid DNA input.')
    print("{0} {1} {2} {3}".format(dna_count['A'], dna_count['C'], dna_count['G'], dna_count['T']))
def main():
    with open('./rosalind_dna.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for dna_string in content:
        print(dna_string)
        count_dna(dna_string)
main()
