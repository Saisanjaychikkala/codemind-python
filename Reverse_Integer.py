def reverse(num):
    rev=0
    if num<0:
        num=num*-1
        while num:
            rem=num%10
            rev=rev*10+rem
            num=num//10
        return rev*-1
    else:
        while num:
            rem=num%10
            rev=rev*10+rem
            num=num//10
        return rev

num=int(input())
print(reverse(num))