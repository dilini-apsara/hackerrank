# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X=int(input())
shoeSize=Counter(map(int,(input()).split()))
N=int(input())

Total=0
for i in range(N):
    size,price=input().split()

    if int(size) in shoeSize:
        if shoeSize[int(size)]>0:
            Total+=int(price)
            (shoeSize)[int(size)]-=1

print(Total)
