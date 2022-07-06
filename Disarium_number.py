n=input()
a=list(n)
p,s=1,0
for i in n:
    s+=int(i)**p
    p+=1
if s==int(n):
    print(True)
else:
    print(False)