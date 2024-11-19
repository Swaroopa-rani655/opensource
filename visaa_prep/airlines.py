import math
x,n=map(int,input().split())
tot=math.ceil(n/100)
planes=max(0,tot-x)
print(planes)
