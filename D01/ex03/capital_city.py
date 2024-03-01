#!/usr/bin/env python3

import sys

def capital_city(country):
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
    if country in states:
        return capital_cities[states[country]]
    else:
        return "Unknown state"

def main():
    if len(sys.argv) != 2:
        return
    country = sys.argv[1]
    print(capital_city(country))

if __name__ == "__main__":
    main()