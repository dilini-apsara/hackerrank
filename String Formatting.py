def print_formatted(number):
    # your code goes here
    for i in range(n):
        pad=len(bin(n)[2:]) #define space 
       
        decimal=i+1
        octal=(oct(decimal))[2:]
        hexadecimal=(hex(decimal))[2:]
        Binary=(bin(decimal))[2:]
        print(str(decimal).rjust(pad),
        octal.rjust(pad),
        (hexadecimal.upper()).rjust(pad),
        Binary.rjust(pad))
        
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
