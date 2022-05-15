def amicable(num):
    sd=0
    for i in range(1,num//2+1):
        if num%i==0:
            sd+=i
    return sd


num1=int(input())
num2=int(input())
if amicable(num1)==num2 and amicable(num2)==num1:
    print("Amicable")
else:
     print("Not Amicable")
    