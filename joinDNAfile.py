def getString(file):
    with open(file, 'r') as infile:
        upperString = ''
        infile = [line.rstrip('\n') for line in infile]
        infile = ''.join(infile)
