# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cdf(x, mean_, std):
    Sn = (x - mean_)/std
    return 0.5*(1 + math.erf(Sn/(math.sqrt(2)))) 

max_=int(input())
num_of_=int(input())
mean_=float(input())
std=float(input())

mean_hash= num_of_ * mean_
std_hash= math.sqrt(num_of_) * std

print(round(cdf(max_,mean_hash,std_hash),4))