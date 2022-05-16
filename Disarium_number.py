def disarium(num):
    le=len(str(num))
    spd=0
    temp=num
    while num:
        rem=num%10
        spd+=rem**le
        le-=1
        num//=10
    if temp==spd:
        return True
    else:
        return False
        

num=int(input())
if disarium(num):
    print(True)
else:
    print(False)