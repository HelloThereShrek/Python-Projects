#! /usr/bin/python

import binascii

filename = raw_input("File name (must be in same directory as program): ")
vieworiginal = raw_input("View original contents (y/n)? ")

with open(filename, 'rb') as f:
    content = f.read()

if vieworiginal == "y":
    print("Original:\n" + content + "\n\n\n")
else:
    pass

content = binascii.hexlify(content)

print("Hex code:\n" + ':'.join(content[i:i+2] for i in range(0, len(content), 2)))