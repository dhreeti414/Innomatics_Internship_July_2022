# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    a=int(input())
    A=set(map(int,input().split()))
    b=int(input())
    B=set(map(int,input().split()))
    
    if len(A.difference(B)) == 0:
        print(True)
    else:
        print(False)
