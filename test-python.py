#!/bin/python3 

import sys

def say_hello():
    print("Ciao mondo, dalla pipeline e da dentro una funzione")
    print(f"version: {sys.version}")

if __name__ == "__main__":
    say_hello()