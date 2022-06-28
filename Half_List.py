n=int(input())
li=list(map(int,input().split()))
li2=[]
mid=n//2
for i in range(n-1,mid-1,-1):
    li2.append(li[i])
for i in range(mid):
    li2.append(li[i])
for i in li2:
    print(i,end=' ')

