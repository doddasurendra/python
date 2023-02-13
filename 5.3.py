def perfectsquare(n):
    res=n
    
    for i in range(1,n+1):
        temp=i*i

        if temp>n:
            break
        else:
            res=min(res,1+perfectsquare(n-temp))
    return res
n=int(input("enter a number: "))
if n<=3:
    print("1")
else:
    print(perfectsquare(n))
