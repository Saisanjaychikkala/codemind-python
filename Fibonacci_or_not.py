n=int(input())
a=0
b=1
for i in range(0,n+1):
    c=a+b
    a=b
    b=c
    if a==n:
        print(True)
        break
else:
    print(False)
    