# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *

AB=int(input())
BC=int(input())
hypotenuseAC= hypot(AB,BC)
CM=AM= hypotenuseAC/2
BCA=asin(AB/hypotenuseAC)
BM=sqrt((BC**2+CM**2)-(2*BC*CM*cos(BCA)))
result= round(degrees(asin(sin(BCA)*CM/BM)))
degree= chr(176)
print(result,degree,sep='')