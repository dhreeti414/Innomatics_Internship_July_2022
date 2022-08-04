# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
M=set(map(int,input().split()))
n=int(input())
N=set(map(int,input().split()))

for i in sorted(M^N):
    print(i)