def reverse(num):
    rev=0
    while num:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
n=int(input())
if reverse(n)==n:
    print(True)
else:
    print(False)