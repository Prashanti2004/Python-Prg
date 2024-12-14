n = int(input())

def computeXOR(n):
    res = 0
    for i in range(1,n+1):
        res = res ^ i
    return res
print(computeXOR(n))