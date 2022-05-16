def reverse(num):
    rev=0
    while num:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev


num=int(input())
rev=reverse(num)
if num**2==reverse(rev**2):
    print(True)
else:
    print(False)