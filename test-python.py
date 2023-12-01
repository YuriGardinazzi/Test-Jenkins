#!/bin/python3 

import sys
import pandas as pd
import numpy as np
def say_hello():
    print("Ciao mondo, dalla pipeline e da dentro una funzione")
    print(f"version: {sys.version}")
    df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
    print(df.head())

if __name__ == "__main__":
    say_hello()