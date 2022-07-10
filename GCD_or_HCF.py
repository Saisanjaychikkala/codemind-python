n,m=map(int,input().split())
b=min(n,m)
if b!=0:
    for i in range(b,0,-1):
        if n%i==0 and m%i==0:
            print(i)
            break
else:
    print(max(n,m))
