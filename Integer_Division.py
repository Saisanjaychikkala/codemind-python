class number:
    def __init__(self,i):
        self.x=i
    def prime(self):
        if self.x==1:
            return 0
        for i in range(2,int(self.x**0.5)+1):
            if self.x%i==0:
                return 0
        return 1
    def __del__(self):
        pass
    def divide(self,divisor):
        return self.x//divisor

x=int(input())
num=number(x)
print(num.divide(10))