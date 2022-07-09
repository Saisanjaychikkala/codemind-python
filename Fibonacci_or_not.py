n=int(input())
a=0
b=1
flag=0
for i in range(n):
    if a==n:
        flag=1
        break
    c=a+b
    a=b
    b=c
if flag==1:
    print(True)
else:
    print(False)
    