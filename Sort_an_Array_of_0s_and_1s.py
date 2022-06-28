n=int(input())
num=list(map(int,input().split()))
li1=[]
li2=[]
for i in num:
    if i==0:
        li1.append(0)
    else:
        li2.append(1)
li=li1+li2
for i in li:
    print(i,end=' ')