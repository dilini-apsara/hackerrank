import textwrap
def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    if k>=1 and k<=n:
        if n%k==0:
            sub=textwrap.wrap(string,k) # creating a list 
            for i in sub:
                s=""
                for j in range(k):
                    if i[j] not in s:
                        s+=i[j]  
                    
                print(s)
    return 
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
