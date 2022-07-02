def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

m=int(input())
n=int(input())
t=m+n
s=t
while True:
    t=t+1
    if prime(t):
        print(t-s)
        break
        
    