# COUNT(Text, Pattern) 1A
def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count
# FREQUENTWORDS(Text, k) 1B
def frequent_patterns(text, k):
    freq_patterns = []
    count = {}
    for i in range(len(text) - k):
        pattern = text[i:i + k]
        count[i] = pattern_count(text, pattern)
    maxCount = 0
    for c in count:
        if count[c] > maxCount:
            maxCount = count[c]
    for i in range(len(text) - k):
        if count[i] == maxCount:
            freq_patterns.append(text[i:i + k])
    # remove duplicates
    final_list = []
    for kmer in freq_patterns:
        if kmer not in final_list:
            final_list.append(kmer)
    return final_list

# REVERSECOMPLEMENT(Pattern) 1C
def reverse_complement(dna):
    print("Pattern: 5' - {} - 3'".format(dna))
    complement = ""
    for c in dna:
        if c == 'A':
            complement += 'T'
        elif c == 'C':
            complement += 'G'
        elif c == "G":
            complement += 'C'
        elif c == 'T':
            complement += 'A'
    return "Reverse Complement: 5' - {} - 3'".format(complement[::-1])

# PATTERNMATCH(Pattern, Genome) 1D
def pattern_match(pattern, genome):
    positions = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i + len(pattern)] == pattern:
            positions.append(i)
    return positions

def symbol_to_number(symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3
    else:
        return -1

# PATTERNTONUMBER(Pattern) 1L
def pattern_to_number(pattern):
    if pattern == "":
        return 0
    else:
        symbol = pattern[-1]
        prefix = pattern[0:len(pattern) - 1]
        return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)

def number_to_symbol(index):
    if index == 0:
        return 'A'
    elif index == 1:
        return 'C'
    elif index == 2:
        return 'G'
    elif index == 3:
        return 'T'
    else:
        return ''
def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefixIndex = index // 4
    r = index % 4
    symbol = number_to_symbol(r)
    prefixPattern = number_to_pattern(prefixIndex, k - 1)
    return prefixPattern + symbol

def main():
    print(pattern_count("NavalHelloNavalNavalNavalHelloNaval", "Naval")) # Expected output: 4\n

    print(frequent_patterns("ACAACTATGCATACTATCGGGAACTATCCT", 5))

    print(reverse_complement("AGTCGCATAGT"))

    print(pattern_match("CAT", "ABCATCATABCAT"))

    print(pattern_to_number("AGT"))

    print(number_to_pattern(9904, 7))
main()
