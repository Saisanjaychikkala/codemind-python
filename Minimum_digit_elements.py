def count(num):
    c=0
    while num:
        num=num//10
        c+=1
    return c
n=int(input())
arr=list(map(int,input().split()))
l=min(arr)
c=count(l)
co=0
for i in arr:
    if count(i)==c:
        co+=1
print(co)