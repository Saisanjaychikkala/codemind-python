n=int(input())
li=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if (li[i-1]%2==0 and li[i+1]%2!=0) or  (li[i+1]%2==0 and li[i-1]%2!=0):
        c+=1
print(c)