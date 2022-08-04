# Enter your code here. Read input from STDIN. Print output to STDOUT
K=int(input())
roomno=list(map(int,input().split()))

set_rmno=set(roomno)
sum_rmno=sum(roomno)
sumset_rmno=sum(set_rmno)*K 
Captain_rmno=(sumset_rmno - sum_rmno)//(K-1)
print(Captain_rmno)