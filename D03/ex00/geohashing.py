#!/usr/bin/env python3

import sys
import antigravity

def main():
    if len(sys.argv) != 4:
        print("Usage: python geohashing.py <latitude> <longitude> <date>")
        #exemple : python geohashing.py 37.421542 -122.085589 2005-05-26-10458.68
        sys.exit(1)
    try:
        lat = float(sys.argv[1])
        lon = float(sys.argv[2])
        date = sys.argv[3].encode('utf-8')
        antigravity.geohash(lat, lon, date)
    except Exception as e:
        print('Error: ' + str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()