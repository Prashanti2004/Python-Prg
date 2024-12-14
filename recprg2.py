#write a code to check weather the number is prime or not.#
def prime(n,i=2):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n%i == 0:
        return 0
    if i*i > n:
        return 1
    return prime(n,i+1)
n = int(input("Enter a number:"))
res = prime(n)
if res == 1:
    print(f"{n} is a prime")
else:
    print(f"{n} is not prime")