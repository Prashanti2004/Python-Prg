def fun(a):
    if(a==0):
        return 200
    fun(a-1)
    print(a)
x=int(input("Enter upper limit: "))
fun(x)
