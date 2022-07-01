n=int(input())
arr=list(map(int,input().split()))
t1=0
for i in range(1,n,2):
    t1+=arr[i]
print(t1)