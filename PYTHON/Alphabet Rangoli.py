def print_rangoli(size):
    # your code goes here
    alphabet="abcdefghijklmnopqrstuvwxyz"
    nlist=(list(alphabet[:size]))
    nlist.reverse()
    length=4*size-3
    
    if size==1:
        print("a")
    else:
        
        #upper half 
    
        for i in range(size):
            nlist1=nlist[:i]
            nlist1.reverse() 
            c="-".join(nlist[:i+1])+'-'+"-".join((nlist1))
            print(c.center(length,'-'))
        
        #bottom half
        
        size-=1
        for i in range(size):
            nlist1=nlist[:size-i]
            nlist1.reverse()
            c="-".join(nlist[:size-i])+"-"+"-".join(nlist1[1:])
            print(c.center(length,"-"))

       
    return 

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
