import math
n=int(input())
m=math.sqrt(n)
if m%int(m)==0:
    print(True)
else:
    print(False)