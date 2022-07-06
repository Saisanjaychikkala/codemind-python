m=int(input())
s=0
while True:
    n=str(m)
    for i in n:
        s+=int(i)**2
    if s<10:  
        if s==7 or s==1:
            print(True)
            break
        else:
            print(False)
            break
    m=s
    s=0