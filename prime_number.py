#to check whether a number prime or not

def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
        
num=int(input())
if prime(num):
    print('Prime'.lower())
else:
    print('Not a Prime'.lower())
        