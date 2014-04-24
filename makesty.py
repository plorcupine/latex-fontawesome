import re

# Input file created from http://astronautweb.co/snippet/font-awesome/
INPUT_FILE = 'htmlfontawesome.txt'

with open(INPUT_FILE) as r:
  for line in r:
    # Expects to find 'fa-NAME' ending with "
    name = re.findall(r'fa-[^""]*', line)[0]
    # Expects to find '\fSYMBOL' ending with "
    symbol = re.findall(r'\\f[^"]*', line)[0][1:].upper()

    camel_case = [w.capitalize() for w in name.split('-')]
    camel_case[0] = camel_case[0].lower()
    camel_name = ''.join(camel_case)

    name = name.lstrip('fa-')
    print('\expandafter\def\csname faicon@{name}\endcsname '
          '{{\symbol{{"{symbol}}}}} \def\{camel_name} '
          '{{{{\FA\csname faicon@{name}\endcsname}}}}'.format(name=name,
            camel_name=camel_name, symbol=symbol))
