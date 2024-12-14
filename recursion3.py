def fun(n):
    if n >= 0:
        print(n)        
        fun(n - 1)
        if n >0:        
            print(n)     
x = int(input("Enter the number: "))
fun(x)