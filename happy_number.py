n=int(input())
num=n
s=0
while num:
    rem=num%10
    s=s+rem**2
    num=num//10
    if num==0 and s>9:
        num=s
        s=0
if s==7 or s==1:
    print(True)
else:
    print(False)
        
    
    