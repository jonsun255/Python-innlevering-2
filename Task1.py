import os
import sys


print("what file do you want to access)")
filename = str(input())

try:
    with open(filename, 'r') as file:
        readFile = [filename.strip() for filename in file]
        print("file exists")
        print(readFile)
except (FileNotFoundError, PermissionError):
        print("file does not exist")

