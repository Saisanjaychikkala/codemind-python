def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def palindrome(num):
    temp=num
    rev=0
    while num:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if temp==rev:
        return True
    else:
        return False
        
n=int(input())
while True:
    n=n+1
    if prime(n):
        if palindrome(n):
            print(n)
            break