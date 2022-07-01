n=int(input())
arr=list(map(int,input().split()))
t1=t2=0
for i in range(0,n,2):
    t1+=arr[i]
for i in range(1,n,2):
    t2+=arr[i]
print(abs(t1-t2))