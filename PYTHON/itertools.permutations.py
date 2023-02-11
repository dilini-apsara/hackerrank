# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

I=(input().split())
S,k=I[0],int(I[1])
sList=list(S)
sList.sort()

for i in list(permutations(sList,k)):
    result=''
    for j in i:
        result+=j    
    print(result)
        
    
