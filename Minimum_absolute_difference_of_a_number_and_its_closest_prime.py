

def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
        
def left(num):
    for i in range(num-1,0,-1):
        if prime(i):
            return i

def right(num):
    div=num+1
    while True:
        if prime(div):
            return div
        div+=1

num=int(input())
if prime(num):
    print(0)
    quit()
else:
    lhs=left(num)
    rhs=right(num)
    lhs_dif=num-lhs
    rhs_dif=rhs-num
    if lhs_dif<rhs_dif:
        print(lhs_dif)
    else:
        print(rhs_dif)
