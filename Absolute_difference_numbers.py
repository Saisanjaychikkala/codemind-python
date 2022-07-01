m,x=map(int,input().split())
n=str(m)
s1=n[0:x]
s2=n[(len(n)-x):len(n)+1]
print(abs(int(s1)-int(s2)))
