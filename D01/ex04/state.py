#!/usr/bin/env python3

import sys

def state(capital_city):
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
    if capital_city in capital_cities.values():
        capital_cities_key = list(capital_cities.keys())[list(capital_cities.values()).index(capital_city)]
        return list(states.keys())[list(states.values()).index(capital_cities_key)]
    else:
        return "Unknown state"

def main():
    if len(sys.argv) != 2:
        return
    capital_city = sys.argv[1]
    print(state(capital_city))

if __name__ == "__main__":
    main()

