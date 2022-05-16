def prime(num):
    if num==1 or num==0:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
        
def left(num):
    for i in range(num-1,0,-1):
        if prime(i):
            return i
    else:
        return 0

def right(num):
    div=num+1
    while True:
        if prime(div):
            return div
        div+=1

test=int(input())
for i in range(test):
    num=int(input())
    if prime(num):
        print(num)
        continue
    else:
        lhs=left(num)
        rhs=right(num)
        if lhs==0:
            print(rhs)
            continue
        lhs_dif=num-lhs
        rhs_dif=rhs-num
        if lhs_dif<rhs_dif:
            print(lhs)
        elif lhs_dif==rhs_dif:
            if lhs<rhs:
                print(lhs)
            else:
                print(rhs)
        else:
            print(rhs)
