def fun(n):
    if n == 0 :
        return 200 
    print(n)
    t = fun(n-1)
    return t 
x = int(input("Enter the number:"))
print(fun(x))