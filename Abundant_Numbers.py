def ab_num(num):
    tot=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            tot+=i
    if tot>num:
        print(True)
    else:
        print(False)

num=int(input())
ab_num(num)