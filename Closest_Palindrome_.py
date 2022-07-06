n=int(input())
for i in range(n-1,0,-1):
    j=str(i)
    if j==j[::-1]:
        low=i
        break
for i in range(n+1,n**2):
    j=str(i)
    if j==j[::-1]:
        high=i
        break
if((n-low)>(high-n)):
    print(high)
elif((n-low)<(high-n)):
    print(low)
else:
    print(low,high)