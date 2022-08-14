# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

sample_size = int(input())
mean= int(input())
std= int(input())
dist_per= float(input())
z_value= float(input())

sample_std= std/math.sqrt(sample_size)

A=mean-(z_value * sample_std)
B=mean+(z_value * sample_std)

print(round(A,2))
print(round(B,2))