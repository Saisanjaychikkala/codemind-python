n=int(input())
li=list(map(int,input().split()))
li2=[]
for i in li:
    if i not in li2:
        li2.append(i)
for i in li2:
    print(i,end=' ')
    