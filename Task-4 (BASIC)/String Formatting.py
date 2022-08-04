def print_formatted(number):
    # your code goes here
    l = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(l,' '),end=' ')
        print(oct(i).replace('0o','').rjust(l,' '),end=' ')
        print(hex(i).replace('0x','').upper().rjust(l,' '),end=' ')
        print(bin(i).replace('0b','').rjust(l,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)