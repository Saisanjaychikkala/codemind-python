n=int(input())
arr=list(map(int,input().split()))
t1=0
for i in arr:
    if i%2==0:
        t1+=i
print(t1)