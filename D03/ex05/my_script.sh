#!/bin/bash

# create virtual environment
python3 -m venv django_venv

# activate virtual environment
source django_venv/bin/activate

# install requirements
#some prerequisite to install psycopg2 you have to install libpq-dev in your system
# or you can instead update psycopg2 to psycopg2-binary in requirement.txt This will install the binary version of psycopg2
pip install -r requirement.txt
