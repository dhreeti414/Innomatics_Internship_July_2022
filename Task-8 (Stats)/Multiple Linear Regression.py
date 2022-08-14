# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

m,n = [int(i) for i in input().split()]
X = []
Y = []

for i in range(n):
    data = input().split()
    X.append(data[:m])
    Y.append(data[m:])
    
q = int(input().strip())

new_X = []

for x in range(q):
    new_X.append(input().split())
    
X = np.array(X,float)
Y = np.array(Y,float)
new_X = np.array(new_X,float)

X_R = X-np.mean(X,axis=0)
Y_R = Y-np.mean(Y)

beta = np.dot(np.linalg.inv(np.dot(X_R.T,X_R)),np.dot(X_R.T,Y_R))

X_new_R = new_X-np.mean(X,axis=0)
Y_new_R = np.dot(X_new_R,beta)
new_Y = Y_new_R + np.mean(Y)

for i in new_Y:
    print(round(float(i),2))