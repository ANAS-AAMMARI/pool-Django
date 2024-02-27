#!/bin/sh

# Check if a bit.ly link is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <bit.ly link>"
    exit 1
fi

# Use curl to follow redirects and get the final destination URL
final_url=$(curl -sIL "$1" | grep -i -m 1 location | cut -d' ' -f2)

echo $final_url
