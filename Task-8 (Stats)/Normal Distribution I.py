# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cdf(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / (std * math.sqrt(2))))

mean,std= map(int,input().split())
num=float(input())
lo_bnd,up_bnd= map(int,input().split())

print(round(cdf(num, mean, std), 3))
print(round(cdf(up_bnd, mean, std) - cdf(lo_bnd, mean, std), 3))
