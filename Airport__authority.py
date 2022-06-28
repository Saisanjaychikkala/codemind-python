def weight_machine(n,w,t):
    c=0
    for i in w:
        if i<=t:
            c+=1
        else:
            c+=2
    return c
    
    
    
n=int(input())
weight=[]
for i in range(n):
    val=int(input())
    weight.append(val)
thr=int(input())
print(weight_machine(n,weight,thr))
