import string

def print_rangoli(size):
    # your code goes here
    alphabet=string.ascii_lowercase
    width=4*size-3
    for i in list(range(size))[::-1] + list(range(1,size)):
        print('-'.join(alphabet[size-1:i:-1] + alphabet[i:size]).center(width,'-'))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)