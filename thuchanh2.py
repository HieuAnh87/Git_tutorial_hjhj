# Mã sinh viên: 239
import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def main():
    n = 39
    tmp = []
    for i in range(2, 1000):
        if isPrime(i):
            tmp.append(i)
    print(tmp[n-1])
main()