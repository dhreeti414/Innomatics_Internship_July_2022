# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cdf(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / (std * math.sqrt(2))))*100

mean,std= map(int,input().split())
num=int(input())
grade=int(input())

print(round(100 - cdf(num, mean, std), 2))
print(round(100 - cdf(grade, mean, std), 2))
print(round(cdf(grade, mean, std), 2))
