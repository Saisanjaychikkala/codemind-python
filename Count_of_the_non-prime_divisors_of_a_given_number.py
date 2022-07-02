def prime(num):
    if num==1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

n=int(input())
c=count=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i):
            c+=1
        count+=1
print(count-c)