#!/usr/bin/env python3

import sys

def all_in(str):

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    arr = str.split(',')
    for i in range(len(arr)):
        target = arr[i].strip()
        target = ' '.join(word.capitalize() for word in target.split())
        if target is None or target == '':
            continue
        if target in states:
            print(f'{capital_cities[states[target]]} is the capital of {target}')
        elif target in capital_cities.values():
            capital_cities_key = list(capital_cities.keys())[list(capital_cities.values()).index(target)]
            print(f'{target} is the capital of {list(states.keys())[list(states.values()).index(capital_cities_key)]}')
        else:
            print(f'{target} is neither a capital city nor a state')

def main():
    if len(sys.argv) != 2:
        return
    str = sys.argv[1]
    all_in(str)

if __name__ == "__main__":
    main()