#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    namelst=s.split()
    new1=[]
    for i in namelst:
       
        if i[0].isalpha()==True:
            name=(i[0].upper())+(i[1:])    
            new1.append(name)        
        else:
            new1.append(i)         
    result=" ".join(new1)
    
    for i in range(len(s)):     
        if s[i]!=result[i]:
            if result[i].lower()!=s[i] and s[i]==" ":
                result=result[:i]+" "+result[i:]
       
    
    print(result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
