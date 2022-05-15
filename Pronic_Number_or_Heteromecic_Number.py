def pronic(num):
    for i in range(1,int(num**0.5)+1):
        for j in range(1,int(num**0.5)+1):
            if i*(j+1)==num:
                return True
    return False


num=int(input())
if pronic(num):
    print('YES')
else:
    print('NO')