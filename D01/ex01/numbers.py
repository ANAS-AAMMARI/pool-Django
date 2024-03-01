#!/usr/bin/env python3

def print_file():
    f = open('numbers.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        numbers = line.strip().split(',')
        for number in numbers:
            print(int(number))

if __name__ == '__main__':
    print_file()
