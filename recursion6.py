def fun(n,m):
    if n > m:
        return 
    print(n)
    fun(n + 1, m)
    print(n)

x=int(input("Enter the number:"))
fun(1,x)