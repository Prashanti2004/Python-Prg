def fun(n,m):
    if n==0:
        return 0
    print(m)
    fun(n-1,m+1)
    print(m)

x = int(input("Enter the number:"))
fun(1,x)