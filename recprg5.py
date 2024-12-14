#reduce the number to 1#
def countways(n):
    if (n == 1):
        return 0;
    elif (n % 2 == 0):
        return 1 + countways(n / 2);
    else:
        return 1 + min(countways(n - 1), countways(n + 1));

n = int(input("Enter a number:"))
print(countways(n))