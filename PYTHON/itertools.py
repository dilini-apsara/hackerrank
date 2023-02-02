
from itertools import product
A=list(map(int,(input()).split()))
B=list(map(int,(input()).split()))

lst_AB=list(product(A,B))
for i in lst_AB:
    print(i,end=" ")
