def minion_game(string):
    # your code goes here
    vowel="AEIOU"
    stuart=0
    kevin=0
    lenth=len(string)
    for i in range(lenth):
        if string[i] in vowel:
            kevin=kevin+(lenth-i)
        else:
            stuart+=(lenth-i)
    if stuart>kevin:
        print("Stuart",end=" " )
        print(stuart)
    elif stuart<kevin:
        print("Kevin",end=" ")
        print(kevin)
    else:
        print("Draw")
    return
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
