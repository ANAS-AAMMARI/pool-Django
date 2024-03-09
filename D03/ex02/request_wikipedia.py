#!/usr/bin/env python3

import requests
import sys
import  json
import dewiki

def request_wikipedia(query):
    try:
        response = requests.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'parse',
                'format': 'json',
                'page': query,
                'prop': 'wikitext',
                'redirects': 'true',
            }
        )
        response.raise_for_status()
        data = response.json()
        wikitext = data['parse']['wikitext']['*']
        return dewiki.from_string(wikitext)
    except requests.RequestException as e:
        print(f'Error: {e}')
        sys.exit(1)
    

def write_to_file(query):
    fileName = f"{query.replace(' ', '_')}.wiki"
    with open(fileName, 'w', encoding='utf-8') as file:
        file.write(request_wikipedia(query))

def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <query>')
        sys.exit(1)
    query = sys.argv[1]
    write_to_file(query)

if __name__ == '__main__':
    main()