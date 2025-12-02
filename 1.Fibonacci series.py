def fibonacci_series(n):
    f1=0
    f2=1
    f3=1
    count=2
    print("fiboancci series is:")
    print(f1," ",f2,end=" ")
    while count<n:
        print(f3,end=" ")
        count=count+1
        f1=f2
        f2=f3
        f3=f1+f2
n=int(input("enter the limit: "))
fibonacci_series(n)