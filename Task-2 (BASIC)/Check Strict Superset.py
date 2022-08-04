# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(map(int,input().split()))
n=int(input())
flag=0
for i in range(n):
    B=set(map(int,input().split()))
    if not B.issubset(A):
        flag=1
    if(len(B)>=len(A)):
            flag=1

if flag == 0:
    print(True)
else:
    print(False)
