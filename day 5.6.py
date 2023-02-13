from math import factorial
n =int(input('enter number of rows'))
m=int(input('enter the row number'))
s=0
if(n<1):
    print('invalid input')
elif(m<1):
    print('invalid input')
else:
    for i in range(n):
        for j in range(n - i + 1):
            print(end=" ")
        for j in range(i + 1):
            a=(factorial(i) // (factorial(j) * factorial(i - j)))
            if m==i+1:
                s=s+a
            print(a,end='  ')
        print( )
print()
print(s)
