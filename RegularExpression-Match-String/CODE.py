import re

filepath="C:\\Users\\Tarmah\\Desktop\\data.txt"
pattern = re.compile("^0\s*[xyz]$|[+-]?[1-9]*\s*[xyz]$")

with open(filepath) as fp:
    line = fp.readline()
    while line:
        if not re.match(pattern,line):
            print('No match with {}'.format(line))
        line = fp.readline()