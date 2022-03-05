import math
class Prime():   
    def __init__(self, x):
        self.x = x

    def snt(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    def is_Prime(self):
        if self.snt(self.x):
            print(f"{self.x} la so nguyen to")
        else:
            print(f"{self.x} khong la so nguyen to")

    def next_prime(self):
        i = self.x + 1
        while self.is_Prime(i) != True:
            i += 1
        print(f"{i} la so tiep theo")

a = Prime(5)
a.is_Prime()
a.next_prime()