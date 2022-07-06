n=int(input())
s=0
for i in range(1,(n//2)+4):
    if n%i==0:
        s+=i
if(s>i):
    print(True)
else:
    print(False)