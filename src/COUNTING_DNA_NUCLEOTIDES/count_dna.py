if __name__ == '__main__':
    with open('./rosalind_dna.txt') as f:  # open file
        content = f.readlines()            # store lines
    content = [s.strip() for s in content] # strip lines
    content = content[0]                   # get 1st line
    a = content.count('A')                 # count A
    c = content.count('C')                 # count C
    g = content.count('G')                 # count G
    t = content.count('T')                 # count T
    print(a,c,g,t)                         # print output
