# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
string=input().split()
s,k=list(string[0]),int(string[1])
s.sort()
for n in range(1,k+1):
    for i in list(combinations(s,n)):
        result=''
        for j in i:
            result+=j
        print(result)
