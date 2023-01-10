value=list(map(int,(input()).split()))
N,M=value
if N>5 and N<101:
    #upper half
    count=1
    for i in range(N//2):
        
        print(('.|.'*count).center(M,'-'))
        count+=2
    #Middle one
    print("WELCOME".center(M,'-'))  
    #Lower half
    countnew=count-2
    for i in range(N//2):
        print(('.|.'*countnew).center(M,'-')) 
        countnew-=2
                   
