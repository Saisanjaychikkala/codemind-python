def reverse(num):
    rev=0
    while num:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
    
def lhs(num):
    for i in range(num-1,0,-1):
        if reverse(i)==i:
            return i
 
def rhs(num):
    div=num+1
    while True:
        if reverse(div)==div:
            return div
        div+=1

n=int(input())
small=lhs(n)
big=rhs(n)
if (n-small)<(big-n):
    print(small)
elif (n-small)>(big-n):
    print(big)
else:
    print(small,big)