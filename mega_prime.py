#mega prime
def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True

def digits(num):
    while num:
        rem=num%10
        if rem==1 or rem==0:
            return False
        num=num//10
        if prime(rem):
            continue
        else:
            return False
    return True



num=int(input())
if prime(num):
    if digits(num):
        print('Mega Prime')
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
    