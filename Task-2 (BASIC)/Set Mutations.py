# Enter your code here. Read input from STDIN. Print output to STDOUT
A=int(input())
a=set(map(int,input().split()))
N=int(input())
for _ in range(N):
    opr,lnth=input().split()
    n=set(map(int,input().split()))
    if(opr=="intersection_update"):
        a.intersection_update(n)
    elif(opr=="update"):
        a.update(n)
    elif(opr=="symmetric_difference_update"):
        a.symmetric_difference_update(n)
    elif(opr=="difference_update"):
        a.difference_update(n)
print(sum(set(a)))
