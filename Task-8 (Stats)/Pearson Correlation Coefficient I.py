# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))

mu_X= sum(X)/n
mu_Y= sum(Y)/n

stdv_X= math.sqrt(sum([(i - mu_X)**2 for i in X]) / n)
stdv_Y = math.sqrt(sum([(i - mu_Y)**2 for i in Y]) / n)

covariance = sum([(X[i]- mu_X) * (Y[i]- mu_Y) for i in range(n)])
pearson_correlation_coefficient= covariance/(n * stdv_X * stdv_Y)

print(round(pearson_correlation_coefficient,3))