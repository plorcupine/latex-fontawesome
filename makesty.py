import re

# Input file created from http://astronautweb.co/snippet/font-awesome/
INPUT_FILE = 'htmlfontawesome.txt'
OUTPUT_FILE = 'fontawesome.sty'

OUTPUT_HEADER = r'''
% Identify this package.
\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{fontawesome}[2014/04/24 v4.0.3 font awesome icons]

% Requirements to use.
\usepackage{fontspec}

% Define shortcut to load the Font Awesome font.
\newfontfamily{\FA}{FontAwesome}
% Generic command displaying an icon by its name.
\newcommand*{\faicon}[1]{{
  \FA\csname faicon@#1\endcsname
}}
'''

with open(INPUT_FILE) as r, open(OUTPUT_FILE, 'w') as w:
  print(OUTPUT_HEADER, file=w)
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
            camel_name=camel_name, symbol=symbol), file=w)
  print(r'\endinput', file=w)
