def total(num):
    tot=0
    rem=0
    while num:
        rem=num%10
        tot=tot+rem
        num=num//10
    return tot

num=int(input())
tot=0
tot=total(num)
if len(str(tot))==1:
    print(tot)
else:
    tot=total(tot)
    if len(str(tot))==1:
        print(tot)
    else:
        tot=total(tot)
        if len(str(tot))==1:
            print(tot)
