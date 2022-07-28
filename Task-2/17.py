# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split()
n_ele=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
happiness=0

for i in n_ele:
    if i in A:
        happiness = happiness + 1
    elif i in B:
        happiness = happiness - 1 
print(happiness)
