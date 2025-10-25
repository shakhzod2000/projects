import sys


if len(sys.argv) == 1: # only name of file provided
    print("USAGE: python3 app.py <password>")
else: # arg vars provided
    password = sys.argv[1]
    print("Password:", password)
