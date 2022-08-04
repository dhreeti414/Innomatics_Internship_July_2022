import numpy

n,m=map(int,input().split())
A= numpy.array([input().split() for _ in range(n)],int)
B= numpy.array([input().split() for _ in range(n)],int)
print (numpy.add(A,B))
print (numpy.subtract(A,B))
print (numpy.multiply(A,B))
print (numpy.floor_divide(A,B))
print (numpy.mod(A,B))
print (numpy.power(A,B))