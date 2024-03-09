#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys

def roads_to_philosophy(world_to_search):
    try:
        visited = set()
        while True:
            url = "https://en.wikipedia.org/wiki/{}".format(world_to_search)
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.HTTPError as e:
                if e.response.status_code == 404:
                    return print("It's a dead end !")
                print(e)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find(id='firstHeading').text
            if title in visited:
                return print("It's a infinite loop !")
            visited.add(title)
            print(title)
            if title == 'Philosophy':
                return print(f'{len(visited)} roads from {world_to_search} to philosophy !')
            p_elments = soup.find(id='mw-content-text').find(class_='mw-parser-output').find_all('p')
            for p in p_elments:
                for link in p.find_all('a'):
                    if link.get('href').startswith('/wiki/') and ':' not in link.get('href'):
                        world_to_search = link.get('href').replace('/wiki/', '')
                        break
                else:
                    continue
                break
            else:
                return print("It's a dead end !")
        
    except Exception as e:
        print(e)
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
       print('Usage: python3 roads_to_philosophy.py <url>')
       sys.exit(1)
    world_to_search = sys.argv[1]
    roads_to_philosophy(world_to_search)

       
if __name__ == '__main__':
    main() 
