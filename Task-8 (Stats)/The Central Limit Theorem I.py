# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cdf(x, mean_weight, std):
    Sn = (x - mean_weight)/std
    return 0.5*(1 + math.erf(Sn/(math.sqrt(2)))) 

max_weight=int(input())
num_of_box=int(input())
mean_weight=int(input())
std=int(input())

mean_hash= num_of_box * mean_weight
std_hash= math.sqrt(num_of_box) * std

print(round(cdf(max_weight,mean_hash,std_hash),4))