n=int(input())
arr=list(map(int,input().split()))
t1=t2=0
for i in range(0,n):
    if arr[i]%2==0:
        t1+=arr[i]
    else:
        t2+=arr[i]
print(abs(t2-t1))
