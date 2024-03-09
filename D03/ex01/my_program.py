#!/usr/bin/env python3
from path import Path


def main():
	directory = Path('new_dir')
	directory.mkdir()
	file = Path('new_dir/new_file')
	file.touch()
	file.write_text("Hello, World!")
	text = file.read_text()
	print(text)

if __name__ == '__main__':
	main()