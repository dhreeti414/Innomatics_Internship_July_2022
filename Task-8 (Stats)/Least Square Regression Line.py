# Enter your code here. Read input from STDIN. Print output to STDOUT
n = 5
X = []
Y = []

for i in range(n):
    A, B = list(map(int, input().split()))
    X.append(A)
    Y.append(B)
    
def mean(m):
    return sum(m)/len(m)

def lsrl(X, Y):
    b = sum([(X[i] - mean(X)) * (Y[i] - mean(Y))for i in range(len(X))])/sum([(j - mean(X))**2 for j in X])
    a = mean(Y) - (b*mean(X))
    return a+(b*80)

print(round(lsrl(X, Y), 3))