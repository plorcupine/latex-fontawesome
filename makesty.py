import re

# Input file created from http://astronautweb.co/snippet/font-awesome/
INPUT_FILE = 'htmlfontawesome.txt'

with open(INPUT_FILE) as r:
  for line in r:
    # Expects to find 'fa-NAME' ending with "
    name = re.findall(r'fa-[^""]*', line)[0]
    # Expects to find '\fSYMBOL' ending with "
    symbol = re.findall(r'\\f[^"]*', line)[0]
