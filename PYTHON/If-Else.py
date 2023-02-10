#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    r=n%2
    if n>=1 and n<=100:
        if r==1:
            print("Weird")
        else:
            if n<=5 and n>=2:
                print("Not Weird")
            elif n>5 and n<= 20:
                print("Weird")
            else:
                print("Not Weird")
   
