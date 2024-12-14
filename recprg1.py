#write a code to find factiorial to the given number#
def fact(n):
    if(n<0):
        print("fact is not defined")
    elif n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    print(fact(n))
x = int(input("enter a number:"))
result = fact(x)
print(result)