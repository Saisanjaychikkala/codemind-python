def auto(num,le):
    sqr=num*num
    while le:
        rem1=num%10
        rem2=sqr%10
        if rem1!=rem2:
            return False
        num=num//10
        sqr=sqr//10
        le-=1
    return True


num=input()
le=len(num)
if auto(int(num),le):
    print('Automorphic Number')
else:
     print('Not an Automorphic Number')
