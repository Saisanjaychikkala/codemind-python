def verybigsum(li):
    tot=0
    for i in li:
        tot+=i
    return tot
    

n=int(input())
li=list(map(int,input().split()))
print(verybigsum(li))