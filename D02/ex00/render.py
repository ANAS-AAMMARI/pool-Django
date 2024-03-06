#!/usr/bin/env python3

import sys # system
import os # operating system
import re # regular expressions
from settings import *

def render_template(template, values):
    with open(template, 'r') as file:
        content = file.read()
        cont = content.format(**values)
        output = re.sub(r"\.template$", ".html", template)
        with open(output, 'w') as file:
            file.write(cont)

def main():
    if len(sys.argv) != 2:
        print('Usage: render.py <template>')
        sys.exit(1)
    template = sys.argv[1]
    if not os.path.exists(template):
        print(f'Error: template file {template} does not exist')
        sys.exit(1)
    if not os.path.isfile(template):
        print(f'Error: template file {template} is not a file')
        sys.exit(1)
    if not os.access(template, os.R_OK):
        print(f'Error: template file {template} is not readable')
        sys.exit(1)
    if re.search(r"\.template$", template) is None:
        print(f'Error: template file {template} does not have a .template extension')
        sys.exit(1)
    settings_dict = {'Name': Name, 'surName': surName, 'Age': Age, 'Profession': Profession, 'Education': Education, 'Experience': Experience}
    render_template(template, settings_dict)
    

if __name__ == '__main__':
    main()
