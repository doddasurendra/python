a=float(input("enter the number of new loaves purchased"))
if(a<=0):
    print ("enter a positive number")
b=float(input("enter the number of old loaves purchased"))
c=a*185
d=b*185
f=float(d*60/100)
e=185
print('regular price:',e)
print('amount of new bread:',c)
print('amount of old bread:',f)
print('total price=',c+f)
